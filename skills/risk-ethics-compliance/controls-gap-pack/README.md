# Controls Gap Pack

> Reads a requirement (regulation, standard, policy) and your control descriptions, then produces a DRAFT controls-and-gap pack — obligations, mapped controls, apparent coverage, gaps, and actions to assess. Owners and audit decide compliance and effectiveness.

## What it produces

- `DRAFT-controls-gap-<Requirement>-<date>-v1.docx`: the requirement broken into obligations, the controls that appear to address each, apparent coverage (Addressed / Partial / Not evident), gaps, actions to assess, and questions for control owners. DRAFT-labelled; not a compliance determination.
- `DRAFT-controls-gap-<Requirement>-<date>-v1.xlsx` (optional): the mapping as a workbook.

Saved next to the requirement source in OneDrive, with the exact path reported in the conversation.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `controls-gap-pack`; the lowercase `skills` folder name is case-sensitive).
2. Start a NEW Cowork conversation (skills are only discovered when a conversation starts).
3. Put the requirement and your control descriptions in OneDrive/SharePoint and use a trigger below.

## Example triggers

- "Map this regulation to our controls and find the gaps"
- "Run a controls gap analysis for this standard against our control register"
- "Break this policy requirement into obligations and map our controls"
- "Where are the control gaps for these contractual security requirements?"

## Why this exists

Controls mapping is slow, manual, and easy to fudge: read the requirement, split it into obligations, line each up against the control register, and note where coverage is thin. This skill does that first pass from your own documents so compliance and audit start from a structured draft. It is deliberately honest about its ceiling — it can see what a control *says*, not whether it *operates*, so coverage is only ever "apparent", and it never concludes the organisation is compliant or a control is effective. Owners and audit assess and test.

## Status

Tested in Cowork: not yet — format-validated against the Agent Skills spec; run a live tenant test before relying on it. Treat the mapping as a draft requiring owner/audit assessment regardless.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-18 | Initial version |
