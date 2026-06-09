# AGENT LEARNING LOG

How NEXUS-7 gets smarter over time. Agent appends here automatically.
Never edit manually unless correcting a wrong entry.

Format:
[DATE] | TYPE: [voice/behavior/outreach/mistake/preference]
OBSERVED: [what happened]
IMPLICATION: [how agent adjusts going forward]

---
TRIGGERS FOR AUTO-APPEND:
- Rishit rewrites a draft → log what changed, update voice.md if pattern repeats 3x
- Rishit says "that was good" → log what it was, do more of it
- Rishit says "no not that" or dismisses something → log it, never repeat
- An outreach message gets a reply → log the angle, weight it higher
- An outreach message gets ignored → log what didn't land
- Rishit skips the same suggestion 3+ sessions → stop making it
- Rishit says "remember that X" → immediately append, confirm logged
- End of every session → append one observation about the session
- Agent makes a mistake → log it with "NEVER REPEAT" tag

[entries append here]

2026-05-17 | TYPE: behavior
OBSERVED: Rishit DM'd Stingwave24, GillesCode, Distinct_Laugh_5808 based on agent's email parse. Skipped LeaderAtLeading — "wastage of time."
IMPLICATION: Commentary-style replies (analysis, takes) = lower priority. Personal pain stories = pursue. People describing their own struggle > people offering hot takes.

2026-05-17 | TYPE: behavior
OBSERVED: Rishit explicitly said to own the full Reddit workflow — parse emails, find leads, draft DMs, find posts to comment on. He reviews and approves, not does the legwork.
IMPLICATION: Every session: check Gmail for Reddit + F5Bot signals. Parse, rank, draft. Bring action items not raw data.

2026-05-17 | TYPE: outreach
OBSERVED: "vibe coded" F5Bot keyword hit 50/day limit — nearly all hits were garbage. Signal keywords: "launched my saas", "distribution problem", "shouting into the void."
IMPLICATION: Recommend tightening or killing "vibe coded" keyword. High-signal keywords get weighted higher in parsing.

2026-05-17 | TYPE: mistake — NEVER REPEAT
OBSERVED: r/SaaS and r/indiehackers auto-removed Rishit's posts via AutoModerator.
IMPLICATION: Before posting to any new subreddit, check the rules. r/SaaS flags low-effort/AI content. r/indiehackers is strict. Research first, draft accordingly.

2026-05-18 | TYPE: mistake — NEVER REPEAT
OBSERVED: Em dashes appeared in O-049 and O-050 DM drafts. Caught post-draft both times, fixed before Rishit sends. Pattern is the agent generating them naturally in flowing sentences.
IMPLICATION: Before finalizing any DM or comment draft, scan explicitly for the — character. Never use em dashes in outreach copy. Replace with a period or restructure the sentence.

LAST_UPDATED: 2026-05-18

2026-05-23 | TYPE: mistake — NEVER REPEAT
OBSERVED: Em dashes appeared in O-125 and O-126 DM drafts (third occurrence). Pattern: em dashes slip in when writing "saw your post in X — [detail]" sentence structure. Caught post-commit, fixed before Rishit could copy them, but Telegram was already sent with the em-dash version.
IMPLICATION: Any sentence of the form "saw X in Y — [detail]" must be rewritten. Use a period instead: "saw X in Y. [detail]." Always scan every character before finalizing any DM. This is a persistent generation habit that requires explicit checking every single time.

2026-05-31 | TYPE: content
OBSERVED: GrandFit6072's r/vibecoding post "I talked to 40+ founders about what happens after they launch. Here's the pattern I keep seeing." got -3 points and 4 comments. Community rejected it.
IMPLICATION: r/vibecoding doesn't respond to "researcher sharing findings" framing. Community wants peers, not analysts. Future posts there should be first-person builder perspective, not summary/research style. The ICP lives in this sub but the content angle has to match the energy.

2026-06-09 | TYPE: mistake — NEVER REPEAT
OBSERVED: First Gmail subagent in Run 233 hallucinated 3 fictional thread IDs and 3 fictional leads (Local_Loan_9890/r/micro_saas, Minute_Estimate_4418/r/GrowthHacking, Vaprolol/r/SaasDevelopers). Presented them with specific timestamps and quoted post text as if real. Second independent subagent confirmed none of these thread IDs exist in Gmail.
IMPLICATION: Never log a new lead based on a single subagent's Gmail parse. Always cross-verify with a second independent subagent before logging. Subagents hallucinate plausible-sounding Reddit usernames and thread IDs when they can't find real signals. The hallucinations are indistinguishable from real signals without independent verification.

2026-06-09 | TYPE: mistake — NEVER REPEAT
OBSERVED: Run 236 subagent reported Dapper-Turn-3021 (already L-243, logged Run 220) and Left-Importance-8859 (already DISCARDED Run 220 as advisor commenter) as new qualifying leads. Wrote them to leads.md and outreach.md as L-246/L-247 before the main agent caught it via monitor-state cross-check.
IMPLICATION: Before accepting ANY subagent lead report, grep monitor-state.md for every username. If a username already appears in any note_NNN entry, do not log it again regardless of what the subagent says. The hallucination pattern is: subagent re-surfaces already-processed F5Bot emails and presents them as new discoveries.
