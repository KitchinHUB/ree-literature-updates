// Embed the passages from build_chunks.py into a static retrieval index.
//
// Runs at build time in Node. The browser embeds only the user's query, using
// the same package and the same model, so the vectors are directly comparable.
//
// Output: _build/html/chat/index.json
//   { model, dim, scale, chunks: [{page, heading, url, text}], vectors: base64 }
// Vectors are int8-quantized (cosine similarity is scale-invariant, and the
// error is far below the gap between a relevant and an irrelevant passage).

import { pipeline, env } from '@huggingface/transformers';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

env.allowLocalModels = false;

const MODEL = 'Xenova/bge-small-en-v1.5';
const IN = '_build/chat/chunks.json';
const OUT = '_build/html/chat/index.json';
const BATCH = 32;

const chunks = JSON.parse(readFileSync(IN, 'utf8'));
console.log(`embedding ${chunks.length} chunks with ${MODEL}`);

const extractor = await pipeline('feature-extraction', MODEL, { dtype: 'q8' });

// BGE is trained with the heading as part of the passage context; prepending it
// measurably helps short passages that never restate their own subject.
const passages = chunks.map((c) => `${c.page} — ${c.heading}\n${c.text}`);

const vecs = [];
for (let i = 0; i < passages.length; i += BATCH) {
  const batch = passages.slice(i, i + BATCH);
  const out = await extractor(batch, { pooling: 'cls', normalize: true });
  const dim = out.dims[1];
  for (let j = 0; j < batch.length; j++) {
    vecs.push(Array.from(out.data.slice(j * dim, (j + 1) * dim)));
  }
  process.stdout.write(`\r  ${Math.min(i + BATCH, passages.length)}/${passages.length}`);
}
console.log();

const dim = vecs[0].length;

// int8 quantization: vectors are unit-normalized, so components are in [-1, 1].
const SCALE = 127;
const flat = new Int8Array(vecs.length * dim);
let maxErr = 0;
vecs.forEach((v, i) => {
  v.forEach((x, k) => {
    const q = Math.max(-127, Math.min(127, Math.round(x * SCALE)));
    flat[i * dim + k] = q;
    maxErr = Math.max(maxErr, Math.abs(x - q / SCALE));
  });
});

mkdirSync('_build/html/chat', { recursive: true });
writeFileSync(OUT, JSON.stringify({
  model: MODEL,
  dim,
  scale: SCALE,
  count: chunks.length,
  chunks: chunks.map((c) => ({ p: c.page, h: c.heading, u: c.url, t: c.text })),
  vectors: Buffer.from(flat.buffer).toString('base64'),
}));

const kb = (s) => `${(s / 1024).toFixed(0)} KB`;
console.log(`dim ${dim}, max quantization error ${maxErr.toFixed(5)}`);
console.log(`wrote ${OUT} (${kb(readFileSync(OUT).length)})`);
