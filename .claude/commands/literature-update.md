# Weekly Rare Earth Literature Update

Generate a comprehensive literature update report for rare earth separation research.

## Workflow

Execute these steps in order:

### Step 1: Fetch Academic Publications

Run the literature monitor to search OpenAlex for recent publications:

```bash
python3 scripts/literature_monitor.py --days $DAYS
```

Use `--days 7` by default, or the value provided by the user.

### Step 2: Web Search for Industry News

Search the web for recent news and developments. Run these searches:

1. "rare earth separation" news $CURRENT_YEAR
2. "rare earth recycling" developments $CURRENT_YEAR
3. "critical minerals supply chain" news $CURRENT_YEAR
4. "rare earth China export" policy $CURRENT_YEAR

### Step 3: Read and Enhance the Report

Read the generated report from `reports/YYYY-MM-DD_literature_update.md`.

Add a new section called "## Industry & Policy News" after the academic sections, summarizing key findings from the web search. Include:
- Recent industry developments
- Policy and regulatory updates
- Supply chain news
- Links to sources

### Step 4: Write Executive Summary

Update the Executive Summary section to highlight:
- Most significant academic publications
- Key industry developments from web search
- Notable policy changes
- Emerging trends

### Step 5: Commit and Push (if requested)

If the user requests it, commit and push the report:

```bash
git add reports/
git commit -m "Add literature update for $(date +%Y-%m-%d)"
git push origin main
```

### Step 6: Slack Notification (if requested)

If the user requests Slack notification:

```bash
python3 scripts/literature_monitor.py --days $DAYS --slack
```

## Default Behavior

- Search the last 7 days unless specified otherwise
- Always generate the enhanced report with web search results
- Ask before committing/pushing to GitHub
- Ask before sending Slack notification

## Output

The final report will be saved to: `reports/YYYY-MM-DD_literature_update.md`
