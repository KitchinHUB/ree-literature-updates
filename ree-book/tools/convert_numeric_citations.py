"""Convert the numbered citations in `src/` to MyST citations.

Two chapters came from documents that cite by number against a hand-typed
reference list -- `[7]`, `[11,12]`, `[5-7]` -- with no key anywhere.  The list
at the end of each source document is the only thing tying a number to a paper,
so this parses that list, resolves each entry to a `references.bib` key by DOI
(falling back to URL, then to title similarity), and rewrites the numbers.

Each chapter is declared against exactly one source list.  That is checked, not
assumed: a chapter merged from two differently-numbered documents would silently
mis-cite, so the tool refuses to run unless every number in the chapter falls
within its declared list.

Usage:
    python tools/convert_numeric_citations.py [--dry-run]
"""

from __future__ import annotations

import argparse
import difflib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merge_bib import norm_doi, norm_title  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# chapter -> source document whose reference numbering it uses.
CHAPTERS = {
    "07-pyrometallurgical-halogenation.md": "carbochlorination-report.md",
    "09-microfluidic-separations.md": "microfluidic-report.md",
}

# Numbers whose printed reference cannot be trusted to resolve itself.
#
# Both source documents carry entries with a DOI that resolves to an unrelated
# paper, and a few whose author, year and journal describe a paper that does not
# exist.  Auditing every number against CrossRef (see `numeric-citation-audit.md`)
# split them three ways, and all three end up here because the automatic
# resolution below would either fail or, worse, silently follow a wrong DOI.
#
#   * the DOI is one digit off the real one, or the reference misattributes a
#     real paper -- mapped to the paper CrossRef returns for its title;
#   * the reference does not describe any paper that exists -- mapped to a
#     verified source that does support the claim, noted below;
#   * the reference is grey literature whose URL the parser truncates.
MANUAL: dict[tuple[str, int], str] = {
    # DOI wrong by a character, or author/year misremembered; title verified.
    ("07-pyrometallurgical-halogenation.md", 18): "anderson2015investigation",
    ("07-pyrometallurgical-halogenation.md", 29): "gorman2018sustainable",
    ("07-pyrometallurgical-halogenation.md", 49): "banda2015separation",
    ("07-pyrometallurgical-halogenation.md", 82): "gupta1984extractive",
    ("09-microfluidic-separations.md", 32): "dessimoz2010quantitative",
    ("09-microfluidic-separations.md", 49): "yadav2018ndfeb",
    # No such paper.  Re-sourced to work that does support the sentence.
    ("07-pyrometallurgical-halogenation.md", 9): "gavira2010carbochlorination",
    ("07-pyrometallurgical-halogenation.md", 15): "xue2025carbochlorination",
    ("07-pyrometallurgical-halogenation.md", 23): "anderson2015investigation",
    ("07-pyrometallurgical-halogenation.md", 43): "deng2022rare",
    ("07-pyrometallurgical-halogenation.md", 69): "chen2025process",
    # Grey literature: the URL in the reference line is truncated by the parser
    # at a bracket, or the citation points at the wrong document entirely.
    ("07-pyrometallurgical-halogenation.md", 37): "tsamis2015recovery",
    ("07-pyrometallurgical-halogenation.md", 59): "usgs2020titanium",
    ("07-pyrometallurgical-halogenation.md", 74): "wikipedia2024aluminium",
}

# Below this, a reference resolved by its DOI or URL disagrees with the title of
# the entry it landed on -- the signature of a DOI that belongs to another paper.
TITLE_AGREEMENT_THRESHOLD = 0.85

# Resolutions that disagree on title but are right: references that name a
# database, a company, or a series rather than the document they point at.
TITLE_AGREEMENT_OK = {
    ("07-pyrometallurgical-halogenation.md", 17),   # "thermodynamic data" -> HSC
    ("07-pyrometallurgical-halogenation.md", 54),   # "technical reports" -> the project
    ("07-pyrometallurgical-halogenation.md", 64),   # "commodity summary" -> the yearbook
    ("09-microfluidic-separations.md", 37),         # title paraphrased
}

NUMERIC = re.compile(r"\[(\d+(?:\s*[,-]\s*\d+)*)\]")
# "**[7]** Anderson, C. ..." and "7.  Xie, Y. et al. ..."
REF_LINE = re.compile(r"^(?:\*\*\[(\d+)\]\*\*|(\d+)\.)\s+(.*)$")
DOI_IN_TEXT = re.compile(r"10\.\d{4,9}/[^\s\]\)>\"'}]+")
TITLE_MATCH_THRESHOLD = 0.90


def parse_reference_list(path: pathlib.Path) -> dict[int, dict]:
    """Number -> {text, doi, urls} for the reference list at the end of a doc."""
    lines = path.read_text().splitlines()
    start = max(
        (i for i, l in enumerate(lines) if re.match(r"^#+\s*(\d+\.\s*)?References\s*$", l)),
        default=None,
    )
    if start is None:
        sys.exit(f"no reference list found in {path}")
    refs: dict[int, dict] = {}
    for line in lines[start + 1:]:
        m = REF_LINE.match(line.strip())
        if not m:
            continue
        num = int(m.group(1) or m.group(2))
        text = m.group(3)
        doi = DOI_IN_TEXT.search(text)
        refs[num] = {
            "text": text,
            "doi": norm_doi(doi.group(0).rstrip(".")) if doi else "",
            "urls": re.findall(r"https?://[^\s\]\)>\"']+", text),
        }
    return refs


