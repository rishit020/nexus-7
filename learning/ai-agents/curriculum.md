# Applied AI Agents Curriculum

**Owner:** Rishit
**Duration:** 5 weeks (April 19 – May 23, 2026)
**Time commitment:** 10–12 hours/week (lighter during AP exam weeks)
**Cost:** Free
**End goal:** Credible professor outreach in mid-to-late June with a shipped, polished research artifact; foundation for building AI agent startups through high school and college.

---

## Committed Technical Field

**Applied AI agents** — mastering how to build, evaluate, and ship reliable LLM-powered agent systems that reason, use tools, and solve real workflows, with enough depth for research contribution and practical skill for a venture-scale startup over the next 2-3 years.

This curriculum is the execution plan for that commitment.

---

## Table of Contents

1. [The Meta-Framework](#the-meta-framework)
2. [Week 1: Foundations](#week-1-foundations-april-19-25--1012-hours)
3. [Week 2: Core Patterns + Tool Use](#week-2-core-patterns--tool-use-april-26--may-2--1012-hours)
4. [Week 3: Evaluation + Light AP Week](#week-3-evaluation--light-ap-week-may-39--8-hours-max)
5. [Week 4: AP Exam Week](#week-4-ap-exam-week-may-1016--5-hours-max)
6. [Week 5: Post-AP Intensive](#week-5-post-ap-intensive-may-1723--1520-hours)
7. [Core Reading List](#core-reading-list)
8. [Video Courses](#video-courses-in-priority-order)
9. [Ongoing Resources](#ongoing-resources-weekly-rhythm)
10. [What's Excluded](#what-was-deliberately-excluded)
11. [The One Rule](#the-one-rule)

---

## The Meta-Framework

Learning progresses through five stages:

1. **Conceptual foundation** — What agents are and why they work
2. **Core patterns** — The 4 design patterns every agent uses
3. **Tool use and context** — How agents interact with the world
4. **Evaluation** — The skill that separates demos from products (most critical)
5. **Production shipping** — Turning patterns into real applications

Andrew Ng's key insight that guides this curriculum: *"The single biggest predictor of whether someone executes well on agents is their ability to drive a disciplined process for evals and error analysis."*

---

## Week 1: Foundations (April 19-25) — 10-12 hours

**Goal:** Understand what agents are conceptually. Distinguish workflows from agents. Run first simple agent.

### Day 1-2 (Sat-Sun, ~4 hours)

- [ ] **Andrej Karpathy — "Intro to Large Language Models"** (1 hour)
  - Link: https://www.youtube.com/watch?v=zjkBMFhNj_g
  - Watch actively, take notes
- [ ] **Anthropic — "Building Effective Agents"** (1 hour)
  - Link: https://www.anthropic.com/research/building-effective-agents
  - Read twice. Understand workflow vs. agent distinction
- [ ] **Set up environment:**
  - Install Python 3.11+
  - Get Anthropic API key (free tier): https://console.anthropic.com
  - Clone Claude Cookbooks: `git clone https://github.com/anthropics/claude-cookbooks`

### Day 3-4 (Mon-Tue, ~3 hours)

- [ ] **Andrew Ng — "Agentic AI" course, Module 1** (1.5 hours)
  - Link: https://www.deeplearning.ai/courses/agentic-ai/
  - Free to audit. Raw Python, no frameworks
- [ ] **ReAct Paper** (1 hour)
  - Link: https://arxiv.org/abs/2210.03629
  - Read intro, method, experiments. Skip appendix

### Day 5-6 (Wed-Thu, ~3 hours)

- [ ] **Andrew Ng — Module 2 (Reflection pattern)** (1.5 hours)
- [ ] **Anthropic Cookbook — basic_workflows.ipynb** (1 hour)
  - In `patterns/agents` folder. Run every cell
- [ ] **Build:** Simple ReAct loop from scratch in Python using Claude's API
  - One tool: calculator
  - Task: "Find total if I save $350/month for 18 months at 5% annual interest"

### Day 7 (Fri, ~2 hours)

- [ ] **Synthesis:** Write 500-word document answering:
  1. What is an agent?
  2. Difference between workflow and agent?
  3. What did ReAct actually introduce?

### Week 1 Deliverable

Working ReAct agent on laptop with clear comments + synthesis document. Push to GitHub with basic README.

---

## Week 2: Core Patterns + Tool Use (April 26 - May 2) — 10-12 hours

**Goal:** Master the 4 agentic design patterns. Build agents that use tools well.

### Day 1-2 (Sat-Sun, ~4 hours)

- [ ] **Andrew Ng — Module 3 (Tool Use pattern)** (1.5 hours)
- [ ] **Anthropic — "Writing effective tools for AI agents"** (45 min)
  - Link: https://www.anthropic.com/engineering/writing-tools-for-agents
  - Advanced, production-grade. Read slowly
- [ ] **Toolformer paper** (45 min) — skim intro and method only
  - Link: https://arxiv.org/abs/2302.04761
- [ ] **Build:** Extend Week 1 agent with 2-3 more tools (web search, file I/O, API call)

### Day 3-4 (Mon-Tue, ~3 hours)

- [ ] **Andrew Ng — Module 4 (Planning pattern)** (1.5 hours)
- [ ] **Anthropic Cookbook — orchestrator_workers.ipynb + evaluator_optimizer.ipynb** (1.5 hours)
  - Run both, modify for your own task

### Day 5-6 (Wed-Thu, ~3 hours)

- [ ] **Andrew Ng — Module 5 (Multi-Agent pattern)** (1.5 hours)
- [ ] **Reflexion paper** (1 hour)
  - Link: https://arxiv.org/abs/2303.11366
  - How agents learn from failure
- [ ] **Read:** Simon Willison's recent blog posts on agents
  - Link: https://simonwillison.net

### Day 7 (Fri, ~2 hours)

- [ ] **Synthesis:** Update GitHub project with agent using at least 2 design patterns
  - Example: Tool Use + Reflection
  - Document architectural choices

### Week 2 Deliverable

Agent combining at least 2 design patterns. Clean code, documented decisions.

---

## Week 3: Evaluation + Light AP Week (May 3-9) — 8 hours max

**Goal:** Learn evaluation — the most important skill. Protect AP prep.

**STRICT 8-hour cap. Drop more if needed for APs.**

### Day 1 (Sat, 2 hours)

- [ ] **Andrew Ng — Evaluation module** (2 hours)
  - Andrew Ng's explicitly identified most-important differentiator
  - Watch carefully, take detailed notes

### Day 2 (Sun, 2 hours)

- [ ] **Skim SWE-bench paper** (1 hour)
  - Link: https://arxiv.org/abs/2310.06770
  - Gold standard agent benchmark
- [ ] **Skim GAIA paper** (1 hour)
  - Link: https://arxiv.org/abs/2311.12983
  - Understand what makes evaluation hard

### Day 3-5 (Mon-Wed, 2 hours TOTAL across all three)

- [ ] Light reading only: Anthropic blog, Simon Willison, 20-30 min/day max
- [ ] **Study for APs. Seriously.**

### Day 6-7 (Thu-Fri, 2 hours)

- [ ] **Build:** Add eval harness to Week 2 agent
  - 10 test cases with expected outputs
  - Run them, measure pass rate
  - Document failures honestly

### Week 3 Deliverable

Agent project has eval harness and measured pass rate. Plus: strong AP prep.

---

## Week 4: AP Exam Week (May 10-16) — 5 hours max

**Goal:** Survive APs. Minimal momentum. No new learning.

This week is explicitly light. Known weakness is inconsistency mid-project — **not this week**. This week is AP week, full stop.

### Background only (30 min/day max)

- [ ] **The Batch newsletter** — https://www.deeplearning.ai/the-batch — 10 min, 2x a week
- [ ] **Podcast while commuting/exercising:** Latent Space — https://www.latent.space
- [ ] **No new building. Don't touch your code. Don't read papers. Take APs.**

---

## Week 5: Post-AP Intensive (May 17-23) — 15-20 hours

**Goal:** Build capstone project that becomes professor outreach artifact. Everything comes together.

### Capstone Options (pick ONE)

#### Option A — Agent Evaluation Benchmark (research-focused) ⭐ RECOMMENDED

- Pick narrow task domain (e.g., "extracting structured data from unstructured emails")
- Build test set of 30-50 ground-truth examples
- Test 3-5 agent architectures on the task
- Document failure modes systematically
- Publish as GitHub repo with README, methodology, results

**Strongest option for professor outreach.**

#### Option B — Reproducibility Study (research-adjacent)

- Pick recent agent paper with open-source code (ReAct, Reflexion, or smaller workshop paper)
- Reproduce main experiment at small scale
- Document where you couldn't reproduce, what was unclear, what you'd do differently
- Release as GitHub repo with methodology doc

#### Option C — Applied Agent (startup-adjacent)

- Build agent solving real problem in your life (tennis scheduling, AP study planning, paper summarization)
- Ship with proper web UI (Streamlit or FastAPI + basic HTML)
- Get 3 real users (friends, family) to try it
- Add evaluation harness, measure pass rate
- Document publicly

### Daily Breakdown

**Day 1-2 (Sat-Sun, 6 hours):** Scope. Write 1-page spec. Set up repo. Build MVP.

**Day 3-4 (Mon-Tue, 4 hours):** Build evaluation. Measure baseline. Iterate.

**Day 5 (Wed, 3 hours):** Polish. Clean code. Thorough README with methodology, results, limitations.

**Day 6 (Thu, 3 hours):** Record 3-min demo video (Loom is free). Final polish.

**Day 7 (Fri, 2 hours):** Write blog post (can be GitHub wiki) about what you built. This becomes the artifact linked in professor emails.

### Week 5 Deliverable

Finished, polished, public project with methodology, results, blog post. **Research artifact ready for professor outreach in mid-to-late June.**

---

## Core Reading List

### Must-read (do during curriculum)

1. **Anthropic — "Building Effective Agents"** — https://www.anthropic.com/research/building-effective-agents
2. **Anthropic — "Writing effective tools for AI agents"** — https://www.anthropic.com/engineering/writing-tools-for-agents
3. **ReAct** (Yao et al., 2022) — https://arxiv.org/abs/2210.03629
4. **Reflexion** (Shinn et al., 2023) — https://arxiv.org/abs/2303.11366
5. **Toolformer** (Schick et al., 2023) — https://arxiv.org/abs/2302.04761

### Should-skim (during or after)

6. **SWE-bench** — https://arxiv.org/abs/2310.06770
7. **GAIA** — https://arxiv.org/abs/2311.12983
8. **Chain of Thought** (Wei et al., 2022) — https://arxiv.org/abs/2201.11903

### Reference (don't force-read)

9. **Anthropic — Agent Skills** — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
10. **Tree of Thoughts** (Yao et al., 2023) — https://arxiv.org/abs/2305.10601

---

## Video Courses (in priority order)

1. **Andrew Ng's "Agentic AI"** — https://www.deeplearning.ai/courses/agentic-ai/
   - Free to audit. Spine of this curriculum.
2. **Karpathy's "Intro to Large Language Models"** — https://www.youtube.com/watch?v=zjkBMFhNj_g
   - 1 hour. Foundational primer.
3. **Karpathy "Zero to Hero"** — https://karpathy.ai/zero-to-hero.html
   - Optional deep-dive. Not required for this curriculum.

---

## Ongoing Resources (weekly rhythm)

Set up continuous learning inputs:

- **Anthropic Blog** — https://www.anthropic.com/news — weekly check
- **The Batch** (Andrew Ng) — https://www.deeplearning.ai/the-batch — 2x weekly
- **Latent Space Podcast** — https://www.latent.space — 1 episode/week
- **Simon Willison's blog** — https://simonwillison.net — 2x weekly
- **Hugging Face Daily Papers** — https://huggingface.co/papers — weekly skim

---

## What Was Deliberately Excluded

Curated choices, not a dump:

- **Hugging Face Agents Course** — Overlaps with Andrew Ng's. Andrew Ng's is more rigorous. Pick one.
- **LangChain-specific tutorials** — Start framework-free to understand fundamentals. Add frameworks later.
- **CrewAI, AutoGen, LlamaIndex** — Framework-specific. Concepts first, framework later based on need.
- **IBM/Coursera specializations** — Solid but less focused.
- **Paid bootcamps** — Free only. Not necessary even with budget.
- **Training models from scratch** — Not needed for applied agents. Karpathy's Zero to Hero if interested later.

---

## The One Rule

**Ship every week.** Every week ends with a GitHub commit. Not a tutorial watched, not a paper read — something built and pushed.

This protects against known failure modes (broad instead of deep, inconsistent mid-project).

If a week ends with nothing on GitHub, that week failed, regardless of videos watched.

---

## Post-Curriculum: June Outreach Plan

After Week 5, the curriculum ends and outreach begins:

### Mid-June (June 15-21)
- Finalize outreach targets: Dongkuan Xu (NC State, GIC Lab — primary target), Yuchen Liu, Xiaorui Liu at NC State + 2 Duke targets
- Deep-dive on 2-3 most recent papers from each target
- Draft 5 cold emails (under 200 words each)

### Late June (June 22-30)
- Send 1 email per weekday referencing specific papers
- Include GitHub link to capstone artifact
- Specific question or concrete contribution offer per email

---

## Checkpoint Gates

### Day 30 (mid-May)
- Working agent shipped? YES/NO
- If NO: diagnose (not enough hours, wrong vertical, tutorial hell?)

### Day 60 (mid-June)
- Capstone artifact complete and public?
- Evaluation methodology documented with numbers?

### Day 90 (mid-July)
- Professor response received?
- If zero responses: second outreach batch with refined targeting

---

*Committed: April 18, 2026*
