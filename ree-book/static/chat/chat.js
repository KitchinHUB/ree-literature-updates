/* Ask-the-book: retrieval over the book's own text, with optional local
 * generation. No server, no API key, no network beyond two public CDNs.
 *
 * Retrieval always runs and always shows real passages with deep links.
 * Generation is opt-in, runs in the browser via WebGPU, and is constrained to
 * the retrieved passages. The two are kept visually distinct on purpose: this
 * book's standard is that every number traces to a source, and a generated
 * sentence is not a source.
 */
(function () {
  'use strict';

  var BASE = window.__BOOK_CHAT_BASE__ || '';
  var TF = 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.8.1/+esm';
  var LLM = 'https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.84/+esm';
  var GEN_MODEL = 'Qwen2.5-1.5B-Instruct-q4f16_1-MLC';

  var TOP_K = 5;          // passages retrieved
  var CONTEXT_K = 4;      // passages handed to the model
  var FLOOR = 0.55;       // below this, treat the question as out of scope

  var idx = null, embed = null, engine = null, busy = false;

  /* ---------- UI ---------- */

  var openBtn = document.createElement('button');
  openBtn.id = 'bookchat-open';
  openBtn.type = 'button';
  openBtn.textContent = 'Ask this book';

  var panel = document.createElement('div');
  panel.id = 'bookchat';
  panel.innerHTML =
    '<header><b>Ask this book</b><span>searches the text you are reading</span>' +
    '<button type="button" aria-label="Close">×</button></header>' +
    '<div id="bookchat-log"></div>' +
    '<form><input type="text" placeholder="e.g. how many stages does a cascade need?" ' +
    'aria-label="Question" autocomplete="off"><button class="bc-go" type="submit">Ask</button></form>';

  document.body.appendChild(openBtn);
  document.body.appendChild(panel);

  var log = panel.querySelector('#bookchat-log');
  var form = panel.querySelector('form');
  var input = panel.querySelector('input');
  var goBtn = panel.querySelector('.bc-go');

  function el(cls, text) {
    var d = document.createElement('div');
    if (cls) d.className = cls;
    if (text) d.textContent = text;
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
    return d;
  }

  openBtn.addEventListener('click', function () {
    panel.classList.add('open');
    openBtn.style.display = 'none';
    input.focus();
    if (!idx) warmUp();
  });
  panel.querySelector('header button').addEventListener('click', function () {
    panel.classList.remove('open');
    openBtn.style.display = '';
  });

  /* ---------- retrieval ---------- */

  var vectors = null;

  async function warmUp() {
    var status = el('bc-note', 'Loading the index…');
    try {
      var res = await fetch(BASE + '/chat/index.json');
      if (!res.ok) throw new Error('index ' + res.status);
      idx = await res.json();
      var bin = atob(idx.vectors);
      var buf = new Uint8Array(bin.length);
      for (var i = 0; i < bin.length; i++) buf[i] = bin.charCodeAt(i);
      vectors = new Int8Array(buf.buffer);

      status.textContent = 'Loading the search model (about 30 MB, cached after this)…';
      var t = await import(TF);
      // dtype is pinned to match tools/embed_chunks.mjs: query and passage
      // vectors must come from the same model precision to be comparable.
      embed = await t.pipeline('feature-extraction', idx.model, { dtype: 'q8' });

      status.remove();
      el('bc-note', 'Ready. ' + idx.count + ' passages from ' +
        'the book are searchable. Answers quote the book and link to it.');
    } catch (e) {
      status.className = 'bc-warn';
      status.textContent = 'Could not load the search index: ' + e.message;
      throw e;
    }
  }

  async function search(q) {
    // BGE expects this prefix on queries but not on passages.
    var out = await embed(
      ['Represent this sentence for searching relevant passages: ' + q],
      { pooling: 'cls', normalize: true });
    var qv = out.data, dim = idx.dim, scored = [];
    for (var i = 0; i < idx.count; i++) {
      var s = 0, off = i * dim;
      for (var k = 0; k < dim; k++) s += qv[k] * vectors[off + k];
      scored.push({ score: s / idx.scale, i: i });
    }
    scored.sort(function (a, b) { return b.score - a.score; });
    return scored.slice(0, TOP_K);
  }

  function renderHits(hits) {
    hits.forEach(function (h, n) {
      var c = idx.chunks[h.i];
      var d = el('bc-hit');
      d.innerHTML =
        '<a href="' + BASE + c.u + '"></a>' +
        '<div class="bc-where"></div><p></p>';
      d.querySelector('a').textContent = '[' + (n + 1) + '] ' + c.h;
      d.querySelector('.bc-where').textContent = c.p + '  ·  ' + h.score.toFixed(2);
      d.querySelector('p').textContent =
        c.t.length > 460 ? c.t.slice(0, 460).replace(/\s+\S*$/, '') + '…' : c.t;
    });
  }

  /* ---------- generation (opt-in) ---------- */

  var SYSTEM =
    'You answer questions about a technical book on rare earth element separations, ' +
    'using only the numbered excerpts supplied with each question.\n' +
    'Rules, in order of importance:\n' +
    '1. Use ONLY the excerpts. Never add a number, element, chemical, author, or ' +
    'citation that does not appear in them.\n' +
    '2. Attach a bracketed excerpt number to every factual claim, like [2].\n' +
    '3. If the excerpts do not answer the question, say exactly that and stop. ' +
    'Do not guess and do not fill the gap from general knowledge.\n' +
    '4. Be brief: three or four sentences unless the question needs a list.\n' +
    '5. Prefer the book\'s own wording for anything quantitative.';

  function buildPrompt(q, hits) {
    var ctx = hits.slice(0, CONTEXT_K).map(function (h, n) {
      var c = idx.chunks[h.i];
      return '[' + (n + 1) + '] (' + c.p + ' — ' + c.h + ')\n' + c.t;
    }).join('\n\n');
    return 'Excerpts:\n\n' + ctx + '\n\nQuestion: ' + q;
  }

  function hasWebGPU() { return typeof navigator !== 'undefined' && !!navigator.gpu; }

  async function synthesize(q, hits, btn) {
    btn.disabled = true;
    var box = el('bc-answer');
    box.innerHTML = '<span class="bc-tag"></span><div class="bc-body"></div>';
    var tag = box.querySelector('.bc-tag');
    var body = box.querySelector('.bc-body');
    tag.textContent = 'Generated locally — verify against the passages below';

    try {
      if (!engine) {
        body.textContent = 'Loading the language model. This is a ~1 GB download ' +
          'on first use and is cached by the browser afterwards…';
        var w = await import(LLM);
        engine = await w.CreateMLCEngine(GEN_MODEL, {
          initProgressCallback: function (p) { body.textContent = p.text; }
        });
      }
      body.textContent = '';
      var stream = await engine.chat.completions.create({
        stream: true,
        temperature: 0.2,
        max_tokens: 400,
        messages: [
          { role: 'system', content: SYSTEM },
          { role: 'user', content: buildPrompt(q, hits) }
        ]
      });
      for await (var chunk of stream) {
        var piece = chunk.choices[0].delta.content;
        if (piece) { body.textContent += piece; log.scrollTop = log.scrollHeight; }
      }
    } catch (e) {
      box.className = 'bc-warn';
      box.textContent = 'Local generation failed: ' + e.message +
        ' The passages below are unaffected.';
    }
  }

  /* ---------- ask ---------- */

  form.addEventListener('submit', async function (ev) {
    ev.preventDefault();
    var q = input.value.trim();
    if (!q || busy) return;
    busy = true; goBtn.disabled = true; input.value = '';
    el('bc-q', q);

    try {
      if (!idx) await warmUp();
      var thinking = el('bc-note', 'Searching…');
      var hits = await search(q);
      thinking.remove();

      if (!hits.length || hits[0].score < FLOOR) {
        el('bc-warn', 'Nothing in the book looks like a close match for that. ' +
          'The nearest passages are below, but treat them as a weak result — ' +
          'the book may simply not cover this.');
      }
      renderHits(hits);

      if (hits.length && hits[0].score >= FLOOR) {
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'bc-syn';
        if (hasWebGPU()) {
          btn.textContent = 'Synthesize an answer from these passages';
          btn.addEventListener('click', function () { synthesize(q, hits, btn); });
        } else {
          btn.textContent = 'Synthesis needs WebGPU (Chrome, Edge, or Safari 18+)';
          btn.disabled = true;
        }
        log.appendChild(btn);
        log.scrollTop = log.scrollHeight;
      }
    } catch (e) {
      el('bc-warn', 'Something went wrong: ' + e.message);
    } finally {
      busy = false; goBtn.disabled = false; input.focus();
    }
  });
})();
