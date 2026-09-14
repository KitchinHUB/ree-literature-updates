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
cd ree-literature-updates   # the repository root

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

# Rebuild a past week's report
python scripts/literature_monitor.py --to-date 2026-09-14 --days 7

# Skip the LLM relevance pass (lists every candidate, unscreened)
python scripts/literature_monitor.py --no-llm
```

The script uses only the Python standard library. The relevance pass needs
the `claude` CLI installed and logged in (see [Data Sources](#data-sources)).

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

47 new publications found from 2026-09-07 to 2026-09-14

🔬 Separation Technologies: 10
🧪 Extractants & Materials: 11
♻️ Recycling & Urban Mining: 5
🌱 Environmental & Sustainability: 10
📊 Supply Chain & Policy: 10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Highlights:

• Development of a Ca-K-Li-RE-Cl (RE = La, Ce, Pr, Nd) rare-earth molten salt database
  Nicholas Ury, Brandon Bocklund et al. (Calphad)
  View paper

• Detoxification of Ion-Adsorption Rare Earth Elements Low-Level Radioactive Residues
  Qingqing Chang, Fanxin Xie et al. (ACS Sustainable Resource Management)
  View paper

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📎 Full report: reports/2026-09-14_literature_update.md
```

## Directory Structure

```
ree-literature-updates/
├── README.md
├── .env                          # API keys and Slack settings (not committed)
├── scripts/
│   ├── literature_monitor.py     # Search, screening, and report generation
│   ├── weekly_update.sh          # Cron wrapper: run, commit, push, notify
│   └── claude_weekly_update.sh   # Runs /literature-update non-interactively
├── reports/                      # Generated reports
│   └── YYYY-MM-DD_literature_update.md
├── logs/                         # Cron and update logs
├── ree-book/                     # The REE separation book (MyST)
├── .github/workflows/
│   └── deploy-book.yml           # Builds and deploys the book
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

### Cron Job (Current Setup)

`scripts/weekly_update.sh` runs the monitor, commits and pushes the new
report, then posts the Slack summary from the same run's saved results
(`.cache/last_run.json`). If any step fails, it posts a warning to Slack
instead. It reads `OPENALEX_API_KEY` and the Slack variables from `.env`
in the repository root, and runs Python from the path set in `PYTHON` at
the top of the script; edit that for your machine.

```bash
# crontab -e: every Monday at 4am
0 4 * * 1 /path/to/ree-literature-updates/scripts/weekly_update.sh >> /path/to/ree-literature-updates/logs/cron.log 2>&1
```

Cron runs with a minimal `PATH`, so the script adds `~/.local/bin` (the
default `claude` install location). Do not set `ANTHROPIC_API_KEY` in the
cron environment unless it is valid: it overrides the CLI's login.

### Manual Check With Claude Code
Run `/literature-update` in Claude Code. It runs the monitor, then adds web
news and an executive summary.

## Customization

Settings live at the top of `scripts/literature_monitor.py`:
- `SEARCH_QUERIES`: the OpenAlex searches
- `REE_MENTION_PATTERNS`: the keyword prefilter
- `LLM_INSTRUCTIONS`: the relevance rubric and category definitions
- `RELEVANCE_THRESHOLD`, `LLM_MODEL`, `LLM_BATCH_SIZE`: screening settings

## Example Report

```markdown
# Rare Earth Separation Literature Update

**Report Period:** 2026-09-07 to 2026-09-14
**Total Publications Found:** 47

## Separation Technologies

### 2. Detoxification of Ion-Adsorption Rare Earth Elements Low-Level Radioactive Residues via Mild Alkali–Carbonate: Uranium Extraction and Multi-Metal Recovery

**Authors:** Qingqing Chang, Fanxin Xie, Siyan Mao, Lingsheng Ke, Hailin Zhang

**Published:** 2026-09-12 | **Journal:** ACS Sustainable Resource Management | **Citations:** 0 | **Access:** 🔒

**DOI:** [https://doi.org/10.1021/acssusresmgt.6c00145](https://doi.org/10.1021/acssusresmgt.6c00145)

**Relevance (3/3):** Develops mild alkali-carbonate leaching process to detoxify REE-bearing radioactive residues while enriching REE grade and extracting uranium.

**Abstract:** Abstract Impeded by the harsh high-temperature/pressure conditions...

**Keywords:** Leaching (pedology), Uranium, Detoxification (alternative medicine), Residue (chemistry), Extraction (chemistry)

---

...

## Screened Out

<details>
<summary>268 candidates scored below 2</summary>

- (1) [Polymorph Engineering of the Layered Rare-Earth Magnet GdAlGe](https://doi.org/10.48550/arxiv.2609.08601): Materials physics study of a layered Gd-based magnet for spintronics, not about REE extraction or separation.
...
</details>
```

See `reports/2026-09-14_literature_update.md` for a full report.

## Tips for Best Results

1. **Run weekly** to catch new publications before they're buried
2. **Skim the Screened Out list** now and then; if good papers land there,
   adjust `LLM_INSTRUCTIONS`
3. **Use BibTeX entries** for easy import into reference managers
4. **Cross-reference** with your existing literature review
5. **Track open access** publications for full-text access
