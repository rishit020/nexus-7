"""Canvas API fetcher. Pulls upcoming assignments across active courses."""
import os
import sys
from datetime import datetime, timezone
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ["CANVAS_BASE_URL"].rstrip("/")
TOKEN = os.environ["CANVAS_TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_active_courses():
    url = f"{BASE_URL}/api/v1/courses"
    params = {"enrollment_state": "active", "per_page": 100}
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def get_assignments(course_id):
    url = f"{BASE_URL}/api/v1/courses/{course_id}/assignments"
    params = {"per_page": 100, "order_by": "due_at", "bucket": "upcoming"}
    r = requests.get(url, headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_all():
    courses = get_active_courses()
    out = []
    for c in courses:
        cid = c.get("id")
        cname = c.get("name", f"course-{cid}")
        try:
            assigns = get_assignments(cid)
        except requests.HTTPError as e:
            print(f"WARN: could not fetch assignments for {cname}: {e}", file=sys.stderr)
            continue
        for a in assigns:
            a["_course_name"] = cname
            out.append(a)
    return out


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    items = fetch_all()
    print(f"Fetched {len(items)} raw items from Canvas.")
    if dry:
        for a in items:
            due = a.get("due_at") or "no-due-date"
            print(f"  [{a['_course_name']}] {a.get('name')} — due {due} — types={a.get('submission_types')}")
