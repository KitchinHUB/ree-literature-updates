"""Report which cited sources still have no full text in `fulltexts/`.

The book's rule is that a citation which resolves is not thereby correct: the
cited work has to contain the claim, which means someone has to read it. Reading
needs the PDF, and the PDFs are collected by hand because publishers block
automated retrieval. This works out what is still missing and writes
`fulltexts-wanted.md` -- the DOIs, batched fifty at a time, in the order worth
collecting them.

Deciding what is already on hand is the awkward part, because `fulltexts/` has
accumulated files three ways:

1. Named for their citation key, `ding2023separation.pdf`, which is the
   convention and needs no lookup.
2. Named by the publisher -- `1-s2.0-S0304386X23000294-main.pdf`,
   `s41893-022-00989-3.pdf`. These are identified by pulling the DOIs printed on
   the first two pages and matching against the bibliography. Roughly four in
   five give themselves up this way.
3. Named by the publisher AND printing no DOI on the front matter, usually
   because the paper predates the practice. There is no general fix; the ten
   in this category were identified by reading their title pages and are listed
   in OVERRIDE below.

The DOI scan is the slow step, so its results are cached in `fulltexts/` beside
the PDFs (a gitignored directory) and keyed by path, size and mtime.

Two things this deliberately does not do. It does not treat an uncited entry as
wanted -- `references.bib` covers more ground than the book does, and nothing
rests on the remainder; `orphan-references.md` lists those. And it does not
claim a collected PDF has been read: `fulltexts/1-50/`, `fulltexts/u-p/` and
tiers 2 and 3 have been read against the book, the rest are merely on disk.

Usage:
    python tools/fulltext_inventory.py [--check]

`--check` reports the counts and writes nothing, for use in a build.
"""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BIB = ROOT / "references.bib"
CITED_BIB = ROOT / "src" / "references-cited.bib"
FULLTEXTS = ROOT / "fulltexts"
CACHE = FULLTEXTS / ".doi-cache.json"
OUT = ROOT / "fulltexts-wanted.md"
BATCH = 50

# PDFs whose filename is not a citation key and which print no DOI on their
# front matter. Each was identified by reading its title page against the
# bibliography entry. Add to this only after doing the same.
OVERRIDE = {
    "51-100/1-s2.0-S0009250999001190-main.pdf": "wichterlova1999dynamic",
    "51-100/1-s2.0-S0021967301824043-main.pdf": "james1968displacement",
    "51-100/1-s2.0-S1002072112602816-main.pdf": "liao2013clean",
    "51-100/Lyon_idaho_0089N_10815.pdf": "lyon2016separation",
    "51-100/Rare_earth_separation_in_China.pdf": "yan2006rare",
    "51-100/ja01203a063.pdf": "spedding1947separation",
    "51-100/s11663-002-0018-1.pdf": "huang2002rare",
    "tier-4/1-s2.0-S0009250999000147-main.pdf": "geist1999kinetics",
    "tier-4/1-s2.0-S037673889900040X-main.pdf": "gabelman1999hollow",
    "tier-4/ic00284a028.pdf": "cossy1988oxygen",
}

# Sources carrying a claim `needs-journal-access.md` records as unverified, or
# that a chapter says outright it cannot source. Reading these changes the text,
# so they sort to the front regardless of how often they are cited.
FLAGGED = {
    "an2024agile", "augustine2026coupling", "bao2025mxene", "cossy1988oxygen",
    "deng2025application", "duchanois2023prospects", "elmaangar2020microfluidic",
    "gabelman1999hollow", "geist1999kinetics", "he2016kinetics",
    "he2024intensifying", "leite2025creation", "liu2026machine",
    "nichols2011mechanistic", "tian2010kinetics", "tian2020rare",
    "yang2022pilot", "yu2026progress", "zhang2026predicting",
}

BACK_MATTER = {"90", "91", "92", "93", "94"}


# --- bibliography ----------------------------------------------------

def _field(body, name):
    """Read one brace-delimited field, counting nested braces."""
    m = re.search(r"\n\s*%s\s*=\s*\{" % name, body)
    if not m:
        return None
    i, depth, out = m.end(), 1, []
    while i < len(body) and depth:
        c = body[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                break
        out.append(c)
        i += 1
    return re.sub(r"\s+", " ", "".join(out)).strip()


def parse_bib(path):
    s = path.read_text(encoding="utf-8")
    entries = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),", s):
        key, start = m.group(2).strip(), m.end()
        nxt = s.find("\n@", start)
        body = s[start:nxt if nxt != -1 else len(s)]
        entries[key] = {
            "doi": (_field(body, "doi") or "").strip(),
            "title": (_field(body, "title") or "").replace("{", "").replace("}", ""),
            "year": _field(body, "year") or "",
            "author": (_field(body, "author") or "").replace("{", "").replace("}", ""),
            "url": _field(body, "url") or "",
            "venue": (_field(body, "journal") or _field(body, "booktitle")
                      or _field(body, "publisher") or _field(body, "institution")
                      or _field(body, "school") or ""),
        }
    return entries


