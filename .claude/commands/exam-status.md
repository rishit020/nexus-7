---
description: AP exam prep status — subjects, schedule, weeks remaining.
---

# /exam-status

## What you do

1. Read `learning/ap-exams/study-schedule.md` and `learning/ap-exams/progress.md`
2. Read `context/deadlines.md` for exam dates
3. Output:

```
## AP EXAM STATUS

Weeks until May exams: X

### Calc BC
- Hours this week: __
- Status: on track / behind / urgent

### AP CS
- Hours this week: __
- Status: ...

### Gov
- Hours this week: __
- Status: ...

### Verdict
[One sentence: are you on track to crush these, or do you need to change something?]
```

## Rules

- If weekly hours = 0, say "behind" without softening
- If exam is <4 weeks out and hours are low, mark "urgent"
- Don't suggest a fix unless asked — just report status
