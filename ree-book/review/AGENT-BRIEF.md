# Brief for agents working the FIXPLAN

You are editing a MyST Markdown book, "Rare Earth Element Separations", in
`ree-book/src/`. Read `review/FIXPLAN.md` for the item you were assigned and
`review/raw/*.md` for the underlying review evidence.

## Hard rules

1. **File ownership.** You may edit ONLY the files named in your assignment.
   Do not touch any other file under `src/`, and never touch `references.bib`,
   `review/FIXPLAN.md`, or `myst.yml`. Another agent is working in parallel.
2. **Citations.** Cite as `[@key]`. Every key you use MUST already exist in
   `references.bib` — check with `grep -n "^@.*{key," references.bib`.
   If a claim needs a source that is not there:
   - verify the DOI against CrossRef:
     `curl -s -H "User-Agent: ree-book/1.0 (https://github.com/KitchinHUB/ree-literature-updates; mailto:jkitchin@andrew.cmu.edu)" "https://api.crossref.org/works/<DOI>"`
   - key it `lastnameYEARword`
   - append the BibTeX entry to `review/bib-additions/<your-name>.bib`
   - use the key in the text as normal; the orchestrator merges the file.
   Never invent a DOI, a key, or an author.
3. **A citation that resolves is not thereby correct.** Before attaching a key
   to a number, confirm the cited work actually contains that number (CrossRef
   abstract, or the notes in `review/raw/`). If you cannot confirm it, either
   delete the claim or rewrite it as qualitative. An unsupported number is
   worse than no number.
4. **67 citations were deleted from this book** (`references-rejected.bib`).
   Nothing may rest on those keys.
5. **Do not invent data.** No fabricated recoveries, TRLs, costs, or separation
   factors. If the plan says "source or delete", deleting is an acceptable and
   often correct outcome — say so in your report.
6. **Do not run the build, do not `git add`, do not `git commit`.** The
   orchestrator builds and commits.

## Conventions

- Every file has an explicit `(slug)=` label above its H1. Cross-reference other
  chapters as `[](#slug)` — get the slug by grepping `^(.*)=` in the target file.
- Index entries: ``{index}`term` `` or ``{index}`shown <indexed>` ``. The pattern
  must not fire mid-word.
- Tables are pipe tables. Prose is narrative, not bullet-soup, where the
  surrounding text is narrative; match the register of the file you are in.
- Do not add a heading level deeper than `####`.

## Reporting

When done, write a short report to `review/agent-reports/<your-name>.md`:
what you changed, what you deleted and why, any bib entries you added, and
anything you could not resolve. Then return that same summary as your final
message. Be concrete and honest about what you could not verify.
