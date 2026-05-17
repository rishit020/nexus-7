---
name: daily-brief
description: Proactive daily brief that tells Rishit what to focus on, what's in the pipeline, and what the agent has been doing. Runs when Rishit opens a session or asks what's going on.
allowed-tools: Read, Bash
disable-model-invocation: false
---

# Daily Brief

## Purpose
Replace "what should I do today" with a brief that already has the answer.
Rishit should never have to ask -- this surfaces automatically.

## When to run
- When Rishit opens a new session (auto-trigger via SessionStart hook)
- When Rishit says "what's going on", "brief me", "catch me up",
  "what do i have today", "what should i focus on"

## Data sources
1. context/current-priorities.md -> the one thing
2. context/deadlines.md -> anything due in 48 hours
3. tasks/today.md -> today's tasks if they exist
4. data/outreach.md -> count approved (queued to send) + pending review
5. data/leads.md -> count new uncontacted leads
6. context/last-updated.md -> stale files

Get today: date=$(date +"%A, %B %d")

## Output format

  ======================================
  [DAY, MONTH DATE]
  ======================================
  FOCUS:      [from current-priorities -- max 10 words]
  DUE SOON:   [48hr deadlines or "nothing critical"]
  --------------------------------------
  TIDE:
    leads found:      [total in pipeline]
    needs your review:[pending-review count in outreach]
    ready to send:    [approved count in outreach]
    posts queued:     [approved in posts]
  --------------------------------------
  [if stale files exist]: STALE: [file list]
  ======================================
  [ONE sentence on what to do first -- derived from what-next logic]

## Motivational close
End every brief with one short, direct motivational line.
Not generic. Based on where Tide actually stands.
Example: "3 people are waiting to talk to you. go message them."
Example: "you haven't shipped anything yet. that changes today."
Rotate -- never repeat the same line twice in a row.
