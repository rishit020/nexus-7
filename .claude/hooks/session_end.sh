#!/bin/bash
# Fires when Claude Code session terminates
# Logs session end

TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
PROJECT="${CLAUDE_PROJECT_DIR}"

echo "session_end: ${TIMESTAMP}" >> "${PROJECT}/data/agent-log.md" 2>/dev/null

exit 0
