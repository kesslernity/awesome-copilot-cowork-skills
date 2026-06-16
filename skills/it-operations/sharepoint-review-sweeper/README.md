# SharePoint Review Sweeper

> Finds every document past its review date in a SharePoint library, then hands you a reminder spreadsheet and per-owner email Drafts instead of a manual library export.

## What it produces

- `review-sweep-YYYY-MM-DD.xlsx` in OneDrive at `/Documents/Cowork/output/sharepoint-review-sweeper/`, with four sheets: Overdue (document, owner, review date, days overdue, link), Due soon, No review date (documents with missing or unparseable metadata, so nothing slips through), and a Summary with reconciled counts.
- One notification email per document owner in your Drafts folder, listing their overdue documents with links. Drafts only, the skill never sends anything.
- A conversation summary with bucket counts, the exact workbook path, and confirmation of whether notifications went to Drafts or to a fallback `notifications-YYYY-MM-DD.md` file.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` (so the file sits at `/Documents/Cowork/skills/sharepoint-review-sweeper/SKILL.md`).
2. Start a NEW Cowork conversation. Skills are only discovered when a conversation starts.
3. Use one of the trigger phrases below.

Optional but recommended: fill in `references/sweep-config.md` (site URL, library, review-date column, owner column) before the first run. If you skip this, the skill asks for the missing values in conversation.

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
