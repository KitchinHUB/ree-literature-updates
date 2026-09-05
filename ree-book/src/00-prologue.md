---
title: Prologue — How This Book Was Made
---

(prologue-how-this-book-was-made)=
# Prologue: How This Book Was Made

## A disclaimer about AI

**This book was assembled with substantial AI assistance, and you should read it
accordingly.**

The source material was produced over roughly a year of work in which large
language models were used to search the literature, summarize papers, and draft
review prose. Some chapters began as AI-generated documents that were then
reviewed and edited; others are original analysis by group members that used AI
only for search and formatting. The reorganization into this book — the chapter
structure, the merging of overlapping documents, and the bibliography
consolidation — was also done with AI assistance.

That method has a specific, well-documented failure mode: **language models
fabricate citations.** They produce references that are formatted correctly,
attributed to plausible journals, and describe papers that do not exist. This is
not a hypothetical concern for this book. It happened here, and we found it.

## What we found

When the six source bibliographies were merged, an audit turned up:

- **Nine entries with no author, no DOI, and no URL**, carrying titles precisely
  matched to gaps in the review's argument — for example *"Role of Phosgene and
  Carbon Tetrachloride as Intermediates in Carbochlorination Reactions"* and
  *"Activation Energy Determination for Carbochlorination of Light Rare Earth
  Oxides."* These have every characteristic of fabricated references.
- **Twenty-nine entries with placeholder authorship** of the form
  `author = {{PNAS Authors}}` or `{{ScienceDirect Authors}}` — auto-generated
  filler where a real author list was never captured.
- **Two hundred and eleven entries with no author field at all**, in a single
  source file.
- One source document that carried its own unresolved warning in its reference
  section: *"If there is not a url, the reference may be hallucinated."*

## What we did about it

Every reference in this book went through the following pipeline. Each step is
a script in `tools/`, so the whole bibliography can be rebuilt from the original
sources and audited independently.

**1. Merge and deduplicate.** Six separate bibliographies had accumulated across
the source documents, overlapping and contradicting each other. Five were merged;
one (`nnl.bib`) was excluded as a general materials-science library with no
overlap with this subject matter. Deduplication ran in two passes, because one
pass is not enough: matching on DOI alone misses duplicates where neither copy
records a DOI, and matching on citation key alone misses duplicates where the
same paper was filed under two different keys in two different files. Both
happened here. Where duplicates were merged, the record with more complete
metadata survived and filled its gaps from the other.

**2. Re-key from metadata.** Citation keys were regenerated from each entry's
actual author, year, and title rather than trusting the inherited keys, three
incompatible conventions of which were in use — and which in about a hundred
cases encoded a journal or topic word instead of an author.

**3. Recover missing identifiers.** Entries lacking a DOI were searched against
CrossRef by title. A match was accepted only when the normalized title
similarity exceeded 0.90 *and* the publication year agreed within one year.
Anything below that bar was left alone and reported rather than guessed at, so
no entry silently acquired the DOI of a different paper.

**4. Verify every entry against an external source.** Each reference was checked
by one of three routes:

- *DOI resolution.* The DOI was resolved against the CrossRef works API. A DOI
  that resolves is positive evidence the paper exists.
- *Live URL.* Sources that legitimately have no DOI — standards pages, software
  documentation, agency reports — were verified by confirming the URL responds.
- *Neither.* Entries with no DOI and no URL cannot be checked by any automated
  means. These were treated as unverified.

**5. Repair authorship from authoritative metadata.** Where a DOI resolved, the
author list, journal, year, and volume returned by CrossRef were treated as
authoritative and used to replace placeholder authorship and fill empty fields.
This is what corrected the `{{Journal}} Authors` entries and the entries with no
author at all.

**6. Cross-check titles.** For every entry with a resolving DOI, the title
recorded in the bibliography was compared against the title CrossRef returns for
that DOI. Divergence means the DOI and the description have come apart — either
the DOI is wrong or the reference was described inaccurately. Those cases are
listed for manual review rather than auto-corrected.

**7. Delete what could not be verified.** Entries that failed verification were
removed from the bibliography — not quietly, but into a separate
`references-rejected.bib` file that stays in the repository. Any claim in the
text resting solely on a deleted citation was removed or rewritten rather than
left standing unsupported.

### What the pipeline actually removed

Running it over the merged bibliography:

| | |
|---|---|
| Entries loaded from five source files | 506 |
| Duplicates merged away | 33 |
| Missing DOIs recovered from CrossRef | 77 of 154 |
| Author fields repaired from CrossRef | 172 |
| Wrong DOIs corrected | 37 |
| **Entries verified** | **406** (359 by DOI, 47 by live URL) |
| **Entries rejected and deleted** | **67** |

**Roughly one reference in seven did not survive.** That is the scale of the
problem this book started with, and it is why the disclaimer above is stated as
plainly as it is.

The 37 corrected DOIs deserve their own note, because they are the most
dangerous category and the least visible. These entries carried a DOI that
resolved perfectly well — and pointed at a completely different paper. A
citation reading *"Selective Precipitation of Rare Earth and Critical
Elements"* resolved to a paper about anaerobic digestion. The failure pattern
was consistent: the journal and year were right and the article number was
invented, landing on a real but unrelated paper in the same journal. A checker
that only asks "does this DOI resolve?" passes every one of them.

