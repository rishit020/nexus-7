---
name: monitor-communities
description: Continuously monitor Reddit, HN, and Discord communities for posts from potential Tide users in pain about distribution or launch traction. Flag them, draft responses, notify Rishit.
allowed-tools: Read, Write, WebSearch, WebFetch, Bash
disable-model-invocation: false
---

# Monitor Communities

## Purpose
This is the core autonomous skill. Rishit should not have to go read
Reddit to find leads. This skill does it for him, flags what matters,
drafts responses, and reports back.

## Step 1 — Load context
Read context/communities.md — all communities, their pain quotes, fit rating.
Read context/voice.md — needed for drafting responses.
Read context/work.md — ICP definition and pain language.

## Step 2 — Search all HIGH and MEDIUM fit communities

For Reddit (JSON API):
  URL: https://www.reddit.com/r/{sub}/search.json?q={query}&sort=new&limit=25&t=week

Subreddits: indiehackers, SideProject, solopreneur, webdev, startups

Queries per subreddit:
  "no traction" launch
  "shouting into the void"
  "nobody saw my launch"
  "0 upvotes" launched
  "crickets" launched
  "built it" "no users"
  "failed launch"
  "post launch" distribution

For HN:
  https://hn.algolia.com/api/v1/search?query={query}&tags=show_hn&hitsPerPage=20
  Queries: "no traction", "crickets", "nobody saw", "failed to get users"

Rate limit handling: if 429, wait 15s, retry once, skip and continue.

## Step 3 — Qualify
For each result check:
- Pain matches Tide ICP (built something, can't distribute)?
- Posted within last 7 days?
- Not already in data/leads.md? (check: grep username data/leads.md)
- Not already contacted? (check: grep username data/outreach.md)

## Step 4 — For each qualified lead
1. Create record in data/leads.md with next sequential ID
2. Auto-draft a response using context/voice.md rules
   - DM variant (4 sentences max, opens with their situation)
   - Comment variant (shorter, adds value, doesn't mention Tide)
3. Save draft to data/outreach.md with status: pending-review

## Step 5 — Report to Rishit
Output a notification:

  MONITOR REPORT -- [DATE]
  --------------------------
  NEW LEADS FOUND: [X]
  DRAFTS READY FOR REVIEW: [X]

  TOP LEADS:
  [username] -- r/[sub] -- "[pain quote]"
  [username] -- r/[sub] -- "[pain quote]"
  [username] -- r/[sub] -- "[pain quote]"

  Say "review outreach" to see drafts and approve them.
  --------------------------

## When to run
- When Rishit says anything like "find leads", "check reddit",
  "anyone posting about distribution", "what's going on out there",
  "find me someone to talk to"
- Proactively surface if it has been more than 24 hours since last run
  (check data/agent-log.md for last monitor run timestamp)
