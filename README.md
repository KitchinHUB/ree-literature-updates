# Rare Earth Separation Literature Monitor

Automated monitoring system for tracking new publications and developments in rare earth element separation technologies.

## Quick Start

### Using Claude Code Slash Command

```
/literature-update
```

This will:
1. Search OpenAlex for recent academic publications
2. Search the web for news and developments
3. Generate a comprehensive report with bibliography

### Running the Script Directly

```bash
cd /home/user/scratch/rare-earth-project

# Last 7 days (default)
python scripts/literature_monitor.py

# Last 30 days
python scripts/literature_monitor.py --days 30

# Custom output file
python scripts/literature_monitor.py --output reports/custom_report.md

# With Slack notification
python scripts/literature_monitor.py --slack

# With Slack file upload
python scripts/literature_monitor.py --slack-upload
```

## Slack Integration

Get notified when new literature is found with a rich summary message.

### Option 1: Incoming Webhook (Simple)

Best for basic notifications with a summary.

1. **Create a Slack App**: https://api.slack.com/apps
2. **Enable Incoming Webhooks**: Features → Incoming Webhooks → On
3. **Add Webhook to Channel**: Click "Add New Webhook to Workspace"
4. **Copy the URL** and set it as an environment variable:

```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T.../B.../xxx"
python scripts/literature_monitor.py --slack
```

### Option 2: Bot Token (File Upload)

For uploading the full report as a file attachment.

1. **Create a Slack App**: https://api.slack.com/apps
2. **Add Bot Token Scopes**: OAuth & Permissions → Bot Token Scopes:
   - `files:write` - Upload files
   - `chat:write` - Send messages
3. **Install to Workspace** and copy the Bot Token
4. **Get Channel ID**: Right-click channel → View channel details → Copy ID
5. **Set environment variables**:

```bash
export SLACK_BOT_TOKEN="xoxb-..."
export SLACK_CHANNEL="C0123456789"
python scripts/literature_monitor.py --slack-upload
```

### Slack Message Preview

```
📚 Rare Earth Literature Update
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

47 new publications found from 2024-12-20 to 2024-12-27

🔬 Separation Technologies: 18
🧪 Extractants & Materials: 12
♻️ Recycling & Urban Mining: 8
🌱 Environmental & Sustainability: 5
📊 Supply Chain & Policy: 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Recent Highlights:

• Novel ionic liquid system for Nd/Pr separation
  Zhang, Y. et al. (Separation and Purification Technology)
  View paper

• Electrochemical recovery of rare earths from NdFeB magnets
  Smith, J. et al. (Hydrometallurgy)
  View paper

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📎 Full report: reports/2024-12-27_literature_update.md
```

## Directory Structure

```
rare-earth-project/
├── README.md
├── scripts/
│   ├── literature_monitor.py  # Search, screening, and report generation
│   └── weekly_update.sh       # Cron wrapper: run, commit, push, notify
├── reports/                 # Generated reports
│   └── YYYY-MM-DD_literature_update.md
└── .claude/
    └── commands/
        └── literature-update.md  # Slash command definition
```

## How Papers Are Selected

1. **Search.** Three OpenAlex title/abstract queries (`SEARCH_QUERIES` in
   `literature_monitor.py`) cover rare earth terms, the individual element
   names, and REE minerals and magnets. Every page of results is fetched, so
   nothing is cut off by a per-query cap.
2. **Clean up.** Duplicate records (repository version DOIs, preprint copies)
   are merged, and works dated after the report window are dropped.
3. **Prefilter.** The title, abstract, or keywords must name a rare earth
   (`REE_MENTION_PATTERNS`). Terms match as whole words, and element symbols
   that double as ordinary words (La, Pr, Er, Y) count only in a chemical
   context such as `La2O3`, `Eu3+`, or `Nd/Pr`.
4. **LLM relevance pass.** The `claude` CLI scores every candidate 0-3 for
   relevance to REE separation and assigns a category. Papers scoring 2 or
   more go in the report, each with a one-line reason; the rest are listed in
   a collapsed "Screened Out" section so the screening can be checked. If the
   pass fails, the run fails instead of publishing an unscreened report
   (`--no-llm` skips it deliberately).

Categories: Separation Technologies, Extractants & Materials, Recycling &
Urban Mining, Environmental & Sustainability, Supply Chain & Policy, Other.

## Data Sources

### OpenAlex (Academic Literature)
- Free, open scholarly database
- 250M+ works indexed
- Comprehensive metadata including abstracts
- Set `OPENALEX_API_KEY` for higher rate limits

### Claude Code CLI (Relevance Screening)
- The `claude` command must be installed and logged in
- Set `CLAUDE_BIN` if it is not on `PATH`; `--llm-model` picks the model
  (default `sonnet`)

### Web Search (News & Developments)
- Industry news and announcements
- Policy and regulatory updates
- Company developments
- Market analysis

## Report Format

Each report includes:

1. **Executive Summary**
   - Publication counts by category
   - Key highlights

2. **Categorized Publications**
   - Title and authors
   - Journal and publication date
   - Relevance score and the reason for it
   - Abstract (when available)
   - DOI and links
   - Open access indicator

3. **Bibliography**
   - Formatted citations, in section order
   - Screened-out candidates with scores and reasons
   - BibTeX entries for reference managers

## Setting Up Recurring Monitoring

### Option 1: Manual Weekly Check
Run `/literature-update` every Monday

### Option 2: Cron Job (Automated)
```bash
# Add to crontab for weekly Monday 8am execution
0 8 * * 1 cd /home/user/scratch/rare-earth-project && python scripts/literature_monitor.py
```

### Option 3: GitHub Actions
Create a workflow that runs weekly and commits reports to the repository.

## Customization

Settings live at the top of `scripts/literature_monitor.py`:
- `SEARCH_QUERIES`: the OpenAlex searches
- `REE_MENTION_PATTERNS`: the keyword prefilter
- `LLM_INSTRUCTIONS`: the relevance rubric and category definitions
- `RELEVANCE_THRESHOLD`, `LLM_MODEL`, `LLM_BATCH_SIZE`: screening settings

## Example Report

```markdown
# Rare Earth Separation Literature Update

**Report Period:** 2024-12-20 to 2024-12-27
**Total Publications Found:** 47

## Separation Technologies

### 1. Novel membrane process for selective Nd/Pr separation
**Authors:** Zhang, Y., Wang, L., et al.
**Published:** 2024-12-23 | **Journal:** Separation and Purification Technology
**DOI:** https://doi.org/10.1016/j.seppur.2024.xxxxx

**Abstract:** A novel supported liquid membrane system utilizing...

---
```

## Tips for Best Results

1. **Run weekly** to catch new publications before they're buried
2. **Review abstracts** to quickly assess relevance
3. **Use BibTeX entries** for easy import into reference managers
4. **Cross-reference** with your existing literature review
5. **Track open access** publications for full-text access
