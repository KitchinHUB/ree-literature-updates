#!/usr/bin/env python3
"""Inject the ask-the-book widget into the built site.

MyST has no hook for custom JavaScript, so the widget is added as a post-build
step, the same way the PDF is copied into the site. Run after
`mystmd build --html` and after tools/embed_chunks.mjs.

Honours BASE_URL exactly as the MyST build does, so the widget's asset and
deep-link paths resolve when the site is served from a repository subpath.
Idempotent: running it twice does not inject twice.
"""

import os
import pathlib
import shutil
import sys

HTML = pathlib.Path("_build/html")
SRC = pathlib.Path("static/chat")
MARKER = "<!-- bookchat -->"

BASE = os.environ.get("BASE_URL", "").rstrip("/")


def main():
    if not HTML.is_dir():
        sys.exit("no _build/html; run `npx mystmd build --html` first")

    index = HTML / "chat" / "index.json"
    if not index.exists():
        sys.exit("no _build/html/chat/index.json; run tools/embed_chunks.mjs first")

    dest = HTML / "chat"
    dest.mkdir(parents=True, exist_ok=True)
    for name in ("chat.js", "chat.css"):
        shutil.copy2(SRC / name, dest / name)

    snippet = (
        f'{MARKER}'
        f'<link rel="stylesheet" href="{BASE}/chat/chat.css">'
        f'<script>window.__BOOK_CHAT_BASE__={BASE!r};</script>'
        f'<script defer src="{BASE}/chat/chat.js"></script>'
    ).replace("'", '"')

    pages = sorted(HTML.rglob("index.html"))
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

    size = index.stat().st_size / 1024
    print(f"injected into {injected} pages ({skipped} skipped)")
    print(f"index {size:.0f} KB, base URL {BASE or '/'}")


if __name__ == "__main__":
    main()
