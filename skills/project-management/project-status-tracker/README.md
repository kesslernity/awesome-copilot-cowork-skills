# Project Status Tracker

> Cowork maintains your project's status files from email, Teams and meeting transcripts, then writes the weekly status report so you stop rebuilding it by hand every Friday.

## What it produces

One OneDrive folder per project at `/Documents/Cowork/projects/<project-name>/` containing:

- **project.md**: overview, aliases, Green/Amber/Red status, milestones and a dated progress log
- **decisions.md**: a decision log with context, who decided, source and status
- **risks.md**: a RAID log (risks, assumptions, issues, dependencies) with owners and review dates
- **links.md**: the key files, threads and URLs with a note on why each matters
- **status-YYYY-WW.docx**: a weekly DRAFT status document (summary, progress, decisions taken, top risks with owners, asks) built from the four files
- **actions.md**: action items, written as the reliable file fallback because Cowork's writes to Planner and To Do can fail silently

First run scaffolds the four files. Every later run appends and revises: each file keeps a dated Changes section at the top, and nothing is ever silently deleted.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` so the file sits at `/Documents/Cowork/skills/project-status-tracker/SKILL.md`.
2. Start a NEW Cowork conversation (skills are only discovered when a conversation starts).
3. Use one of the trigger phrases below.

## Example triggers

- "Set up project tracking for the Helios migration."
- "Update the helios-migration project files from the last two weeks of email and Teams."
- "Log a decision on helios-migration: we are going with vendor B for the data layer."
- "Produce this week's status report for helios-migration."

## Why this exists

The strongest Cowork demand signal we found while researching this repo is a thread on r/microsoft_365_copilot asking for exactly this workflow: project status that keeps itself current from the emails, Teams channels and meetings where the information already lives. Cowork can read all of those sources and write OneDrive files, but it has no memory between sessions; this skill gives it durable per-project files to maintain, so each run picks up where the last one stopped. Thread: https://www.reddit.com/r/microsoft_365_copilot/comments/1tkio2o/

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | 2026-06-10 | Initial version |
