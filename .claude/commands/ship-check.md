---
description: Can I ship [project] on time? Brutal verdict.
argument-hint: [project-name]
---

# /ship-check

## Usage

```
/ship-check tennis-cv-app
/ship-check fryars-gate-hoa
```

## What you do

1. Read `projects/$ARGUMENTS/README.md`
2. Read `context/deadlines.md` for the deadline
3. Compute days remaining
4. Read progress log to gauge velocity
5. Output verdict:

```
## SHIP CHECK: [project]

Deadline: [date] ([X days remaining])
Current status: [from README]
Velocity: [recent progress log entries, condensed]

### Verdict
[ON TRACK | AT RISK | WON'T MAKE IT]

[2-3 sentences. If on track: what to keep doing. If at risk: specific fix. If won't make it: what to cut or push.]
```

## Rules

- Be brutal. Do not soften "won't make it" with hedging.
- "At risk" must come with a specific action that flips it to on track
- Don't suggest scope cuts unless verdict is at-risk or worse
- If the project has no recent progress entries, velocity = 0 and that's a red flag itself
