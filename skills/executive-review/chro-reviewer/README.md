# CHRO Reviewer

> Pressure-test your plan against a CHRO archetype before the real one asks who actually loses their job on slide 12.

## What it produces

A structured review document, `<artifact-name>-chro-review.docx`, saved to `/Documents/Cowork/reviews/` in your OneDrive, containing:

- **VERDICT**: ready, ready with conditions, or not ready
- **TOP FINDINGS**: each one quotes or cites the exact part of your document it is about, no generic feedback; where the document is silent, the finding is recorded as an open question, never an invented fact
- **RISKS**: from the people lens (change load, consultation exposure, skills gaps, manager load, attrition, survivor morale)
- **WHAT WOULD CHANGE MY MIND**: the specific evidence that would move the verdict up
- **5 INTERROGATION QUESTIONS**: the questions the real CHRO is likely to ask in the room

The persona lives in `references/persona.md`: mandate, ten probes, red flags, what convinces a CHRO and what gets dismissed, plus documented blind spots so a validator can challenge the feedback where the archetype distorts it.

## Install

**Quickest: upload the zip.** [Download `chro-reviewer.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/chro-reviewer.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/chro-reviewer/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a CHRO review on ops-restructure-plan.docx"
- "What would HR say about this operating model deck before the people committee sees it?"
- "Pressure-test this rollout plan from a people lens, the works council meets next month"
- "I present this to our CHRO on Tuesday. Find the people holes first."

## Why this exists

This skill is a bench persona for the executive-review suite. The core seven cover the C-suite; the bench adds executive lenses you run only when the document warrants them. The CHRO lens matters whenever a plan changes who does what: restructurings, operating model shifts, automation cases and anything with "freed capacity" in it. Those documents tend to be precise about the savings and vague about the people, and that vagueness is exactly what the real CHRO interrogates. It works standalone; you do not need the rest of the suite installed.


## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
