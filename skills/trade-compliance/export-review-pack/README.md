# Export Review Pack

> Reads an export transaction and produces a DRAFT review pack — parties to screen, a classification worksheet, a red-flag review, and licence-determination questions. Never classifies, screens, clears, or decides a licence; trade compliance does.

## What it produces

- `DRAFT-export-review-<Transaction>-<date>-v1.docx`: a parties-to-screen list + screening checklist, an item classification worksheet (no ECCN assigned), a red-flag review, licence-determination questions, and open items. DRAFT-labelled, with every determination left to trade compliance.

Saved next to the source description in OneDrive, with the exact path reported in the conversation.

## Install

**Quickest: upload the zip.** [Download `export-review-pack.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/export-review-pack.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/export-review-pack/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Prepare an export review pack for this order"
- "Build the trade-compliance prep for this overseas shipment"
- "Pre-check this transaction for export control — parties, classification, red flags"
- "Assemble the export-control file for this deal"

## Why this exists

Every export needs the same file built before trade compliance can decide: who must be screened, what the item is in technical terms, whether any red flags are present, and what drives the licence question. This skill assembles that file from a transaction description so the export control officer starts from a structured pack. It deliberately makes no determination: it never assigns a classification, never decides a screening match, never clears anyone, and never decides licence need — because those carry civil and criminal liability and belong to trade compliance, against current official sources. Screening still runs in your screening tool.

## Status

Tested in Cowork: not yet — format-validated against the Agent Skills spec; run a live tenant test before relying on it. Treat every output as preparation requiring trade-compliance review regardless.

## Changelog

| Version | Date | Notes |
| --- | --- | --- |
| 1.0 | 2026-06-18 | Initial version |