# --- what is on disk -------------------------------------------------

def dois_in(path, cache):
    """DOIs printed on a PDF's first two pages, cached by path/size/mtime."""
    st = path.stat()
    stamp = [st.st_size, int(st.st_mtime)]
    rel = str(path.relative_to(FULLTEXTS))
    hit = cache.get(rel)
    if hit and hit[:2] == stamp:
        return hit[2]
    try:
        txt = subprocess.run(["pdftotext", "-f", "1", "-l", "2", str(path), "-"],
                             capture_output=True, text=True, timeout=120).stdout
    except (OSError, subprocess.SubprocessError):
        txt = ""
    found = [d.rstrip(".").rstrip(")").rstrip("/").lower()
             for d in re.findall(r"\b10\.\d{4,9}/[^\s\"<>,;)\]]+", txt)][:8]
    cache[rel] = stamp + [found]
    return found


def collected(bib):
    """key -> the PDF that holds it, for everything identifiable in fulltexts/."""
    cache = {}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except ValueError:
            cache = {}
    doi2key = {}
    for k, v in bib.items():
        if v["doi"]:
            doi2key.setdefault(v["doi"].lower(), k)

    have, unknown = {}, []
    for path in sorted(FULLTEXTS.rglob("*.pdf")):
        rel = str(path.relative_to(FULLTEXTS))
        if path.stem in bib:
            have.setdefault(path.stem, rel)
            continue
        if rel in OVERRIDE:
            have.setdefault(OVERRIDE[rel], rel)
            continue
        for doi in dois_in(path, cache):
            if doi in doi2key:
                have.setdefault(doi2key[doi], rel)
                break
        else:
            unknown.append(rel)

    CACHE.write_text(json.dumps(cache, indent=1))
    return have, unknown


# --- citation counts -------------------------------------------------

