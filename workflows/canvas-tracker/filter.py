"""Filter Canvas items to assignments only. Drops quizzes, tests, discussions."""

EXCLUDED_SUBMISSION_TYPES = {
    "online_quiz",          # quizzes
    "discussion_topic",     # discussion posts
    "external_tool",        # often proctored test tools (Edulastic, etc.) — conservative exclude
    "none",                 # no submission = usually not an actionable assignment
    "not_graded",
}

EXCLUDED_NAME_KEYWORDS = (
    "quiz",
    "test",
    "exam",
    "midterm",
    "final",
    "discussion",
)


def is_assignment(item):
    """True if this item is a real submittable assignment, not a quiz/test/discussion."""
    # Explicit quiz field on the API
    if item.get("is_quiz_assignment"):
        return False
    if item.get("quiz_id"):
        return False

    name = (item.get("name") or "").lower()
    for kw in EXCLUDED_NAME_KEYWORDS:
        if kw in name:
            return False

    sub_types = set(item.get("submission_types") or [])
    if sub_types & EXCLUDED_SUBMISSION_TYPES:
        # If ONLY excluded types, drop. If it has online_upload etc. alongside, keep.
        if not (sub_types - EXCLUDED_SUBMISSION_TYPES):
            return False

    # Must have a due date to be actionable
    if not item.get("due_at"):
        return False

    return True


def filter_items(items):
    return [i for i in items if is_assignment(i)]


if __name__ == "__main__":
    import sys
    from fetch import fetch_all
    raw = fetch_all()
    kept = filter_items(raw)
    print(f"Kept {len(kept)} of {len(raw)} items after filtering.")
    for a in kept:
        print(f"  [{a['_course_name']}] {a.get('name')} — due {a.get('due_at')}")
