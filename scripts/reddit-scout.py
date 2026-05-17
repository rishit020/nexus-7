#!/usr/bin/env python3
"""
NEXUS-7 Reddit Scout — runs every 10 minutes via launchd
Finds posts matching Tide ICP pain signals, sends Telegram with link + draft text.
Rishit goes in and pastes the comment or DM. That's it.
"""

import urllib.request
import urllib.parse
import json
import time
import os
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────
TELEGRAM_TOKEN  = "8701467843:AAECR1h7Ro6yHjX1vUBu_lG7rCQ3YswnFM0"
TELEGRAM_CHAT_ID = "8383354309"
STATE_FILE      = os.path.expanduser("~/NEXUS-7/data/scout-seen.json")
LOG_FILE        = os.path.expanduser("~/NEXUS-7/data/scout-log.txt")

SUBREDDITS = [
    "buildinpublic",   # lenient, good ICP
    "SideProject",     # lenient, good ICP
    "nocode",          # lenient, vibe coders
    "vibecoding",      # lenient, vibe coders
    "solopreneur",     # medium karma req
    "indiehackers",    # stricter — include anyway, good signal
    "SaaS",            # stricter — include anyway, great signal
]

# Posts older than this are skipped (seconds). 45 min window catches anything
# posted between runs without going too far back.
MAX_AGE_SECONDS = 2700  # 45 minutes

# Already contacted — never draft for these
ALREADY_CONTACTED = {
    "stingwave24", "gillescode", "distinct_laugh_5808",
    "initialstudent9000", "ollyconscious", "leaderatleading",
    "automoderator",
}

# ── Keyword signals ────────────────────────────────────────────────────────────
# Each entry: (required_phrases, boost_phrases)
# A post matches if ANY required_phrase is found in title+body (lowercase)
PAIN_SIGNALS = [
    (["no traction"],           ["launch", "built", "shipped", "saas"]),
    (["zero traction"],         []),
    (["no users"],              ["launch", "built", "months"]),
    (["0 users"],               []),
    (["can't get users"],       []),
    (["cannot get users"],      []),
    (["getting users"],         ["struggling", "hard", "help", "how"]),
    (["no audience"],           ["launch", "built", "shipped"]),
    (["without an audience"],   []),
    (["shouting into the void"], []),
    (["launched", "crickets"],  []),
    (["launched", "nothing"],   ["users", "traffic", "traction"]),
    (["launched", "nobody"],    []),
    (["launched", "no one"],    []),
    (["built", "struggling"],   ["users", "traffic", "distribution"]),
    (["distribution"],          ["hard", "struggle", "problem", "help", "killing", "difficult"]),
    (["how do i get users"],    []),
    (["how do i get traffic"],  []),
    (["how to get users"],      []),
    (["how to get traffic"],    []),
    (["first users"],           ["how", "struggling", "help", "where"]),
    (["post-launch"],           ["struggle", "hard", "help", "users"]),
    (["i just launched"],       ["users", "traffic", "audience", "traction"]),
    (["just launched"],         ["no users", "no traffic", "help", "struggling"]),
]

# Comment is safe in these subreddits (lenient automod, low karma OK)
COMMENT_SAFE_SUBS = {"buildinpublic", "SideProject", "nocode", "vibecoding"}

# DM only in these — aggressive automod flags AI content, karma=2 gets removed
DM_ONLY_SUBS = {"SaaS", "indiehackers", "solopreneur"}


# ── State management ───────────────────────────────────────────────────────────
def load_seen():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            data = json.load(f)
            # Prune entries older than 48 hours to keep file small
            cutoff = time.time() - 172800
            return {k: v for k, v in data.items() if v > cutoff}
    return {}


def save_seen(seen):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(seen, f)


def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"[{ts}] {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


# ── Reddit fetching ────────────────────────────────────────────────────────────
def fetch_new_posts(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=25&sort=new"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "NEXUS7-TideScout/1.0 (personal research by /u/GrandFit6072)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read())
        return data["data"]["children"]
    except Exception as e:
        log(f"r/{subreddit} fetch error: {e}")
        return []


