# DPIA Draft Pack

> Reads a project/processing description and produces a DRAFT DPIA scaffold — description, necessity & proportionality questions, a risk table with the ratings left blank, mitigations, and open questions. The DPO rates, decides, and signs.

## What it produces

- `DRAFT-DPIA-<Project>-<date>-v1.docx`: a DPIA scaffold — processing description, necessity & proportionality questions, a risk table with every rating cell left blank, mitigations to consider, and open questions. DRAFT-labelled; works from descriptions, contains no personal data.

Saved next to the source description in OneDrive, with the exact path reported in the conversation.

## Install

**Quickest: upload the zip.** [Download `dpia-draft-pack.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/dpia-draft-pack.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/dpia-draft-pack/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Start a DPIA for the new employee-monitoring tool — here's the project doc"
- "Draft a DPIA scaffold from the marketing-analytics design"
- "Scaffold a DPIA for sharing customer data with our new processor"
- "Build a DPIA draft from this processing description"

## Why this exists

A DPIA's first draft is mostly transcription: restating the processing, listing the questions to answer, and laying out the risk table — before any actual assessment happens. This skill does that scaffolding from a project description so the DPO starts from a structured draft instead of a blank template. It deliberately leaves every risk rating blank and makes no lawfulness call: the assessment, the ratings, and the sign-off are the DPO's, against the applicable law. It also works only from descriptions, never from personal data.

## Status

Tested in Cowork: not yet — format-validated against the Agent Skills spec; run a live tenant test before relying on it. Treat it as a scaffold the DPO must complete regardless.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-18 | Initial version |
