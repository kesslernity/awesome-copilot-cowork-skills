# Branded Deck Builder

> Cowork has no BrandKit, so this skill gives it one: your own .pptx template, written brand rules, and a compliance pass on every slide.

## What it produces

- A PowerPoint deck built on your company template, saved to OneDrive at `/Documents/Cowork/output/<topic-slug>-deck-v1-DRAFT.pptx`, with DRAFT on the title slide
- The approved outline as `<topic-slug>-outline.md`
- A slide-by-slide brand compliance report as `<topic-slug>-brand-compliance.md`, every rule marked PASS, FIXED or MANUAL CHECK

## Install

**Quickest: upload the zip.** [Download `branded-deck-builder.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/branded-deck-builder.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/branded-deck-builder/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Build a 12-slide deck on the Q3 roadmap using our company template."
- "Turn this Word doc into an on-brand presentation for the exec review."
- "I need CI-compliant slides for the customer kickoff next week."
- "Rebuild these slides on our corporate template and check them against our brand rules."

## Why this exists

Brand compliance keeps coming up in the Cowork community as something the product does not do. One Frontier preview user named CI-compliant presentations as a custom skill the biggest wow factor compared with the old Copilot (https://www.reddit.com/r/microsoft_365_copilot/comments/1slxidi/), and another reported on template-based decks that they "gave it our standard template and it worked really well" (https://www.reddit.com/r/microsoft_365_copilot/comments/1shymgj/). This skill packages that pattern so it is repeatable: an explicit template file, explicit written rules, and an explicit compliance check, instead of hoping the model remembers your colours.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
