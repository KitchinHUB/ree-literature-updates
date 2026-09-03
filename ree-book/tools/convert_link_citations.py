"""Convert inline Markdown hyperlink citations to MyST `[@key]` citations.

The fourth and last of the inherited citation styles.  Several source
documents cited by hyperlink -- `([Nature Communications](https://...))` --
rather than by key, so the reference is a URL and nothing else.  A URL is a
worse citation than a key: it carries no author, no year, and no title, it
rots, and it cannot be checked against the bibliography.  This resolves each
URL to a DOI (`tools/link_dois.py`), looks the DOI up in `references.bib`, and
rewrites the link as a citation.

Roughly a quarter of the links are vendor pages, national-lab press releases,
and news articles that have no DOI because they are not papers.  Those are
left as hyperlinks on purpose: they are the honest form for that kind of
source, and turning them into citations would imply a peer-reviewed record
that does not exist.

Three URLs point at a paper that has nothing to do with the sentence citing
them -- the same failure mode as the wrong DOIs found in the numeric audit,
arriving through a different channel.  They are corrected in `MANUAL_URL`
below, with the replacement chosen by searching CrossRef for a paper that
actually supports the claim.

Usage:
    python tools/convert_link_citations.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from link_dois import doi_for  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# Files whose links are not citations.  Appendix B lists DOIs as DOIs on
# purpose -- it is a reading list, not prose making claims -- and the
# provenance appendix links to the source repository.
SKIP = {"93-appendix-provenance.md", "94-appendix-further-reading.md"}

# URL -> DOI.  Each of these URLs resolves to a real paper on an unrelated
# subject; the replacement was verified to support the sentence that cites it.
MANUAL_URL = {
    # Cited for magnetic adsorbents for REE recovery; the URL is a paper on
    # chitosan nanoparticles for drug delivery.
    "https://www.frontiersin.org/articles/10.3389/fbioe.2020.00004/full":
        "10.1016/j.seppur.2022.121708",
    # Cited for polymer inclusion beads recovering REEs from end-of-life
    # magnets; the URL is a paper on liquid-desiccant membrane distillation.
    "https://www.sciencedirect.com/science/article/pii/S1383586623024450":
        "10.1016/j.mineng.2024.108779",
    # Cited for ion-imprinted polymers; the URL is a paper on organoarsenic
    # adsorption by a zirconium MOF.
    "https://www.sciencedirect.com/science/article/abs/pii/S1385894719315906":
        "10.1016/j.seppur.2025.134593",

    # Repository, aggregator, and publisher-platform URLs that host a real
    # paper but expose no DOI.  Each was matched to its published record by
    # CrossRef title search.
    "https://www.researchgate.net/publication/244611960_Two-Phase_Calorimetry_I"
    "_Studies_on_the_Thermodynamics_of_Lanthanide_Extraction_by_Bis2-EthylHexyl"
    "_Phosphoric_Acid": "10.1080/07366290802301374",
    # The link regex stops at the "(" inside the escaped filename, so the URL
    # is keyed here in the truncated form the converter actually sees.
    "https://centaur.reading.ac.uk/86832/1/MS-Thermodynamic_parameters_revised"
    "_v190915_all%20(1": "10.1016/j.jct.2019.105955",
    "https://academic.oup.com/chromsci/article/55/4/465/2712537":
        "10.1093/chromsci/bmw200",
    "https://scielo.org.za/scielo.php?script=sci_arttext&pid="
    "S2225-62532022000700011": "10.17159/2411-9717/1989/2022",
}

LINK = re.compile(r"\[([^]\[]*)\]\((https?://[^)\s]+)\)")
# A parenthesised group of one or more links, separated by commas: the form
# nearly every one of these citations takes.
GROUP = re.compile(
    r"\((\[[^]\[]*\]\(https?://[^)\s]+\)"
    r"(?:\s*,\s*\[[^]\[]*\]\(https?://[^)\s]+\))*)\)"
)


def bib_keys_by_doi(path: pathlib.Path) -> dict[str, str]:
    keys: dict[str, str] = {}
    key = None
    for line in path.read_text().splitlines():
        m = re.match(r"@\w+\{([^,]+),", line)
        if m:
            key = m.group(1)
            continue
        m = re.match(r"\s*doi\s*=\s*[{\"]([^}\"]+)", line)
        if m and key:
            keys[m.group(1).strip().lower()] = key
    return keys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cache_path = ROOT / ".link-dois.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    by_doi = bib_keys_by_doi(ROOT / "references.bib")

    missing: list[tuple[str, str, str]] = []
    stats = {"cited": 0, "kept": 0}

    def key_for(url: str) -> str | None:
        doi = MANUAL_URL.get(url) or doi_for(url, cache)
        if not doi:
            return None
        key = by_doi.get(doi.lower())
        if not key:
            missing.append((fname, url, doi))
        return key

    for path in sorted(SRC.glob("*.md")):
        if path.name in SKIP:
            continue
        fname = path.name
        text = original = path.read_text()

        def repl_group(m: re.Match) -> str:
            links = LINK.findall(m.group(1))
            resolved = [(label, url, key_for(url)) for label, url in links]
            if all(k for _, _, k in resolved):
                stats["cited"] += len(resolved)
                return "[" + "; ".join("@" + k for _, _, k in resolved) + "]"
            # A mixed group: cite what can be cited, leave the rest a link.
            parts = []
            for label, url, key in resolved:
                if key:
                    stats["cited"] += 1
                    parts.append(f"[@{key}]")
                else:
                    parts.append(f"[{label}]({url})")
            return "(" + ", ".join(parts) + ")"

        text = GROUP.sub(repl_group, text)

        # Links outside a parenthesised group -- "**Reference:** [X](url)".
        def repl_bare(m: re.Match) -> str:
            key = key_for(m.group(2))
            if not key:
                return m.group(0)
            stats["cited"] += 1
            return f"[@{key}]"

        text = LINK.sub(repl_bare, text)
        stats["kept"] += len(LINK.findall(text))

        if text != original and not args.dry_run:
            path.write_text(text)

    if missing:
        print("DOI resolved but not in references.bib:", file=sys.stderr)
        for fname, url, doi in missing:
            print(f"  {fname}  {doi}  {url}", file=sys.stderr)
        return 1

    cache_path.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
    print(f"cited {stats['cited']} links, kept {stats['kept']} as hyperlinks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
