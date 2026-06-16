# Project Dashboard Builder

> One Cowork request turns your project tracker files into a polished, offline, single-file HTML dashboard you can attach, pin or print.

## What it produces

A self-contained `dashboard-<project>-YYYY-MM-DD.html` file saved to `/Documents/Cowork/projects/<project>/` with five sections: a colour-coded status banner (Green, Amber or Red), a milestones table, a risks heat list sorted by severity, a decisions log and a links list. All CSS is inline, there is no JavaScript and no CDN call, so the file renders in any browser with no internet connection. Optionally, an Outlook draft (never sent) with the dashboard attached.

It pairs with the `project-status-tracker` skill in this repository: that skill maintains `project.md` (which holds the status and the milestones table), `decisions.md`, `risks.md` and `links.md` in your project folder, and this skill renders them. No tracker yet? It also runs from a status summary you paste into the chat.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (so the path is `/Documents/Cowork/skills/project-dashboard-builder/`).
2. Start a NEW Cowork conversation (skills are discovered only when a conversation starts).
3. Use one of the trigger phrases below.

## Example triggers

- "Build a dashboard for the website-relaunch project."
- "Make me an HTML status page for Project Atlas I can pin in Teams."
- "Turn my project tracker into a one-page dashboard for the steering committee."
- "Refresh the migration project dashboard with this week's tracker."

## Why this exists

HTML dashboards and micro-apps are a recurring ask among Cowork preview users: project dashboard builds have been posted on r/microsoft_365_copilot (https://www.reddit.com/r/microsoft_365_copilot/comments/1t8or2n/ and https://www.reddit.com/r/microsoft_365_copilot/comments/1too7y3/), and an r/CopilotPro thread asked people to share the dashboards they had generated. This skill adds two guardrails that ad hoc builds tend to miss: it forbids external resources entirely, so the file keeps rendering with no internet connection, and it names an explicit OneDrive save path and reports where the file actually went, because Cowork outputs sometimes land in session folders.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