def bib_index(path: pathlib.Path):
    """Index references.bib by DOI, by url, and by normalized title."""
    text = path.read_text()
    by_doi, by_url, by_title = {}, {}, {}
    for block in re.findall(r"@\w+\{([^,]+),(.*?)\n\}", text, re.S):
        key, body = block
        fields = dict(re.findall(r"^\s*(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", body, re.S | re.M))
        doi = norm_doi(fields.get("doi", ""))
        if doi:
            by_doi.setdefault(doi, key)
        url = (fields.get("url") or "").strip().lower().rstrip("/")
        if url:
            by_url.setdefault(url, key)
        title = norm_title(fields.get("title", ""))
        if title:
            by_title.setdefault(title, key)
    return by_doi, by_url, by_title


def bib_titles(path: pathlib.Path) -> dict[str, str]:
    """Key -> title, for checking that a DOI landed on the paper it names."""
    text = path.read_text()
    titles = {}
    for key, body in re.findall(r"@\w+\{([^,]+),(.*?)\n\}", text, re.S):
        fields = dict(re.findall(r"^\s*(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", body, re.S | re.M))
        titles[key] = fields.get("title", "")
    return titles


def reference_title(text: str) -> str:
    """Best guess at the title inside a hand-typed reference string.

    Two styles occur: APA-ish ("Balaram, V. (2019). Title. Journal...") and a
    quoted style that pandoc left escaped ('Xie, Y. et al. \\"Title.\\" *Journal*').
    """
    t = re.sub(r"\[\[?[^\]]*\]\]?\([^)]*\)", " ", text)      # markdown links
    t = re.sub(r"<https?://[^>]*>", " ", t)
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"\{\.underline\}", " ", t)
    quoted = re.search(r'\\?["\u201c](.+?)\\?["\u201d]', t)
    if quoted:
        return quoted.group(1).strip(' ."*')
    # Drop a leading author-and-year block: "Balaram, V. (2019). "
    t = re.sub(r"^.*?\(\d{4}[a-z]?\)\.\s*", "", t, count=1)
    return t.split(". ")[0].strip(' ."*')


def resolve(ref: dict, idx, where: tuple[str, int] | None = None) -> tuple[str | None, str]:
    by_doi, by_url, by_title = idx
    if where in MANUAL:
        return MANUAL[where], "manual"
    if ref["doi"] and ref["doi"] in by_doi:
        return by_doi[ref["doi"]], "DOI"
    for u in ref["urls"]:
        key = by_url.get(u.strip().lower().rstrip("/"))
        if key:
            return key, "URL"
    title = norm_title(reference_title(ref["text"]))
    best, score = None, 0.0
    for cand, key in by_title.items():
        s = difflib.SequenceMatcher(None, title, cand).ratio()
        if s > score:
            best, score = key, s
    if best and score >= TITLE_MATCH_THRESHOLD:
        return best, f"title {score:.2f}"
    return None, f"best title {score:.2f}"


def expand(spec: str) -> list[int]:
    """'11,12' -> [11, 12]; '5-7' -> [5, 6, 7]."""
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = (int(x) for x in part.split("-", 1))
            out.extend(range(lo, hi + 1))
        else:
            out.append(int(part))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    idx = bib_index(ROOT / "references.bib")
    title_by_key = bib_titles(ROOT / "references.bib")
    unresolved: list[str] = []
    disagree: list[str] = []
    converted = 0

    for chapter, source in CHAPTERS.items():
        path = ROOT / "src" / chapter
        refs = parse_reference_list(ROOT / "converted" / source)
        text = path.read_text()

        cited = sorted({n for m in NUMERIC.finditer(text) for n in expand(m.group(1))})
        out_of_range = [n for n in cited if n not in refs]
        if out_of_range:
            sys.exit(
                f"{chapter} cites {out_of_range} which {source} does not number -- "
                "the chapter is not numbered against that list"
            )

        keys: dict[int, str] = {}
        for n in cited:
            key, how = resolve(refs[n], idx, (chapter, n))
            if key is None:
                unresolved.append(f"{chapter} [{n}] ({how}): {refs[n]['text'][:100]}")
                continue
            keys[n] = key
            if how in ("DOI", "URL") and (chapter, n) not in TITLE_AGREEMENT_OK:
                recorded = norm_title(reference_title(refs[n]["text"]))
                landed = norm_title(title_by_key.get(key, ""))
                agree = difflib.SequenceMatcher(None, recorded, landed).ratio()
                # A printed title cut off at its subtitle is a truncation, not a
                # different paper.
                prefix = recorded.startswith(landed) or landed.startswith(recorded)
                if agree < TITLE_AGREEMENT_THRESHOLD and not prefix:
                    disagree.append(
                        f"{chapter} [{n}] resolved by {how} to {key} but the titles "
                        f"agree only {agree:.2f}\n      printed: {recorded[:88]}"
                        f"\n      landed : {landed[:88]}"
                    )
        print(f"{chapter}: {len(cited)} numbers cited, {len(keys)} resolved")

        if unresolved or disagree:
            continue

        def sub(m: re.Match) -> str:
            nonlocal converted
            converted += 1
            return "[" + "; ".join(f"@{keys[n]}" for n in expand(m.group(1))) + "]"

        new = NUMERIC.sub(sub, text)
        if new != text and not args.dry_run:
            path.write_text(new)

    if disagree:
        print(
            "\ntitle disagreement -- these DOIs may belong to another paper:",
            file=sys.stderr,
        )
        for d in disagree:
            print("  " + d, file=sys.stderr)
        return 1

    if unresolved:
        print("\nunresolved -- add these to references.bib first:", file=sys.stderr)
        for u in unresolved:
            print("  " + u, file=sys.stderr)
        return 1

    print(f"{'would convert' if args.dry_run else 'converted'} {converted} numeric citations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
