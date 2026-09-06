#!/usr/bin/env python3
"""Add a Google Scholar link to every citation tooltip in the built site.

MyST renders a citation's hover card (`div.hover-document`) and the per-chapter
References list (`li.myst-bibliography-item`) from the SAME string: the `html`
field of `references.cite.data[<key>]` in the page payload. Appending an anchor
to that string therefore puts the link in both places at once, with no DOM
scraping and no dependency on the theme's minified class names.

Google Scholar has no URL that opens the related-articles list for a DOI --
that page is keyed on Scholar's own cluster id, which is not derivable from a
DOI and can only be had by scraping Scholar. `scholar_lookup?doi=` is the
documented endpoint publishers use; it lands on the paper's Scholar record,
where "Related articles" and "Cited by" are one click away. That is the closest
thing that exists.

The payload lives in two places and both must be patched, because the first
render hydrates from the HTML and later client-side navigations fetch the JSON:

  * `_build/html/*.json`      -- one per page, fetched on navigation. Patched by
                                 a JSON round-trip.
  * `_build/html/**/index.html` -- the payload embedded in `window.__remixContext`.
                                 Patched by string replacement, using React's
                                 serialisation: JSON.stringify (which does not
                                 escape non-ASCII) followed by escaping < > &
                                 to \\u003c \\u003e \\u0026. That model was
                                 checked against the built site and reproduces
                                 all 47 citation strings on the microfluidics
                                 page exactly.

Run after `mystmd build --html`. Idempotent: a second run injects nothing.
"""

import json
import pathlib
import sys
from urllib.parse import quote

HTML = pathlib.Path("_build/html")
LOOKUP = "https://scholar.google.com/scholar_lookup?doi="
MARKER = "scholar_lookup?doi="


def anchor(doi):
    return (
        ' · <a class="scholar-link" target="_blank" rel="noreferrer"'
        ' title="Find this paper on Google Scholar, and its related articles"'
        f' href="{LOOKUP}{quote(doi, safe="")}">Google Scholar</a>'
    )


def cite_data(node):
    """The references.cite.data dict of a page payload, or None."""
    if isinstance(node, dict):
        cite = node.get("cite")
        if isinstance(cite, dict) and isinstance(cite.get("data"), dict):
            return cite["data"]
        for value in node.values():
            found = cite_data(value)
            if found is not None:
                return found
    return None


def embedded(text):
    """Escape a string the way React embeds it in the SSR payload."""
    return (
        json.dumps(text, ensure_ascii=False)[1:-1]
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def main():
    if not HTML.is_dir():
        sys.exit("no _build/html; run `npx mystmd build --html` first")

    # key -> (old html, new html), collected from the JSON payloads and reused
    # to patch the HTML, so the two copies cannot drift apart.
    rewrites = {}
    patched_json = nodoi = 0

    for path in sorted(HTML.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        data = cite_data(payload)
        if not data:
            continue
        touched = False
        for key, entry in data.items():
            html = entry.get("html")
            doi = entry.get("doi")
            if not html or MARKER in html:
                continue
            if not doi:
                nodoi += 1
                continue
            rewrites[key] = (html, html + anchor(doi))
            entry["html"] = rewrites[key][1]
            touched = True
        if touched:
            # Compact separators, matching what MyST wrote: these files are
            # fetched on every client-side navigation.
            path.write_text(
                json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )
            patched_json += 1

    patched_html = 0
    for path in sorted(HTML.rglob("index.html")):
        text = path.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        out = text
        for old, new in rewrites.values():
            token = embedded(old)
            if token in out:
                out = out.replace(token, embedded(new))
        if out != text:
            path.write_text(out, encoding="utf-8")
            patched_html += 1

    print(
        f"scholar links: {len(rewrites)} references, "
        f"{patched_json} json + {patched_html} html pages"
        + (f", {nodoi} skipped (no DOI)" if nodoi else "")
    )


if __name__ == "__main__":
    main()
