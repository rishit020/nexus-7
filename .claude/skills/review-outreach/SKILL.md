---
name: review-outreach
description: Show Rishit all pending outreach drafts for review and approval. He approves, edits, or kills each one. Approved drafts get queued. Nothing sends without his sign-off.
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Review Outreach

## Purpose
Rishit approves every outreach message before it goes out. This skill
surfaces everything pending, one at a time, and gets his decision.

## When to run
- When Rishit says "show me drafts", "what needs review", "review outreach",
  "what did you write", "show me what you found", "let me see the messages"

## Step 1 — Load pending drafts
Read data/outreach.md. Find all records with status: pending-review.
Count them.

If none: "nothing pending review. run monitor to find new leads."

## Step 2 — Show one at a time
For each pending record:

  ----------------------------------
  OUTREACH DRAFT [O-XXX] -- [platform]
  LEAD: [username] on [platform]
  THEIR PAIN: "[pain quote]"
  ----------------------------------
  DM VARIANT:
  [draft text]
  ----------------------------------
  COMMENT VARIANT:
  [draft text]
  ----------------------------------
  [X] more drafts after this one.
  approve dm / approve comment / edit / kill it

Wait for response before showing next draft.

## Step 3 — Handle response
"approve dm" or "approve comment":
  -> update record status to: approved
  -> update lead status in data/leads.md to: contacted
  -> append to context/patterns.md: what was approved and why it landed
  -> confirm: "approved. [X] remaining."

"edit [new text]":
  -> update draft_text with edit
  -> set status: approved
  -> append to context/patterns.md: what was changed and why
  -> confirm: "updated and approved."

"kill it":
  -> set status: rejected
  -> append to context/patterns.md: what didn't land
  -> confirm: "killed. [X] remaining."

Any other input:
  -> treat as an edit, incorporate it, confirm

## Step 4 — When all reviewed
  "all [X] drafts reviewed. [X] approved, [X] killed.
   approved messages are in your outreach queue.
   send them manually on [platform] — i'll track who you've reached out to."
