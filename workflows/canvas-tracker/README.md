# Canvas Tracker

Pulls assignments from Canvas and drops them into `tasks/backlog.md`. Filters out quizzes, tests, discussions. Prints a morning digest.

## Why It Exists

School assignments fall through the cracks. Canvas has notifications but they get ignored. This workflow forces assignments into `tasks/backlog.md`, which is already part of the daily workflow. No notification fatigue, just a clean inbox append.

## What It Does

1. Hits the Canvas REST API with a personal access token.
2. Pulls upcoming assignments across all active courses.
3. Filters to assignments only (excludes quizzes, tests, discussion posts).
4. Dedupes against existing entries in `tasks/backlog.md`.
5. Appends new items in the existing backlog format.
6. Prints one-line digest: "Due today: X. Due this week: Y. Overdue: Z."

## Setup (One-Time)

### 1. Get a Canvas access token
- Log in to Canvas (https://wcpss.instructure.com)
- Account → Settings → Approved Integrations → "+ New Access Token"
- Name it "NEXUS-7 canvas-tracker", no expiry, save the token

### 2. Configure
```bash
cd workflows/canvas-tracker
cp config.example.env .env
# edit .env and paste your token + your Canvas base URL
```

### 3. Install deps
```bash
pip install requests python-dotenv
```

### 4. Test (dry run)
```bash
python fetch.py --dry-run
```
Verify output looks right (assignments listed, no quizzes/tests).

### 5. Live run
```bash
./run.sh
```

### 6. Schedule (optional)
Daily 7am cron:
```bash
crontab -e
# add:
0 7 * * * cd /Users/rishits/NEXUS-7/workflows/canvas-tracker && ./run.sh >> run.log 2>&1
```

## Files

- `fetch.py` — Canvas API calls, returns raw assignments
- `filter.py` — drops quizzes/tests/discussions
- `digest.py` — writes to backlog, prints digest
- `run.sh` — entrypoint
- `config.example.env` — template (the real `.env` is gitignored)

## What v1 Does NOT Do

- No email, no SMS, no Slack. Intentionally.
- No reminder tree (24hr/2hr/1hr). Morning digest only.
- No auto-cron install — you run `crontab -e` yourself.
- No priority scoring. Due date sorts everything.

If any of these become real needs (not nice-to-haves), add them in v2.
