---
description: Show the complete state — shipping, blocked, done, upcoming deadlines.
---

# /organize

## What you do

1. Scan every `projects/*/README.md`
2. Read `context/deadlines.md` and `context/current-priorities.md`
3. Output a single compact dashboard:

```
## SHIPPING
- Project | deadline | next action

## BLOCKED
- Project | blocker | days stuck

## SIDELINED / PAUSED
- Project | status

## UPCOMING DEADLINES (next 30 days)
- Date | Thing | Project

## THIS WEEK'S TOP 3
- From current-priorities.md
```

Keep it scannable. No paragraphs. No filler.

## Rules

- Don't editorialize unless asked
- If a project has been stuck >7 days, flag it with `⚠` (the only exception to the no-emoji rule, and only if needed)
- End output immediately — no "let me know" close
