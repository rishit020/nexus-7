---
name: capture
description: Instantly log any thought, idea, lead, task, or link to context/inbox.md without breaking flow. No analysis, no questions, just log and confirm in one line.
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Capture

## Purpose
Zero-friction logging. Rishit has a thought -> it's saved -> back to work.
Do not analyze. Do not expand. Do not ask questions. Log and confirm.

## When to run
- "remember this"
- "log this"
- "note that"
- "save this"
- "don't let me forget X"
- Any short statement that sounds like something to capture

## Process
1. timestamp=$(date +"%Y-%m-%d %H:%M")
2. Auto-detect TYPE:
   URL -> link
   name/username/platform -> lead
   "decide" / "decided" / "going with" -> decision
   "idea for" / "what if" -> idea
   verb + deadline / "need to" / "should" -> task
   everything else -> thought

3. Append to context/inbox.md:
   [timestamp] | TYPE: [type] | [content exactly as given]

4. count=$(grep -c "^[0-9]" context/inbox.md 2>/dev/null || echo 1)
5. Reply ONLY: "got it. [count] in inbox."

Nothing else.

## Phase 2 note
This same logic becomes the Telegram voice note classifier.
