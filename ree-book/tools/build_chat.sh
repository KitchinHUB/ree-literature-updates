#!/usr/bin/env bash
# Build the ask-the-book retrieval index and inject the widget into the site.
# Run after `npx mystmd build --html`. Set BASE_URL when the site is served
# from a subpath, exactly as the MyST build requires.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build_chunks.py
node tools/embed_chunks.mjs
python3 tools/inject_chat.py
