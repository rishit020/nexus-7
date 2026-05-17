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

LAST_UPDATED: 2026-05-17
