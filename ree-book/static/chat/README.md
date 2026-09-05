# Ask-the-book: retrieval-augmented chat on a static site

A question box on every page of a static site that searches the site's own text
and answers with real passages and deep links. No server, no API key, no paid
service, nothing to keep running. The index is built once at deploy time; the
rest happens in the reader's browser.

Built for a MyST site deployed to GitHub Pages, but only one of the six files
knows anything about the source format. This document is written so you can lift it.

## What it costs

| | |
|---|---|
| Reader who never opens the panel | **0 bytes** — nothing loads until the pill is clicked |
| Opening the panel | ~30 MB embedding model (browser-cached), plus the index |
| Index, this book (187k words, 830 passages) | 1.7 MB on disk, **707 KB gzipped on the wire** |
| Widget itself | 3.5 KB JS + 1.2 KB CSS, gzipped |
| Opting into generated answers | ~1 GB model download, browser-cached, WebGPU only |
| Hosting | $0. It is still a static site. |
| Per-question | $0, and no request leaves the reader's machine after load |

Index size scales with corpus, roughly **850 bytes gzipped per 200-word
passage**. A million-word corpus lands under 4 MB gzipped, which is where you
should start thinking about sharding or a smaller stored text field.

## The six files

```
tools/build_chunks.py    corpus  -> chunks.json      (the only MyST-specific part)
tools/embed_chunks.mjs   chunks  -> index.json       (embeddings, int8-quantized)
tools/inject_chat.py     built site -> site + widget (post-build injection)
tools/build_chat.sh      runs the three in order
static/chat/chat.js      the widget: query embedding, search, optional generation
static/chat/chat.css     styling
```

Plus a `package.json` pinning `@huggingface/transformers` to an exact version,
and three steps in the deploy workflow.

## Porting it

### To another MyST / Jupyter Book 2 site

Copy `static/chat/`, the four files in `tools/`, and `package.json`. Add to your
workflow after the HTML build:

```yaml
- name: Install index-builder dependencies
  working-directory: <your-book-dir>
  run: npm ci

- name: Build the retrieval index and inject the widget
  working-directory: <your-book-dir>
  run: bash tools/build_chat.sh
```

Set `BASE_URL` if you serve from a repository subpath — `inject_chat.py` reads
the same variable the MyST build does. That is all; nothing else is
site-specific.

### To a non-MyST site

**Replace `build_chunks.py` and keep everything else.** Its only contract is to
emit a JSON array of objects with four string fields:

```json
[{"page": "Chapter title",
  "heading": "Section title",
  "url": "/path/to/page/#anchor",
  "text": "The passage itself, a few hundred words."}]
```

Whatever produces that — an HTML scrape with BeautifulSoup, a walk over
Markdown, a database query — the remaining four files work unchanged.

Injection assumes each page is an HTML file containing `</body>`. For a
single-page app, drop the two `<script>`/`<link>` tags into the template
instead and skip `inject_chat.py` entirely.

## The decisions that actually matter

**Chunk at headings, not at a fixed token count.** A heading is a
human-authored statement of what a passage is about, and it doubles as a deep
link. Fixed-size windows cut mid-argument and give you nothing to link to. Long
sections are split further at paragraph boundaries, and every sub-chunk keeps
its parent heading's anchor, so a hit always lands the reader somewhere real.

**Prepend the heading to the passage before embedding.** Passages rarely restate
their own subject — a paragraph deep in a section about bauxite residue may
never say "bauxite." Embedding `"{page} — {heading}\n{text}"` fixes this and
costs nothing.

**Keep the citations.** The first version stripped citation nodes and produced
text like *"report multiple-model predictive control of component content"* —
the authors had been in the node that was dropped. Render them as
`Zhang et al. (2016)`. It repairs the sentence and makes author-year searchable.

**Pin the model dtype on both sides.** This was a real bug here. The build ran
`fp32` in Node; the browser would have defaulted to `q8`. Queries and passages
would then have come from different model precisions and been quietly less
comparable — no error, just worse results. Both are pinned to `q8`.

