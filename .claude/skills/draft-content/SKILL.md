---
name: draft-content
description: Draft Reddit posts, tweets, HN posts, or any content for Tide distribution or Rishit's personal brand. Always reads voice.md and communities.md first. Never posts directly — shows Rishit for approval first.
allowed-tools: Read, Write, Bash
disable-model-invocation: false
---

# Draft Content

## Purpose
Write platform-native content that actually performs. Sounds like Rishit,
fits the community, moves Tide forward.

## When to run
- "write a post about X"
- "draft something for reddit"
- "i want to post about Y"
- "make content about Z"
- "tweet about this"

## Step 1 — Load context
Read context/voice.md — full file.
Read context/communities.md — find right community for goal.
Read context/work.md — Tide positioning.

## Step 2 — Understand the goal
Parse from natural language:
- What platform?
- What is the goal (find users, validate idea, build audience, share insight)?
- Any specific angle mentioned?

If unclear, ask one question: "what's the goal of this post?"

## Step 3 — Draft
Apply ALL platform rules from voice.md.
Apply WHAT PERFORMS and WHAT GETS YOU BANNED from communities.md.

For Reddit:
  - Title: specific, no clickbait, fits subreddit tone
  - Body: hook in line 1, conversational, no wall of text
  - Write title and body separately

For Twitter: 280 char max or thread
For HN Show HN: "Show HN: [product] -- [plain English description]"

Output:

  PLATFORM: [platform]
  COMMUNITY: [where and why]

  TITLE:
  [title]

  BODY:
  [full post]

  RISK FLAGS:
  [anything that could get this removed or backfire]

## Step 4 — Approval
Print: "approve it, edit it, or kill it."

approve -> save to data/posts.md with status: approved, confirm with ID
edit -> incorporate, save approved
kill -> save rejected, log what didn't land in context/patterns.md

NEVER post directly. Queue only.
Phase 2 adds direct posting via API.
