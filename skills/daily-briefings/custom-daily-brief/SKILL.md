---
name: custom-daily-brief
description: Builds a role-tuned morning brief as a Word document covering emails that need replies, today's calendar, Teams mentions and upcoming deadlines, using section presets from an editable config file. Use when the user asks for their daily brief, morning brief, start-of-day summary or custom briefing, or wants to change which sections their brief covers.
---

## PURPOSE

Produce a consistent, role-specific morning brief and save it as a dated Word document. This skill is the configurable layer on top of the built-in Daily Briefing skill, not a replacement for it. The built-in gives everyone the same summary; this skill adds four things the built-in does not: role presets (PM, EA, IT admin, sales), a user-editable custom section list, a saved file with a predictable date-stamped name in a fixed folder, and an optional email Draft of the brief to the user. Every data-gathering step delegates to a built-in skill.

## WHEN TO RUN

- The user asks for their daily brief, morning brief, start-of-day summary or "run my brief".
- The user asks to change, tune or reconfigure what their brief covers (edit the config, switch preset).
- The user asks to see which brief presets exist.
- The user asks to run the brief every morning: confirm the active preset, run it once now, then tell the user they can ask Cowork to repeat this skill on a schedule (for example "run custom-daily-brief every weekday at 07:30") (Cowork allows up to five scheduled prompts per user).

## INPUTS YOU GATHER

1. The active preset and its section list from `references/brief-config.md`. Read this file fresh on every run; the user edits it between runs and edits must take effect immediately.
2. Today's date, for the output filename and for all date-window calculations.
3. The lookback windows defined in the config (email lookback, Teams mention lookback, deadline horizon).
4. Whether to also create an email Draft of the brief: use the `email-draft` flag in the config; if the flag is absent, ask the user once and suggest they add the flag to the config.

