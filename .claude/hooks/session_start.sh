#!/bin/bash
# Fires every time Claude Code opens or resumes a session
# Injects stale-file warnings into Claude's context

DATE=$(date +"%Y-%m-%d")
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
PROJECT="${CLAUDE_PROJECT_DIR}"

# Log session start
echo "" >> "${PROJECT}/data/agent-log.md" 2>/dev/null
grep -q "session_start.*${DATE}" "${PROJECT}/data/agent-log.md" 2>/dev/null || \
  echo "session_start: ${TIMESTAMP}" >> "${PROJECT}/data/agent-log.md"

# Check for stale files -- stdout goes to Claude's context
if [ -f "${PROJECT}/context/last-updated.md" ]; then
  STALE=$(awk -v today="${DATE}" '
    /^context\// {
      n = split($0, f, /[[:space:]]*\|[[:space:]]*/);
      if (n >= 3 && f[3] != "never" && f[3] < today) {
        print "  " f[1] " (overdue since " f[3] ")"
      }
    }
  ' "${PROJECT}/context/last-updated.md")

  if [ -n "$STALE" ]; then
    echo "STALE CONTEXT -- flag these before starting work:"
    echo "$STALE"
    echo ""
  fi
fi

# Check for pending outreach
if [ -f "${PROJECT}/data/outreach.md" ]; then
  PENDING=$(grep -c "status: pending-review" "${PROJECT}/data/outreach.md" 2>/dev/null || echo 0)
  APPROVED=$(grep -c "status: approved" "${PROJECT}/data/outreach.md" 2>/dev/null || echo 0)
  if [ "$PENDING" -gt 0 ] || [ "$APPROVED" -gt 0 ]; then
    echo "OUTREACH: ${PENDING} drafts need review, ${APPROVED} approved and ready to send"
    echo ""
  fi
fi

exit 0