**int8-quantize the stored vectors.** Cosine similarity is scale-invariant, so
storing `round(x * 127)` costs a max component error of 0.004 and cuts the
vector payload by 4×. Do this; there is no downside at this scale.

**Retrieval first, generation second and optional.** The panel always shows
sourced passages. Generation is a button, needs WebGPU, is prompted to use only
the supplied excerpts, and renders in a visually distinct box *above* the
passages rather than instead of them. A small model will occasionally invent a
number, and it will be wearing your site's name when it does. Design so the
reader can always see what the answer was built from.

## Calibrating the refusal floor — do this on your own corpus

The most valuable knob, and the one you must set yourself. Embed a handful of
questions your corpus **does** answer and a handful it obviously does not, and
look at the top score for each:

```
0.86  why is scandium found in bauxite residue?     -> Bauxite Residue
0.82  how much lithium is in Pennsylvania water?    -> What Pennsylvania Produces
0.72  how many stages does a cascade need?          -> A Fenske Bound
----------------------------------------------------- floor at 0.55
0.54  best pizza toppings
0.46  what is the capital of France?
```

On this corpus the bands are 0.72–0.86 and 0.46–0.54, so 0.55 sits in a clean
gap. Below the floor the panel says the book may not cover the question instead
of serving a confident irrelevant passage. **Your gap will be somewhere else.**
A corpus with narrower vocabulary compresses the range; if the bands overlap,
your chunks are probably too long or too heterogeneous.

## Gotchas

- **MyST has no hook for custom JavaScript.** Hence post-build injection.
  `inject_chat.py` is idempotent, so re-running it is safe.
- **MyST v2 emits a Remix SPA.** A fixed-position element appended to
  `document.body` sits outside the React root and survives client-side
  navigation. Do not mount it inside the app's container.
- **`BASE_URL`.** Serving from a subpath breaks every absolute path if you
  forget it. Store chunk URLs base-*relative* and prefix at render time, so the
  index is portable across deployments.
- **`npm audit` reports high CVEs in `sharp`**, a hard transitive dependency of
  transformers.js. They are libvips image-decoding bugs. This pipeline only
  embeds text and never decodes an image, and it is a build-time dependency that
  never reaches readers. Judge it for your own threat model.
- **CI adds ~2 minutes**, nearly all of it downloading the embedding model.
  Cache `~/.cache/huggingface` in the workflow to remove it.
- **GitHub Pages gzips JSON automatically.** Do not hand-compress the index.

## Tuning

| Knob | Where | Default | Effect |
|---|---|---|---|
| `TARGET_WORDS` | `build_chunks.py` | 220 | Shorter = sharper hits, bigger index |
| `MODEL` | `embed_chunks.mjs` | `bge-small-en-v1.5` | `all-MiniLM-L6-v2` is smaller and weaker |
| `FLOOR` | `chat.js` | 0.55 | Refusal threshold — **recalibrate per corpus** |
| `TOP_K` / `CONTEXT_K` | `chat.js` | 5 / 4 | Passages shown vs. passages sent to the model |
| `GEN_MODEL` | `chat.js` | `Qwen2.5-1.5B-Instruct-q4f16_1-MLC` | `Llama-3.2-1B` is ~half the download and worse at refusing |

Both models come from public CDNs (jsDelivr for the libraries, Hugging Face for
weights, MLC for the generation model). If you need to remove that dependency,
self-host the weights and set `env.remoteHost` in transformers.js.

## Verifying a port

1. `bash tools/build_chat.sh`, then check the chunk count and median word count
   look sane for your corpus.
2. **Read twenty random chunks.** This is where the citation-stripping and
   list-concatenation bugs above were caught. Nothing else finds them.
3. Run the floor calibration above.
4. Build once with `BASE_URL` set and once without; confirm the injected paths
   and a deep link resolve in both.
5. Open it in a browser and ask it something. The steps above verify the math,
   not the interface.
