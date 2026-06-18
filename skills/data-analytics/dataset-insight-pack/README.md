# Dataset Insight Pack

> Reads a spreadsheet and your question, then produces a DRAFT insight pack — profile, observations (as leads, not conclusions), caveats, and suggested charts. Never the source of truth; every figure is yours to verify.

## What it produces

- `DRAFT-insight-pack-<Dataset>-<date>-v1.docx`: a data profile (columns, types, missing, ranges), observations each cited to the data and framed as leads, caveats (completeness, correlation-not-causation), and suggested next analyses and charts. DRAFT-labelled, with every figure marked "as read — verify in source".

Saved next to the dataset in OneDrive, with the exact path reported in the conversation.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `dataset-insight-pack`; the lowercase `skills` folder name is case-sensitive).
2. Start a NEW Cowork conversation (skills are only discovered when a conversation starts).
3. Put the dataset in OneDrive/SharePoint and use a trigger below.

## Example triggers

- "Explore sales-q3.xlsx and tell me what stands out"
- "Profile this dataset and flag anomalies to investigate"
- "Find leads in the support-tickets export for last quarter"
- "Give me a first read on this spreadsheet before I dig in"

## Why this exists

The slowest part of ad-hoc analysis is the first pass: open the file, see what's in it, spot what's worth chasing. This skill does that first read and writes it up — but it is deliberately honest about its limits. Cowork can misread a column or miss rows, so every observation is a lead to investigate (never a conclusion), every figure says "verify in source", and it never claims a cause or makes the call. It gets you to the real analysis faster; it does not replace it.

## Status

Tested in Cowork: not yet — format-validated against the Agent Skills spec; run a live tenant test before relying on it. Treat all figures as unverified regardless.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-18 | Initial version |
