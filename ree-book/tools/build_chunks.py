#!/usr/bin/env python3
"""Chunk the built MyST AST into retrieval passages for the site chatbot.

Reads _build/site/content/*.json (produced by `mystmd build --html`) and emits
_build/chat/chunks.json: one record per passage, carrying the text, the chapter
and section it came from, and a deep link to the heading anchor.

Chunking is by heading, then split at paragraph boundaries so no passage runs
much past TARGET_WORDS. Every sub-chunk keeps its section's anchor, so a hit
always lands the reader on the right heading.
"""

import json
import pathlib
import re
import sys

CONTENT = pathlib.Path("_build/site/content")
OUT = pathlib.Path("_build/chat/chunks.json")

TARGET_WORDS = 220      # aim for passages around this length
MAX_WORDS = 380         # hard split above this
MIN_WORDS = 25          # drop passages shorter than this

# Nodes whose text we take whole, without recursing further.
LEAF_BLOCKS = {"paragraph", "table", "list", "code", "math", "blockquote",
               "definitionList", "admonition"}
# Nodes we never take text from.
SKIP = {"footnoteReference", "footnoteDefinition",
        "mystComment", "comment", "image", "container", "caption", "legend"}


def node_text(node):
    """Flatten a node to readable plain text."""
    out = []

    def rec(n):
        if isinstance(n, list):
            for v in n:
                rec(v)
            return
        if not isinstance(n, dict):
            return
        t = n.get("type")
        if t in SKIP:
            return
        if t == "text":
            out.append(n.get("value", ""))
            return
        if t in ("inlineMath", "math"):
            v = (n.get("value") or "").strip()
            if v:
                out.append(f"${v}$" if t == "inlineMath" else f" {v} ")
            return
        if t == "inlineCode" or t == "code":
            v = n.get("value") or ""
            if v:
                out.append(v)
            return
        if t == "crossReference":
            # Keep the visible link text, drop the machinery.
            rec(n.get("children"))
            return
        if t in ("cite", "citeGroup"):
            # Citations render as "Zhang et al. (2016)" and are worth keeping:
            # they carry author and year, and dropping them strands the
            # sentence that was built around them.
            rec(n.get("children"))
            return
        if t == "listItem":
            rec(n.get("children"))
            out.append("; ")
            return
        # Cell / row boundaries read better with a separator.
        if t in ("tableCell", "tableRow"):
            rec(n.get("children"))
            out.append(" | ")
            return
        rec(n.get("children"))

    rec(node)
    s = "".join(out)
    s = re.sub(r"\s*\|\s*\|\s*", " | ", s)
    s = re.sub(r"\s*;\s*;\s*", "; ", s)
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip(" ;|\n\t")


def heading_text(node):
    return re.sub(r"\s+", " ", node_text(node.get("children"))).strip()


def walk_blocks(node, emit):
    """Depth-first in document order; emit ('heading', n) or ('block', n)."""
    if isinstance(node, list):
        for v in node:
            walk_blocks(v, emit)
        return
    if not isinstance(node, dict):
        return
    t = node.get("type")
    if t == "heading":
        emit("heading", node)
        return
    if t in SKIP:
        return
    if t in LEAF_BLOCKS:
        emit("block", node)
        return
    walk_blocks(node.get("children"), emit)


def split_paragraphs(paras):
    """Group paragraph strings into chunks near TARGET_WORDS."""
    chunks, cur, n = [], [], 0
    for p in paras:
        w = len(p.split())
        if cur and (n + w > MAX_WORDS or n >= TARGET_WORDS):
            chunks.append("\n\n".join(cur))
            cur, n = [], 0
        cur.append(p)
        n += w
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def main():
    files = sorted(CONTENT.glob("*.json"))
    if not files:
        sys.exit("no built content found; run `npx mystmd build --html` first")

    records = []
    for f in files:
        doc = json.load(open(f))
        slug = doc.get("slug", "")
        title = (doc.get("frontmatter") or {}).get("title") or slug
        # slug 'src.solvent-extraction-fundamentals' -> '/src/solvent-...'
        url_path = "/" + slug.replace(".", "/") + "/"

        sections = []           # (heading_text, anchor, [paragraphs])
        current = (None, None, [])

        def emit(kind, node):
            nonlocal current
            if kind == "heading":
                if current[2]:
                    sections.append(current)
                current = (heading_text(node),
                           node.get("html_id") or node.get("identifier"),
                           [])
            else:
                txt = node_text(node)
                if txt:
                    current[2].append(txt)

        walk_blocks(doc.get("mdast"), emit)
        if current[2]:
            sections.append(current)

        for head, anchor, paras in sections:
            for body in split_paragraphs(paras):
                if len(body.split()) < MIN_WORDS:
                    continue
                records.append({
                    "page": title,
                    "heading": head or title,
                    "url": url_path + (f"#{anchor}" if anchor else ""),
                    "text": body,
                })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(records, open(OUT, "w"), ensure_ascii=False)

    words = sum(len(r["text"].split()) for r in records)
    print(f"{len(records)} chunks from {len(files)} pages, {words:,} words")
    print(f"median {sorted(len(r['text'].split()) for r in records)[len(records)//2]} words/chunk")
    print(f"wrote {OUT} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
