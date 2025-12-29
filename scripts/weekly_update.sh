#!/bin/bash
#
# Weekly Rare Earth Literature Update
# Runs the literature monitor, commits to GitHub, and notifies Slack
#
# Usage: ./scripts/weekly_update.sh [--days N]
#

set -e  # Exit on error

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_FILE="$PROJECT_DIR/logs/weekly_update.log"
PYTHON="/Users/jkitchin/Dropbox/uv/.venv/bin/python"

# Ensure PATH includes git and other tools for cron
export PATH="/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:$PATH"

# Source environment variables
if [ -f "$PROJECT_DIR/.env" ]; then
    export $(grep -v '^#' "$PROJECT_DIR/.env" | xargs)
fi

# Default to 7 days if not specified
DAYS=${1:-7}
if [ "$1" = "--days" ]; then
    DAYS=${2:-7}
fi

# Create logs directory if needed
mkdir -p "$PROJECT_DIR/logs"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Starting weekly literature update (last $DAYS days)"

cd "$PROJECT_DIR"

# Run the literature monitor
log "Running literature monitor..."
$PYTHON scripts/literature_monitor.py --days "$DAYS"

# Get today's report filename
REPORT_DATE=$(date '+%Y-%m-%d')
REPORT_FILE="reports/${REPORT_DATE}_literature_update.md"

if [ ! -f "$REPORT_FILE" ]; then
    log "Error: Report file not found: $REPORT_FILE"
    exit 1
fi

log "Report generated: $REPORT_FILE"

# Check if there are changes to commit
if git diff --quiet HEAD -- "$REPORT_FILE" 2>/dev/null && ! git ls-files --error-unmatch "$REPORT_FILE" &>/dev/null; then
    # File is new (untracked)
    HAS_CHANGES=true
elif ! git diff --quiet HEAD -- "$REPORT_FILE" 2>/dev/null; then
    # File has changes
    HAS_CHANGES=true
else
    HAS_CHANGES=false
fi

if [ "$HAS_CHANGES" = true ]; then
    log "Committing report to git..."
    git add "$REPORT_FILE"
    git commit -m "Add literature update for $REPORT_DATE

Automated weekly update covering the last $DAYS days.

🤖 Generated with [Claude Code](https://claude.com/claude-code)"

    log "Pushing to GitHub..."
    git push origin main

    log "Changes pushed to GitHub"
else
    log "No new changes to commit"
fi

# Send Slack notification
if [ -n "$SLACK_WEBHOOK_URL" ]; then
    log "Sending Slack notification..."
    $PYTHON scripts/literature_monitor.py --days "$DAYS" --slack
    log "Slack notification sent"
else
    log "Warning: SLACK_WEBHOOK_URL not set, skipping Slack notification"
fi

log "Weekly update complete"
