# Works Council Reviewer

> Pressure-test your rollout plan against a Works Council Representative archetype before the real consultation meeting does it for you.

## What it produces

A structured review document, `<artifact-name>-works-council-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback; where your document is silent, the finding is an open question, never an invented fact
- **RISKS**: from the employee-representative lens (consultation sequence, employee data and monitoring exposure, workload and performance pressure, voluntariness, precedent)
- **WHAT WOULD CHANGE MY MIND**: the written commitments and consultation steps that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real representative is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a works council representative and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `works-council-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/works-council-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/works-council-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a works council review on copilot-rollout-plan.docx"
- "What would the works council say about this deck before I take it to consultation?"
- "Pressure-test this business case from an employee-representative lens, we brief the staff council next month"
- "We present the new tooling plan to employee reps on Thursday. Find the holes first."

## Why this exists

This skill is a bench persona for the executive-review suite. The core reviewers cover the C-suite, but plenty of proposals that survive finance and security review stall at employee consultation, because nobody read the document the way an elected employee representative will. This persona does that read before the meeting: consultation sequence, employee data, monitoring capability, whose hours the savings come from, and what precedent the decision sets. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
