---
description: Professor outreach status. Flags overdue follow-ups.
---

# /relationship-status

## What you do

1. Read `projects/professor-outreach/README.md`
2. For each open opportunity, compute days since their last reply
3. Output:

```
## PROFESSOR OUTREACH

### Active conversations
- Dr. [Name] ([institution]) — replied [date] — our response: [status] — [days overdue if any]

### Next targets
- [list]

### Stats
- Emailed: X / 15
- Replied: X
- Real conversations: X

### Verdict
[Flag any overdue follow-up. One sentence.]
```

## Rules

- Reply overdue = >3 days since their response
- If anyone is >3 days overdue, lead with that — don't bury it
- Goal metric is "real conversations," not "emails sent"