# ── Qualification ──────────────────────────────────────────────────────────────
def is_qualifying(post_data):
    author = post_data.get("author", "").lower()
    if author in ALREADY_CONTACTED:
        return False
    if post_data.get("score", 0) < -3:
        return False

    text = (post_data.get("title", "") + " " + post_data.get("selftext", "")).lower()

    for required_list, boost_list in PAIN_SIGNALS:
        # All required phrases must be present
        if all(req in text for req in required_list):
            # If there are boost phrases, at least one must also be present
            if not boost_list or any(b in text for b in boost_list):
                return True
    return False


def get_matched_signal(post_data):
    text = (post_data.get("title", "") + " " + post_data.get("selftext", "")).lower()
    for required_list, boost_list in PAIN_SIGNALS:
        if all(req in text for req in required_list):
            if not boost_list or any(b in text for b in boost_list):
                return required_list[0]
    return "distribution pain"


# ── Comment/DM drafting ────────────────────────────────────────────────────────
def draft_comment(title, body, signal, subreddit):
    import random
    title_l  = title.lower()
    body_l   = (body or "").lower()
    combined = title_l + " " + body_l

    # Pull a specific detail from the title to reference directly
    # Makes it feel like the commenter actually read the post

    if "distribution" in combined and "build" in combined:
        options = [
            "yeah the building vs getting users gap is wild. what have you actually tried so far that didn't work?",
            "this is the part nobody talks about honestly. what channels did you try first?",
            "totally this. what does your current approach even look like? curious where it breaks down for you.",
        ]
    elif "no traction" in combined or "crickets" in combined or "zero traction" in combined:
        options = [
            "ugh the post-launch crickets thing is brutal. how long has it been and what have you tried?",
            "been there. what did you try first after launch? curious if any channel even showed a tiny bit of life.",
            "the silence after launch is honestly the hardest part. what's your current approach to finding people?",
        ]
    elif "no audience" in combined or "no following" in combined:
        options = [
            "launching without an audience is genuinely hard mode. what have you tried so far to find your first users?",
            "yeah this is the real problem most build in public content skips over. where are you trying to find people right now?",
            "without an existing audience the first users problem is real. what's worked even a little so far?",
        ]
    elif "no users" in combined or "0 users" in combined or "can't get users" in combined:
        options = [
            "what channels have you actually tried? like specifically, not just 'posted on reddit' lol",
            "the 0 to first users problem is so real. what's your current approach looking like?",
            "curious what you've tried so far. like which channels and what happened?",
        ]
    elif "just launched" in combined or "i launched" in combined:
        options = [
            "congrats on shipping. what's the distribution plan look like right now?",
            "nice, what are you doing to get your first users? like what channels are you trying?",
            "what does getting your first users look like for you? curious what you're trying first.",
        ]
    elif "how do i get" in combined or "how to get" in combined:
        options = [
            "what have you tried so far? asking bc the answer is usually pretty specific to what you built.",
            "curious what you've already ruled out. what channels did you try that didn't work?",
            "what's the product? that usually changes the answer a lot tbh.",
        ]
    else:
        options = [
            "what have you tried so far and what's felt most broken about it?",
            "where does it actually fall apart for you? like which part specifically.",
            "curious what your current approach looks like. what have you tried?",
        ]

    comment = random.choice(options)

    # Occasionally (1 in 3) add a short second line about doing research
    add_research_line = random.random() < 0.33
    if add_research_line:
        research_lines = [
            "\n\nasking bc i'm researching this exact problem right now.",
            "\n\ni'm actually mapping out this exact problem for something i'm working on.",
            "\n\ncurious to hear more, doing research on exactly this.",
        ]
        comment += random.choice(research_lines)

    return comment