def citation_counts(bib):
    counts = collections.Counter()
    where = collections.defaultdict(set)
    pat = re.compile(r"@([A-Za-z][A-Za-z0-9]*\d{4}[a-z]*)")
    for md in sorted((ROOT / "src").glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in pat.finditer(text):
            key = m.group(1)
            if key in bib:
                counts[key] += 1
                where[key].add(md.name)
    return counts, where


# --- the report ------------------------------------------------------

def chapters(where, key):
    nums = sorted({m.group(1) for f in where[key]
                   if (m := re.match(r"(\d+)", f)) and m.group(1) not in BACK_MATTER})
    return ",".join(n.lstrip("0") or "0" for n in nums)


def shorten(text, n):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[:n - 1].rstrip() + "…"


def source_cell(bib, key):
    e = bib[key]
    first = e["author"].split(" and ")[0].split(",")[0].strip()
    flag = "⚑ " if key in FLAGGED else ""
    who = "%s %s — " % (first, e["year"]) if first else "%s — " % e["year"]
    cell = "%s%s*%s*" % (flag, who, shorten(e["title"], 68))
    return cell.replace("|", "\\|")


def render(bib, cited, have, counts, where):
    missing = sorted(k for k in cited if k not in have)
    missing.sort(key=lambda k: (k not in FLAGGED, -counts[k], k))
    with_doi = [k for k in missing if bib[k]["doi"]]
    no_doi = [k for k in missing if not bib[k]["doi"]]
    lines = []
    add = lines.append

    add("# Full texts still to collect")
    add("")
    add("Generated %s by `tools/fulltext_inventory.py`. Regenerate it rather than"
        % datetime.date.today().isoformat())
    add("editing it by hand — it is a report, not a record.")
    add("")
    add("## What this is")
    add("")
    add("The book's rule is that a citation which resolves is not thereby correct:")
    add("the cited work has to actually contain the claim, and checking that means")
    add("reading it. This is the list of cited sources with no PDF in `fulltexts/`,")
    add("batched fifty at a time so they can be collected in sittings.")
    add("")
    add("| | |")
    add("|---|---:|")
    add("| Entries the book cites | %d |" % len(cited))
    add("| Full text on hand | %d |" % len(have))
    add("| **Still wanted** | **%d** |" % len(missing))
    add("| — with a DOI to fetch | %d |" % len(with_doi))
    add("| — no DOI; see the last section | %d |" % len(no_doi))
    add("")
    add("The %d uncited entries in `references.bib` are out of scope — nothing in"
        % (len(bib) - len(cited)))
    add("the book rests on them. `orphan-references.md` lists those.")
    add("")
    add("## How to use it")
    add("")
    add("Work a batch at a time, in order. **Save each PDF as `<key>.pdf`**, the key")
    add("in the second column exactly as written, anywhere under `fulltexts/`. That")
    add("name is what lets a verification pass find the paper without a lookup table,")
    add("and it is what the next run of this report reads to decide the source is no")
    add("longer wanted.")
    add("")
    add("Every batch ends with a plain block of DOI links and no markup, for pasting")
    add("into a downloader in one go.")
    add("")
    add("## How the batches are ordered")
    add("")
    add("1. **⚑ first.** Sources carrying a claim that `needs-journal-access.md`")
    add("   records as unverified, or that a chapter states outright it cannot")
    add("   source. Reading one of these changes the text.")
    add("2. **Then by how often the book cites the source**, most first. A source the")
    add("   book leans on in twenty places is worth more than one cited once.")
    add("3. Then alphabetically, so the order is stable between runs.")
    add("")
    add("Batch 1 is therefore the highest-value fifty and the last batches are the")
    add("long tail of single citations. If the effort stops partway, it stops in the")
    add("right place.")
    add("")
    add("**Cites** is how many times the book cites the source; **Ch** is which")
    add("chapters do.")
    add("")

    total = (len(with_doi) + BATCH - 1) // BATCH
    for b in range(total):
        chunk = with_doi[b * BATCH:(b + 1) * BATCH]
        add("## Batch %d of %d" % (b + 1, total))
        add("")
        add("| # | Key | Cites | Ch | Source | DOI |")
        add("|---:|---|---:|---|---|---|")
        for i, key in enumerate(chunk, 1 + b * BATCH):
            doi = bib[key]["doi"]
            add("| %d | `%s` | %d | %s | %s | [%s](https://doi.org/%s) |"
                % (i, key, counts[key], chapters(where, key) or "—",
                   source_cell(bib, key), doi, doi))
        add("")
        add("```text")
        for key in chunk:
            add("https://doi.org/%s" % bib[key]["doi"])
        add("```")
        add("")

    add("## Cited, but with no DOI to fetch")
    add("")
    add("These %d cannot be collected by DOI. Most are standards, agency reports,"
        % len(no_doi))
    add("theses or software documentation; the rest are old enough that no DOI was")
    add("ever registered. A recorded URL is given where there is one.")
    add("")
    add("| Key | Cites | Ch | Source | Where |")
    add("|---|---:|---|---|---|")
    for key in no_doi:
        url = bib[key]["url"]
        loc = "[link](%s)" % url if url else (shorten(bib[key]["venue"], 40) or "—")
        add("| `%s` | %d | %s | %s | %s |"
            % (key, counts[key], chapters(where, key) or "—",
               source_cell(bib, key), loc))
    add("")
    add("## What \"on hand\" means here")
    add("")
    add("A source counts as collected when a PDF under `fulltexts/` maps to its key:")
    add("the file is named `<key>.pdf`, or a DOI printed on its first two pages")
    add("matches the entry, or it is one of the ten in the generator's override")
    add("table. Files that satisfy none of the three are invisible to this report and")
    add("will be asked for again — which is the argument for naming them after the")
    add("key when they land.")
    add("")
    add("Collected does **not** mean read. `fulltexts/1-50/`, `fulltexts/u-p/` and")
    add("tiers 2 and 3 have been read against the book and their corrections are in")
    add("the git history. The rest are on disk and still owed a reading.")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="report the counts and write nothing")
    args = ap.parse_args()

    bib = parse_bib(BIB)
    cited = set(parse_bib(CITED_BIB))
    have, unknown = collected(bib)
    counts, where = citation_counts(bib)
    missing = [k for k in cited if k not in have]

    print("cited %d   on hand %d   wanted %d" % (len(cited), len(have), len(missing)))
    if unknown:
        print("%d PDFs in fulltexts/ could not be identified:" % len(unknown))
        for rel in unknown:
            print("   ", rel)
    if args.check:
        return 0
    OUT.write_text(render(bib, cited, have, counts, where), encoding="utf-8")
    print("wrote %s" % OUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
