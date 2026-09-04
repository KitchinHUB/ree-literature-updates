"""Compare each bibliography entry against the registry's record of that DOI.

`verify_bib.py` asks whether a DOI resolves and whether the title of the work
it resolves to matches. That is not enough. An entry can carry a correct DOI
and a correct title and still describe the wrong paper in every other field --
the audit this script was written for found 150 such entries, 51 of which
credited authors who had nothing to do with the work.

So this asks the next question: does the record that comes back agree with what
the entry says about it? Compared are the first author (against the whole
registry author list, since bibliographies disagree about author order more
often than they are wrong about who wrote a paper), the year, the container
title, the volume and the pages.

Nothing here is repaired automatically. The script reports; correcting an entry
is a judgement about which of two records to believe, and a few of the
divergences it finds are deliberate -- an entry whose `note` field explains the
disagreement is reported as DOCUMENTED rather than as a mismatch.

    python3 tools/check_bib_metadata.py                  # every entry
    python3 tools/check_bib_metadata.py keys.txt         # one key per line
    python3 tools/check_bib_metadata.py keys.txt out.json
"""
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

UA = ("ree-book/1.0 (https://github.com/KitchinHUB/ree-literature-updates; "
      "mailto:jkitchin@andrew.cmu.edu)")

TITLE_FLOOR = 0.80
JOURNAL_FLOOR = 0.60


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, r.read()
        except Exception:
            time.sleep(1.5)
    return None, b""


def norm(t):
    """Fold a string to bare lowercase words for comparison.

    LaTeX accents have to go before the comparison, not after: an entry that
    writes L\\'opez and a registry that writes López name the same person, and
    a naive comparison calls that a fabricated author.
    """
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = re.sub(r"\\[a-zA-Z]+\s*", " ", t)          # \textbf, \'{}, \ss ...
    # Bare accent marks, and both apostrophes: a bibliography writes
    # O'Connell-Danes and a registry writes O’Connell-Danes, and dropping only
    # one of the two turns one surname into two different ones.
    t = re.sub(r"[\\'’‘`^\"~=.]", "", t)
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def entries(path="references.bib"):
    s = open(path).read()
    out = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}\n", s, re.S):
        kind, key, body = m.group(1), m.group(2).strip(), m.group(3)
        f = {}
        for fm in re.finditer(r"^\s*([a-z]+)\s*=\s*\{(.*?)\}\s*,?\s*$", body,
                              re.S | re.M):
            f[fm.group(1)] = re.sub(r"\s+", " ", fm.group(2)).strip()
        f["_type"] = kind
        out[key] = f
    return out


def crossref(doi):
    st, b = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    if st != 200:
        return None
    try:
        return json.loads(b)["message"]
    except Exception:
        return None


def datacite(doi):
    st, b = get(f"https://api.datacite.org/dois/{urllib.parse.quote(doi)}")
    if st != 200:
        return None
    try:
        return json.loads(b)["data"]["attributes"]
    except Exception:
        return None


def registry(doi):
    """The DOI's record, flattened to the fields worth comparing.

    DOE software and dataset DOIs are minted at DataCite rather than CrossRef,
    and which registry issued a DOI says nothing about the quality of the work.
    """
    m = crossref(doi)
    if m is not None:
        title = (m.get("title") or [""])[0]
        titles = [title]
        sub = m.get("subtitle") or []
        if sub and norm(sub[0]) not in norm(title):
            titles.append(f"{title}: {sub[0]}")
        dp = ((m.get("issued") or {}).get("date-parts") or [[None]])[0]
        # An institutional author has a `name` and no `family`; dropping it
        # leaves an empty string that matches nothing.
        authors = [a.get("family") or a.get("name") or ""
                   for a in (m.get("author") or [])]
        containers = [c for c in (m.get("container-title") or []) if c]
        return dict(src="crossref", title=title, titles=titles,
                    year=str(dp[0] or ""), authors=[a for a in authors if a],
                    containers=containers,
                    journal=containers[0] if containers else "",
                    volume=m.get("volume") or "", pages=m.get("page") or "")
    m = datacite(doi)
    if m is None:
        return None
    title = (m.get("titles") or [{}])[0].get("title", "")
    return dict(src="datacite", title=title, titles=[title],
                year=str(m.get("publicationYear") or ""),
                authors=[c.get("name", "") for c in (m.get("creators") or [])],
                containers=[], journal="", volume="", pages="")


def check(entry):
    doi = (entry.get("doi") or "").strip()
    if not doi:
        return "NO-DOI", [], {}
    reg = registry(doi)
    if reg is None:
        return "UNRESOLVED", ["DOI resolves in neither CrossRef nor DataCite"], {}

    problems = []

    sim, best = max((difflib.SequenceMatcher(
        None, norm(entry.get("title", "")), norm(c)).ratio(), c)
        for c in reg["titles"])
    if sim < TITLE_FLOOR:
        problems.append(
            f"title {sim:.2f}: bib={entry.get('title', '')!r} reg={best!r}")

    bib_auth = entry.get("author", "")
    if bib_auth and reg["authors"]:
        first = re.split(r"\s+and\s+", bib_auth)[0]
        family = first.split(",")[0].strip().strip("{}")
        if family and not any(norm(family) in norm(a) for a in reg["authors"]):
            problems.append(f"first author {family!r} not among registry "
                            f"authors {reg['authors'][:6]}")

    year = (entry.get("year") or "").strip()
    if year and reg["year"] and year != reg["year"]:
        problems.append(f"year bib={year} reg={reg['year']}")

    container = entry.get("journal") or entry.get("booktitle") or ""
    if container and reg["containers"]:
        # A proceedings paper's container-title carries both the book series
        # and the volume's own title; matching either one is a match.
        score = max(difflib.SequenceMatcher(
            None, norm(container.replace("\\&", "&")), norm(c)).ratio()
            for c in reg["containers"])
        if score < JOURNAL_FLOOR:
            problems.append(f"journal {score:.2f}: bib={container!r} "
                            f"reg={reg['containers']!r}")

    volume = (entry.get("volume") or "").strip()
    if volume and reg["volume"] and volume != reg["volume"]:
        problems.append(f"volume bib={volume} reg={reg['volume']}")

    pages = (entry.get("pages") or "").replace("--", "-").strip()
    if pages and reg["pages"] and pages.replace(" ", "") != reg["pages"].replace(" ", ""):
        problems.append(f"pages bib={pages} reg={reg['pages']}")

    if problems and (entry.get("note") or "").strip():
        # An entry whose note explains the divergence has already been looked
        # at by hand; report it, but not as an unexamined mismatch.
        return "DOCUMENTED", problems + [f"note: {entry['note']}"], reg
    return ("OK" if not problems else "MISMATCH"), problems, reg


def main(argv):
    bib = entries()
    keys = ([k.strip() for k in open(argv[1]) if k.strip()]
            if len(argv) > 1 else sorted(bib))
    results, counts = {}, {}
    for key in keys:
        if key not in bib:
            print(f"{key}: NOT IN BIB")
            continue
        status, problems, reg = check(bib[key])
        results[key] = dict(status=status, problems=problems, meta=reg)
        counts[status] = counts.get(status, 0) + 1
        print(f"{status:10s} {key}"
              + ("" if not problems else "\n    - " + "\n    - ".join(problems)),
              flush=True)
        time.sleep(0.3)
    print("\n" + "  ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    if len(argv) > 2:
        json.dump(results, open(argv[2], "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv)
