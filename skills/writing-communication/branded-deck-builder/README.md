# Branded Deck Builder

> Cowork has no BrandKit, so this skill gives it one: your own .pptx template, written brand rules, and a compliance pass on every slide.

## What it produces

- A PowerPoint deck built on your company template, saved to OneDrive at `/Documents/Cowork/output/<topic-slug>-deck-v1-DRAFT.pptx`, with DRAFT on the title slide
- The approved outline as `<topic-slug>-outline.md`
- A slide-by-slide brand compliance report as `<topic-slug>-brand-compliance.md`, every rule marked PASS, FIXED or MANUAL CHECK

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (keep the folder name `branded-deck-builder`, and note that `skills` is lowercase).
2. Start a NEW Cowork conversation: skills are only discovered when a conversation starts.
3. Use one of the trigger phrases below.

One-time setup before your first deck: drop your company .pptx template into this folder, then copy `references/brand-rules-template.md` to `references/brand-rules.md` and replace the bracketed placeholders with your colours, fonts, logo rules and banned visuals. If you skip this, the skill stops and walks you through it instead of building an off-brand deck.

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