Finding these required comparing each entry's recorded title against the title
its DOI actually belongs to, then searching for the DOI the *title* belongs to.
Where that search found the real paper, the DOI was corrected; where it found
nothing, the entry was rejected as describing a paper that does not exist. In
no case was a wrong DOI's title adopted, which would have quietly swapped one
reference for another.

### What this does and does not establish

Be clear about the limits. This pipeline confirms that a cited paper **exists**,
that its **authorship and venue are recorded correctly**, and that its **title
matches its DOI**. That is enough to catch fabricated references, and it caught
them.

It does **not** confirm that a paper says what this book says it says. No
automated check can do that. Verifying that a claim is faithful to its source
requires reading the source, which is why the guidance below matters.

The full record is kept alongside the book rather than hidden:

- `bibliography-audit.md` — every duplicate merged and every entry flagged, with
  the reason.
- `doi-recovery.md` — every DOI recovered, with its match confidence, and every
  entry where recovery failed.
- `verification-report.md` — every entry rejected and why, every author field
  repaired, and every title that disagrees with its DOI.
- `references-rejected.bib` — the removed entries themselves, kept so a later
  reader can re-examine the judgment.

These files are part of the repository. If you want to know why a reference is
or is not here, that is where to look.

## How to use this book

Treat it as **a map, not a source.** It is a well-organized orientation to a
large literature, and it will tell you what questions the field is asking and
roughly where the answers live. It is not a substitute for reading the primary
literature.

Concretely:

- **Before you cite anything from this book in your own work, read the primary
  source.** The citation is a pointer, not evidence that the claim is right.
- **Treat specific numbers with particular caution.** Yields, separation
  factors, energy figures, and cost estimates are the details most likely to
  drift during summarization. Check them against the paper.
- **If something looks wrong, it may be.** Please correct it. This book is
  version-controlled and meant to be edited.

The value here is in the organization and the synthesis across a scattered
literature. The reliability of any individual sentence is the reliability of the
process described above — good enough to orient you, not good enough to build on
unchecked.

## Requesting a change: file an issue

This book is meant to grow. If a section is missing, out of date, or wrong,
**open a GitHub issue** — you do not need to write the content yourself, and you
do not need repository access to ask.

Issues are worked by Claude, so an issue is effectively a work order written for
someone who has not read the paper you have in mind and cannot ask you a quick
question in the hallway. The more specific it is, the less it will bounce back.
Expect clarifying questions, and expect the result to be reviewed by a group
member before it lands.

Use the **Book content** issue template, which asks for these things:

**What to change, and what kind of change it is.** Say whether you are adding
new material, correcting something wrong, updating something stale, or asking
for a whole new section. "Add a subsection on membrane fouling in REE
nanofiltration" is workable. "The membrane chapter needs work" is not.

**Where it goes.** Name the chapter, and the section within it if you can — for
example, *Chapter 13, Membranes, MOFs and Emerging Approaches, after the
nanofiltration subsection*. If you genuinely do not know where it belongs, say
so and propose a home; deciding placement is part of the work, but a starting
guess saves a round trip. If you are asking for a new chapter, say where it sits
relative to the existing ones.

**The papers, as DOIs.** This is the most important field. Give DOIs, not titles
or PDF attachments — the DOI is what makes a reference verifiable, and every
citation added to this book has to clear the verification pipeline described
above. An issue that names a finding without a DOI cannot be actioned; it will
come back asking for one. If the source has no DOI, give a stable URL and say
what kind of source it is.

**What the source actually shows.** One or two sentences on the finding and why
it belongs here — the specific result, not the abstract. If a number matters
(a separation factor, a yield, a temperature), state it and say where in the
paper it appears. This is also the check on faithfulness that automation cannot
do: you have read the paper, and the pipeline has not.

**What it changes.** If the new material contradicts something the book
currently says, say so explicitly and point at the passage. Corrections are more
valuable than additions and are easy to miss.

A good issue looks roughly like this. The DOI below is a deliberate
non-resolving placeholder — `10.0000/…` belongs to no registrant — because the
findings in the example are invented, and attaching invented findings to a real
paper is the thing this whole section exists to prevent:

> **Type:** correction
> **Where:** Ch. 5 Hydrometallurgical Leaching, §5.2 In-Situ Leaching Process
> **DOIs:** 10.0000/placeholder.replace.me
> **What it shows:** Reports 82% REE recovery with magnesium sulfate lixiviant
> at pH 4.5 (Table 3), against the ~70% the chapter currently attributes to
> ammonium sulfate. Directly relevant to the ammonia-pollution discussion.
> **What it changes:** The chapter presents ammonium sulfate as the performance
> benchmark. This paper suggests the ammonia-free route is no longer a recovery
> tradeoff, which weakens the "gentle but lower-yield" framing in that section.

An earlier draft of this page used a plausible-looking Elsevier DOI here instead
of a placeholder. It resolved — to a review of pyrite flotation, which has
nothing to do with rare earths. The template that teaches DOI hygiene shipped
with a wrong DOI, and the verification pass that checks every entry in the
bibliography did not flag it, because it resolved. That is
the failure mode: not a broken link, which any script catches, but a working
link to the wrong paper, which only a reader who opens it catches. Open it.

Two things that are not issues: if you have already written the prose, open a
pull request instead; and if you are only flagging a suspect citation, say so
plainly — that gets checked against `verification-report.md` rather than
triggering a rewrite.
