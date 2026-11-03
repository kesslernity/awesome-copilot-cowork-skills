# Dataset Insight Pack

> Reads a spreadsheet and your question, then produces a DRAFT insight pack — profile, observations (as leads, not conclusions), caveats, and suggested charts. Never the source of truth; every figure is yours to verify.

## What it produces

- `DRAFT-insight-pack-<Dataset>-<date>-v1.docx`: a data profile (columns, types, missing, ranges), observations each cited to the data and framed as leads, caveats (completeness, correlation-not-causation), and suggested next analyses and charts. DRAFT-labelled, with every figure marked "as read — verify in source".

Saved next to the dataset in OneDrive, with the exact path reported in the conversation.

## Install

**Quickest: upload the zip.** [Download `dataset-insight-pack.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/dataset-insight-pack.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/dataset-insight-pack/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

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
