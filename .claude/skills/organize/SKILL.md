---
name: organize
description: Process everything in context/inbox.md. Triage each item to the right file — tasks to backlog, leads to data/leads.md, ideas to projects, decisions to decisions log. Report what moved where.
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Organize

## Purpose
Clear the inbox. Everything in the right place. Rishit stays focused.

## When to run
- "organize my inbox"
- "process my notes"
- "clean things up"
- "what's in my inbox"
- Weekly when inbox has 10+ items

## Process each entry in context/inbox.md

TYPE=task -> append to tasks/backlog.md
  Format: [DATE] | [task] | PRIORITY: [high/medium/low based on goals alignment]

TYPE=lead -> create record in data/leads.md
  Fill in fields from the captured context. Mark status: new.

TYPE=idea -> if Tide-related: append to projects/tide/README.md under Ideas
           if other: create entry in projects/ or note in context/inbox.md

TYPE=decision -> create record in data/decisions.md
                AND append to decisions/log.md

TYPE=link -> append to relevant project README or context file

TYPE=thought -> if it reveals a pattern: append to context/patterns.md
               otherwise: keep in inbox with [REVIEWED] tag

After processing each entry, append [PROCESSED: DATE] to the entry.

## Final report
  organized [X] items:
  [X] tasks -> tasks/backlog.md
  [X] leads -> data/leads.md
  [X] ideas -> [destinations]
  [X] decisions -> data/decisions.md
  [X] other -> [destinations]
