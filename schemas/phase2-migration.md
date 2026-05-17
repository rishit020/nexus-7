# PHASE 2 MIGRATION GUIDE

## What Phase 2 adds
- Supabase: data files become real database tables
- Telegram bot: voice notes -> Whisper -> Claude -> Supabase (auto-categorized)
- Web dashboard: Next.js reading Supabase live
  Sections: Tide pipeline, leads, outreach, habits, goals, inbox, patterns

## Supabase table map
data/leads.md          -> leads table
data/outreach.md       -> outreach table
data/posts.md          -> posts table
data/decisions.md      -> decisions table
data/agent-log.md      -> agent_sessions table
context/inbox.md       -> inbox table
context/patterns.md    -> patterns table
context/communities.md -> communities table

## Telegram capture flow (Phase 2)
voice note -> Telegram bot -> Whisper transcription -> Claude API classifies ->
  task -> tasks table
  lead -> leads table
  idea -> inbox table
  decision -> decisions table
-> Telegram confirmation sent back

## Dashboard sections (Phase 2)
1. Home: today focus, tasks, habits, current priority
2. Tide: MRR tracker, leads pipeline, outreach queue
3. Brain: projects, decisions, goals
4. Inbox: unprocessed captures
5. Patterns: agent learning log
6. Calendar: Google Calendar (already MCP-connected)

## Upgrade path
1. Supabase project -> create tables from field names in data files
2. Migration script: parse RECORD_START/END blocks -> insert rows
3. Update each skill to call Supabase instead of reading markdown
4. Telegram bot via BotFather + Whisper
5. Next.js dashboard
Skill logic stays identical. Only data access layer changes.
