#!/bin/bash
#
# Weekly Rare Earth Literature Update via Claude Code
# Runs the /literature-update command in non-interactive mode
#
# Usage:
#   ./scripts/claude_weekly_update.sh           # Default 7 days
#   ./scripts/claude_weekly_update.sh 14        # Custom days
#   ./scripts/claude_weekly_update.sh --no-push # Skip git push
#

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_FILE="$PROJECT_DIR/logs/claude_update.log"

# Parse arguments
DAYS=${1:-7}
NO_PUSH=false

for arg in "$@"; do
    case $arg in
        --no-push)
            NO_PUSH=true
            ;;
        [0-9]*)
            DAYS=$arg
            ;;
    esac
done

# Create logs directory if needed
mkdir -p "$PROJECT_DIR/logs"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Starting Claude Code literature update (last $DAYS days)"

cd "$PROJECT_DIR"

# Load environment variables (for Slack webhook, etc.)
if [ -f "$PROJECT_DIR/.env" ]; then
    export $(grep -v '^#' "$PROJECT_DIR/.env" | xargs)
fi

# Build the prompt based on options
if [ "$NO_PUSH" = true ]; then
    PROMPT="/literature-update --days $DAYS"
else
    PROMPT="/literature-update --days $DAYS then commit the report to GitHub, push it, and send Slack notification"
fi

log "Running: claude -p \"$PROMPT\""

# Run Claude Code in non-interactive mode
claude -p "$PROMPT" --dangerously-skip-permissions >> "$LOG_FILE" 2>&1

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    log "Literature update completed successfully"
else
    log "Literature update failed with exit code $EXIT_CODE"
fi

exit $EXIT_CODE