def draft_dm(title, body, signal, username):
    title_l = title.lower()
    combined = (title_l + " " + (body or "").lower())

    if "distribution" in signal or "distribution" in combined:
        line1 = f"hey — saw your post about distribution being the hard part."
        line2 = "genuinely curious where it breaks down for you — is it finding the right channels or getting people to actually care once you're there?"
    elif "no traction" in signal or "crickets" in combined:
        line1 = f"hey — saw your post about launching and getting no traction."
        line2 = "curious what you tried first and what felt most broken about it."
    elif "no audience" in signal:
        line1 = f"hey — saw your post about launching without an audience."
        line2 = "what's the current approach to finding your first real users?"
    else:
        line1 = f"hey — saw your post and it resonated."
        line2 = "what's been the hardest part of getting people to actually find and use what you built?"

    dm = f"{line1} {line2}\n\ndoing research on the gap between shipping something and actually getting users — would love to hear your story."
    return dm


# ── Action decision ────────────────────────────────────────────────────────────
def decide_action(post_data, subreddit):
    age_h = (time.time() - post_data["created_utc"]) / 3600

    # Strict subreddits: always DM, never comment (automod removes AI content)
    if subreddit in DM_ONLY_SUBS:
        return "DM"

    # Lenient subreddits: comment if fresh enough
    if subreddit in COMMENT_SAFE_SUBS and age_h < 2:
        return "COMMENT"

    return "DM"


# ── Telegram ───────────────────────────────────────────────────────────────────
def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text":    text,
        "parse_mode": "HTML",
        "disable_web_page_preview": "false",
    }).encode()
    req = urllib.request.Request(url, data=payload, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())
            return result.get("ok", False)
    except Exception as e:
        log(f"Telegram error: {e}")
        return False


def format_message(post_data, subreddit, action, comment_draft, dm_draft):
    age_min    = int((time.time() - post_data["created_utc"]) / 60)
    age_str    = f"{age_min}m ago" if age_min < 60 else f"{age_min//60}h ago"
    karma_warn = "" if subreddit in LOW_KARMA_SAFE else "\n⚠️ Low karma — comment may be auto-removed. DM safer."

    # Extract a short pain quote from title or body
    title = post_data.get("title", "")
    body  = (post_data.get("selftext", "") or "")[:200].strip()
    pain_quote = body if len(body) > 20 else title

    msg = (
        f"🎯 <b>TIDE LEAD — {action}</b>\n"
        f"r/{subreddit} | u/{post_data['author']} | {age_str}{karma_warn}\n\n"
        f"<b>Post:</b> {title}\n"
        f"<b>Pain:</b> \"{pain_quote[:120]}\"\n\n"
        f"🔗 {post_data['url']}\n\n"
    )

    if action == "COMMENT":
        msg += f"<b>PASTE THIS COMMENT:</b>\n<pre>{comment_draft}</pre>"
    else:
        msg += (
            f"<b>DM THIS:</b>\n<pre>{dm_draft}</pre>\n\n"
            f"<i>Go to their profile → Chat</i>"
        )

    return msg


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    log("Scout run starting")
    seen     = load_seen()
    new_seen = {}
    found    = 0

    for subreddit in SUBREDDITS:
        posts = fetch_new_posts(subreddit)
        for p in posts:
            d      = p["data"]
            post_id = d["id"]

            # Skip if already processed
            if post_id in seen:
                continue

            # Skip old posts
            age = time.time() - d.get("created_utc", 0)
            if age > MAX_AGE_SECONDS:
                new_seen[post_id] = time.time()  # mark as seen so we skip next run too
                continue

            # Skip non-qualifying
            if not is_qualifying(d):
                new_seen[post_id] = time.time()
                continue

            # It's a lead
            signal        = get_matched_signal(d)
            action        = decide_action(d, subreddit)
            comment_draft = draft_comment(d.get("title",""), d.get("selftext",""), signal, subreddit)
            dm_draft      = draft_dm(d.get("title",""), d.get("selftext",""), signal, d["author"])
            message       = format_message(d, subreddit, action, comment_draft, dm_draft)

            if send_telegram(message):
                log(f"Sent: u/{d['author']} on r/{subreddit} [{action}]")
                found += 1
            new_seen[post_id] = time.time()

        time.sleep(2)  # be polite to Reddit's servers

    seen.update(new_seen)
    save_seen(seen)
    log(f"Done — {found} leads sent")


if __name__ == "__main__":
    main()