If `references/brief-config.md` cannot be read, tell the user, ask which preset to use (PM, EA, IT admin, sales or custom), and run with the core sections in workflow order (emails needing answers, today's calendar, Teams mentions, deadlines), applying the preset filters described in steps 3 to 7. Do not silently invent a configuration.

## WORKFLOW

1. **Load config.** Read `references/brief-config.md`. Find the `active-preset:` line and the matching preset block. Resolve each listed section name against the Section catalogue in that file. If the user named a different preset in their request, that overrides the config for this run only; do not edit the config without being asked.
2. **Baseline.** Run the built-in Daily Briefing skill to get the standard summary of the day. Use it as raw input for the sections below, never as the final output; the final output must follow the preset's section order and the document format in step 9.
3. **Emails needing answers** (built-in Email skill). Scan the inbox for messages from the email lookback window (config default: 3 business days) that are unread, flagged, or end in a direct question or request addressed to the user. For each, capture: sender, subject, the ask in one line, and how old it is. Apply the preset's email filter if one is defined (for example the sales preset prioritises external senders; the IT admin preset prioritises incident and outage keywords). On a large inbox, state in the brief how many messages were scanned rather than implying complete coverage.
4. **Today's calendar** (built-in Calendar Management skill). List today's meetings in time order with start time, duration, title and organiser. Flag double-bookings and meetings that have no agenda in the invitation. Apply the preset's calendar notes if defined (for example the sales preset flags external meetings; the IT admin preset flags change windows and maintenance slots).
5. **Teams mentions** (step 2 baseline plus built-in Communications skill). Source mentions primarily from the Daily Briefing baseline already gathered in step 2 and from the built-in Communications skill, within the mention lookback window (config default: 24 hours). For each, capture channel or chat name, who mentioned them, and a one-line summary of what is being asked. Use Enterprise Search only as a fallback when neither primary source is available, querying the user's display name; Enterprise Search keyword-matches text and has no @mention filter, so when the fallback is used the section must be labelled "search-based, may be incomplete" and must not assert "No mentions found". Only when the primary sources ran and returned nothing may the section say "No mentions found" with the configured window named (for example "No mentions found in the last 24 hours"); the section is never silently omitted.
6. **Deadlines** (built-in Enterprise Search skill). Enterprise Search is keyword search; it cannot query by dates inside document text, so work in two stages. First, search the user's recent emails and files for the preset's deadline keywords (for example the PM preset uses milestone and deliverable terms; the IT admin preset uses expiry, renewal and change-window terms). Second, read the top hits, extract any dates they contain, and keep only those falling within the deadline horizon (config default: 7 days). List each as: date, item, source document or email. The section must name the keywords searched and state that coverage is keyword-based and may miss deadlines phrased differently, so gaps are visible rather than implied complete.
7. **Scheduling requests** (built-in Scheduling skill), only if the preset includes this section (the EA preset does by default). List open requests to find or move meeting times, plus today's meetings missing a location or join link.
8. **Yesterday's meeting actions** (built-in Meetings skill), only if the preset includes this section. Pull recaps and action items from the user's meetings on the previous business day and list the actions assigned to the user.
9. **Compose the document** (built-in Word skill). Build the brief with: title "DRAFT Daily Brief, {weekday} {D Month YYYY}", a two-line summary at the top (busiest block of the day plus the single most urgent item), then the preset's sections in the order listed in the config. Sections with no data appear with an explicit "Nothing today" line. Keep each item to one line where possible; the whole document should read in under three minutes.
10. **Save the file.** Save as `/Documents/Cowork/briefs/daily-brief-YYYY-MM-DD.docx` in the user's OneDrive (create the `briefs` folder if it does not exist). Do not rely on the session's default save location. If a file with that exact name already exists, do not overwrite it; save as `daily-brief-YYYY-MM-DD-v2.docx` (incrementing as needed) and tell the user both filenames. After saving, verify the file exists at that path.
11. **Optional email Draft** (built-in Email skill), only if the config flag or the user asked for it. Create a Draft addressed to the user themselves with subject "DRAFT Daily Brief, YYYY-MM-DD" and the brief content in the body. Leave it in Drafts. Never send it.
12. **Report.** Tell the user, in this order: the full OneDrive path of the saved document; whether an email Draft was created (and that it is in Drafts, unsent); which preset and sections were used; which sections came back empty; and that they can ask Cowork to run this skill on a schedule each morning (Cowork allows up to five scheduled prompts per user).

## OUTPUT ARTIFACTS

- `/Documents/Cowork/briefs/daily-brief-YYYY-MM-DD.docx`: the brief, always created, always labelled DRAFT in the title.
- Email Draft "DRAFT Daily Brief, YYYY-MM-DD" in the user's Drafts folder: only when the config flag `email-draft: yes` is set or the user asks. Never sent.
- `/Documents/Cowork/briefs/daily-brief-actions-YYYY-MM-DD.md`: only created as the fallback in the To Do edge case below.

Report the exact saved path of every artifact in the final message. Never leave an artifact in a session folder without telling the user where it is.

## FALLBACKS AND EDGE CASES

- **Config missing or malformed:** say so, ask the user to pick a preset, run with that preset, and offer to repair `references/brief-config.md` (with their approval, since that edits an existing file).
- **A section's data source returns nothing:** keep the section heading and write "Nothing today" or "No mentions found in the last 24 hours". Empty sections are information; omitting them looks like a failure.
- **A built-in skill fails (for example Teams search is unavailable):** produce the brief anyway with that section marked "Could not be retrieved this run", and name the section in the final report.
- **User asks to push the brief's action items to Microsoft To Do or Planner:** attempt it, then verify the items actually appear. These writes are known to fail silently. If verification fails or is not possible, write the items to `/Documents/Cowork/briefs/daily-brief-actions-YYYY-MM-DD.md` instead and tell the user explicitly which path was taken: To Do, the file, or both.
- **Output lands in a session folder:** move or re-save it to `/Documents/Cowork/briefs/` and confirm the final path. The user must never have to hunt for the file.
- **Config edited mid-conversation:** fine, the config is re-read every run. Only renaming the skill folder or SKILL.md requires the user to start a new conversation for re-discovery.
- **Weekend or holiday run:** still produce the brief; "yesterday's meeting actions" means the previous business day.

## SAFETY RULES

- Never delete or overwrite any existing file. Same-name collisions get a `-v2` (then `-v3`) suffix.
- Email output is Drafts only. Never send any email, including the brief to the user themselves.
- Every generated document carries DRAFT in its title until the user has reviewed it.
- Do not edit `references/brief-config.md` or any other existing file without the user's explicit approval in this conversation.
- Read only the user's own mailbox, calendar and Teams data as surfaced by the built-in skills; do not search other people's content beyond what those skills return.

## QUALITY SELF-CHECK

Before reporting completion, confirm every box:

- [ ] `references/brief-config.md` was read this run and the active preset's section order was followed exactly.
- [ ] Each data section was gathered with the named built-in skill (Daily Briefing, Email, Calendar Management, Communications, Enterprise Search, Scheduling, Meetings) and none was reimplemented from scratch.
- [ ] Every email item has sender, subject, the ask and its age; every deadline has a date and a source.
- [ ] Empty sections say so explicitly; no section was silently dropped.
- [ ] The document title starts with DRAFT and the filename matches `daily-brief-YYYY-MM-DD.docx`.
- [ ] The file is confirmed present at `/Documents/Cowork/briefs/` and the full path was reported to the user.
- [ ] No file was overwritten, no email was sent, and any To Do write was verified or replaced by the actions file, with the path taken reported.
- [ ] The final message mentioned that the user can ask Cowork to run this on a morning schedule.
