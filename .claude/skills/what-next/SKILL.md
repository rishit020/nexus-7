---
name: what-next
description: Reads all context and data, applies a strict priority framework, returns the single most important thing Rishit should do right now with brief reasoning. One answer only.
allowed-tools: Read, Bash
disable-model-invocation: false
---

# What Next

## Purpose
When Rishit is stuck, context-switching, or just opening a session --
answer: what should I actually be doing right now?
One answer. Brief reason. No options.

## When to run
- "what should i do"
- "what do i work on"
- "i don't know what to do"
- "what's most important"
- "what next"

## Decision framework (strict order)

1. Hard deadline within 24 hours? -> That. Nothing else.
2. Hard deadline within 72 hours? -> That with urgency flag.
3. Approved outreach in queue not yet sent?
   -> "send those messages -- they're already written, just need to go out"
4. Pending outreach drafts waiting for review?
   -> "review and approve the drafts i wrote"
5. current-priorities.md has a clear incomplete next step?
   -> That step exactly.
6. Leads found but no outreach drafted?
   -> Draft outreach for top lead.
7. No leads in pipeline?
   -> Run community monitor to find new leads.
8. Critically stale context file (>7 days past refresh)?
   -> Update it. Stale context makes everything worse.
9. No signal from any of the above?
   -> "talk to someone. find a potential tide user and have a real conversation."

## Output (no options, no lists)

  +-------------------------------------+
  | DO THIS NOW                         |
  +-------------------------------------+
  | [specific action, max 12 words]     |
  | because: [one sentence]             |
  | after: [what comes next]            |
  +-------------------------------------+
