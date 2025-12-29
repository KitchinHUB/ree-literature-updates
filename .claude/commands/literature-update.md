# Weekly Rare Earth Literature Update

Generate a comprehensive literature update report for rare earth separation research.

## Instructions

1. **Search OpenAlex** for recent academic publications using the literature_monitor.py script
2. **Search the web** for recent news and developments
3. **Compile and organize** findings into a structured report
4. **Generate bibliography** in both formatted and BibTeX formats

## Search Topics

Focus on these areas:
- Rare earth element separation technologies
- Solvent extraction and ion exchange methods
- New extractants (ionic liquids, deep eutectic solvents)
- REE recycling from e-waste and magnets
- Environmental and green chemistry approaches
- Supply chain developments and policy changes
- China export restrictions and alternatives

## Report Structure

Create a report at `reports/YYYY-MM-DD_weekly_update.md` with:

1. **Executive Summary** - Key findings and highlights
2. **Academic Publications** - Categorized by topic with abstracts
3. **Industry News** - Recent developments from web search
4. **Policy Updates** - Government and regulatory news
5. **Full Bibliography** - Formatted citations
6. **BibTeX Entries** - For reference management

## Execution

Run the literature monitor script:
```bash
cd /home/user/scratch/rare-earth-project
python scripts/literature_monitor.py --days 7
```

Then supplement with web search for:
- "rare earth separation" news last week
- "rare earth recycling" developments 2024
- "China rare earth export" policy
- "critical minerals" supply chain news

Synthesize all findings into a cohesive report.
