# SharePoint Review Sweeper

> Finds every document past its review date in a SharePoint library, then hands you a reminder spreadsheet and per-owner email Drafts instead of a manual library export.

## What it produces

- `review-sweep-YYYY-MM-DD.xlsx` in OneDrive at `/Documents/Cowork/output/sharepoint-review-sweeper/`, with four sheets: Overdue (document, owner, review date, days overdue, link), Due soon, No review date (documents with missing or unparseable metadata, so nothing slips through), and a Summary with reconciled counts.
- One notification email per document owner in your Drafts folder, listing their overdue documents with links. Drafts only, the skill never sends anything.
- A conversation summary with bucket counts, the exact workbook path, and confirmation of whether notifications went to Drafts or to a fallback `notifications-YYYY-MM-DD.md` file.

## Install

**Quickest: upload the zip.** [Download `sharepoint-review-sweeper.zip`](https://github.com/kesslernity/awesome-copilot-cowork-skills/raw/main/dist/zips/sharepoint-review-sweeper.zip). In Cowork, open **Customize**, select the **Skills** tab, select the arrow next to **Add**, then **Upload skill**, and choose the file. Cowork validates it and saves the skill to your OneDrive for you, so you never create a folder.

**Or copy this folder** into OneDrive at `/Documents/Cowork/skills/sharepoint-review-sweeper/`. The lowercase `skills` folder name is case-sensitive, and you copy the skill folder itself, not the category folder above it.

Either way, start a **NEW** Cowork conversation afterwards: skills are discovered only when a conversation starts. Then use one of the trigger phrases below.

Custom skills are not supported in Cowork on a phone or tablet, so this needs a laptop or desktop.

## Example triggers

- "Run a review sweep on the Policies library"
- "Which documents in our quality library are past their review date?"
- "Build the overdue document review report and draft the owner reminders"
- "Check the contracts library for stale documents that need review"

## Why this exists

Document review-date governance is a recurring ask from IT admins on the Cowork preview: a Reddit thread describes exactly this workflow, sweeping a library's review-date column and chasing document owners (https://www.reddit.com/r/microsoft_365_copilot/comments/1t8or2n/). IT and MSP admins are the most represented role across Cowork discussion threads, and review-date compliance is the kind of audit item that otherwise means exporting a library to Excel by hand every month. This skill turns it into one request that ends with a versioned spreadsheet and reminder Drafts ready for a human to check and send.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0 | 2026-06-10 | Initial version |
