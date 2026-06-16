# News Monitor Digest

> Turns a manual review of a long list of news sources into one verified, role-relevant digest you can read in two minutes. Sweeps up to 24 sources per run, in grouped queries.

## What it produces

- `digest-YYYY-MM-DD.docx` in OneDrive at `/Documents/Cowork/news/`: 5 to 8 items, each with a one-line so-what for your role, a verified source URL and a publication date, plus a "checked but quiet" list (only sources actually covered by a query this run) and a "not individually checked this run" list, so coverage is never overstated. On request it creates an email Draft to yourself instead (never sent).
- `news-monitor-log.md` in the same folder: an append-only run log, so consecutive digests never repeat an item.

You control what gets monitored by editing one file: `references/sources.md` holds your role, your source list and your relevance criteria, and ships with a worked example for a Microsoft 365 administrator.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (the lowercase `skills` folder name matters), so you end up with `/Documents/Cowork/skills/news-monitor-digest/SKILL.md`.
2. Start a NEW Cowork conversation. Skills are only discovered when a conversation starts.
3. Use one of the trigger phrases below. The first run will ask you to confirm the source list in `references/sources.md`.

## Example triggers

- "Run my news digest"
- "Sweep my sources and make me a news flash for my role"
- "What happened in Microsoft 365 news this week? Put it in a digest doc"
- "Monitor my news sources and draft me an email digest"

## Why this exists

A Cowork preview user described rebuilding their scheduled review of "30+ Microsoft blogs" so it "pulls out much more relevant data and runs three times per week", and a commenter's reply was "Can you share that?" (https://www.reddit.com/r/microsoft_365_copilot/comments/1t8or2n/). In a separate thread, another user runs "a daily News flash with important News specifically for my role" (https://www.reddit.com/r/microsoft_365_copilot/comments/1slxidi/). This skill packages that workflow with a verification rule the manual version rarely gets: no item ships without a working source URL, and anything unconfirmed is marked unverified.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
