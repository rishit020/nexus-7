"""Append filtered assignments to tasks/backlog.md, print morning digest."""
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv

from fetch import fetch_all
from filter import filter_items

load_dotenv()

BACKLOG_PATH = Path(os.environ.get("BACKLOG_PATH", "../../tasks/backlog.md")).resolve()


def fmt_backlog_line(item, added_date):
    """Match existing format: [YYYY-MM-DD added] TASK: ... | DEADLINE: ... | PROJECT: school"""
    course = item["_course_name"]
    name = item.get("name", "").strip()
    due = item.get("due_at", "")
    # Canvas dates are ISO 8601 UTC. Strip to date for readability.
    try:
        due_dt = datetime.fromisoformat(due.replace("Z", "+00:00"))
        due_str = due_dt.astimezone().strftime("%Y-%m-%d")
    except Exception:
        due_str = due or "unknown"
    task_str = f"{course}: {name}"
    return f"[{added_date} added] TASK: {task_str} | DEADLINE: {due_str} | PROJECT: school"


def load_existing_backlog():
    if not BACKLOG_PATH.exists():
        return ""
    return BACKLOG_PATH.read_text()


def already_logged(item, existing_text):
    """Dedupe on course+name+due_date signature."""
    name = (item.get("name") or "").strip()
    course = item["_course_name"]
    sig = f"{course}: {name}"
    return sig in existing_text


def bucket_counts(items):
    now = datetime.now(timezone.utc)
    today = now.date()
    week_end = today + timedelta(days=7)
    due_today = 0
    due_week = 0
    overdue = 0
    for a in items:
        try:
            due = datetime.fromisoformat(a["due_at"].replace("Z", "+00:00"))
        except Exception:
            continue
        d = due.date()
        if d < today:
            overdue += 1
        elif d == today:
            due_today += 1
        elif d <= week_end:
            due_week += 1
    return due_today, due_week, overdue


def append_new_items(new_lines):
    text = BACKLOG_PATH.read_text() if BACKLOG_PATH.exists() else ""
    if text and not text.endswith("\n"):
        text += "\n"
    text += "\n".join(new_lines) + "\n"
    BACKLOG_PATH.write_text(text)


def main():
    dry = "--dry-run" in sys.argv
    raw = fetch_all()
    kept = filter_items(raw)
    existing = load_existing_backlog()
    today_str = datetime.now().strftime("%Y-%m-%d")

    new_items = [a for a in kept if not already_logged(a, existing)]
    new_lines = [fmt_backlog_line(a, today_str) for a in new_items]

    today_n, week_n, overdue_n = bucket_counts(kept)
    print(f"Digest for {today_str}")
    print(f"  Due today: {today_n}")
    print(f"  Due this week: {week_n}")
    print(f"  Overdue: {overdue_n}")
    print(f"  New items to add to backlog: {len(new_items)}")

    if new_items:
        if dry:
            print("(dry-run) would append:")
            for l in new_lines:
                print(f"  {l}")
        else:
            append_new_items(new_lines)
            print(f"Appended {len(new_items)} items to {BACKLOG_PATH}")


if __name__ == "__main__":
    main()
