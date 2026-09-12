#!/usr/bin/env python3
"""Inject the faceted-search widget and its index into the built site.

Same shape, and the same reason, as `inject_chat.py`: MyST offers no hook for
custom JavaScript, so the assets are added after `mystmd build --html`. Run
after `tools/build_facets.py`.

The widget belongs to one page but the script goes on all of them, exactly as
`inject_chat.py` does, because MyST v2 is a Remix SPA: a reader who reaches
Explore from the sidebar never loads Explore's own HTML, so a script injected
only there never runs and they get the no-JavaScript fallback. The script is
inert on every other page -- it looks for `#ree-search`, finds nothing, and
never fetches the index. Explore is still located by its `REE-SEARCH-APP`
sentinel, as a build-time check that the page is in the TOC at all: `folders:
true` puts it at a path that depends on the TOC, so a hard-coded one would fail
silently the first time the TOC moved.

The tags go before </body>, and that placement is load-bearing. In <head> the
script tag is still *present* after hydration but never runs: React reconciles
<head> and the node it puts back is a fresh element, and a script element
inserted that way does not execute. Before </body> the script executes during
parsing, before hydration starts, so it does not matter that Remix later sweeps
the node away.

Honours BASE_URL exactly as the MyST build does. Idempotent.
"""

import json
import os
import pathlib
import shutil
import sys

HTML = pathlib.Path("_build/html")
SRC = pathlib.Path("static/search")
MARKER = "<!-- reesearch -->"
SENTINEL = "REE-SEARCH-APP"

BASE = os.environ.get("BASE_URL", "").rstrip("/")


def main():
    if not HTML.is_dir():
        sys.exit("no _build/html; run `npx mystmd build --html` first")

    index = SRC / "facets.json"
    if not index.exists():
        sys.exit(f"no {index}; run tools/build_facets.py first")

    dest = HTML / "search"
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("search.js", "search.css", "facets.json"):
        shutil.copy2(SRC / name, dest / name)

    # No <link> for the stylesheet: injected here it is fetched and then
    # dropped by the same <body> reconciliation, and the widget renders
    # unstyled. search.js adds the link to <head> itself after hydration,
    # where React is no longer reconciling.
    snippet = (
        f'{MARKER}'
        f'<script>window.__REE_SEARCH_BASE__={BASE!r};</script>'
        f'<script defer src="{BASE}/search/search.js"></script>'
    ).replace("'", '"')

    pages = sorted(HTML.rglob("index.html"))
    if not any(SENTINEL in p.read_text(encoding="utf-8") for p in pages):
        sys.exit(f"no built page contains {SENTINEL}; is src/95-explore.md in the TOC?")

    injected = skipped = 0
    for p in pages:
        html = p.read_text(encoding="utf-8")
        if MARKER in html:
            skipped += 1
            continue
        if "</body>" not in html:
            print(f"  ! no </body> in {p.relative_to(HTML)}, skipped")
            skipped += 1
            continue
        p.write_text(html.replace("</body>", snippet + "</body>", 1), encoding="utf-8")
        injected += 1

    payload = json.loads(index.read_text())
    size = index.stat().st_size / 1024
    print(f"injected into {injected} page(s), {skipped} already had it")
    print(f"index {size:.0f} KB, {len(payload['records'])} records, base URL {BASE or '/'}")


if __name__ == "__main__":
    main()
