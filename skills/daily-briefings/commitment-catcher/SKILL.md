---
name: commitment-catcher
description: Scans the last 24 hours of email, Teams chats and meeting transcripts for commitments in both directions, things the user promised to others and things others promised to the user. Maintains a running commitments.md ledger with open, done and overdue statuses, flags overdue items first, and creates To Do entries with a file fallback. Use when the user asks what they promised, what they are owed, whether they missed a commitment, or to run a daily commitment sweep.
---

# Commitment Catcher

## PURPOSE

Catch every commitment made in the last 24 hours of email, Teams messages and meeting transcripts, in both directions: commitments the user MADE (things they told others they would do) and commitments OWED to the user (things others said they would do for them). Maintain a single ledger file, commitments.md, that tracks each commitment across runs with a status of open, done or overdue, and surface overdue items first. Attempt Microsoft To Do entries for new commitments the user made, with a guaranteed file fallback.

This skill composes the built-in Email, Communications, Meetings and Enterprise Search skills. It does not replace the built-in Daily Briefing: it adds persistent commitment state that a briefing does not keep.

## WHEN TO RUN

- The user asks what they promised, what they are owed, or whether anything slipped.
- The user asks for a commitment sweep, commitment check or to update the commitments ledger.
- As a morning routine alongside the built-in Daily Briefing, or after a day heavy with meetings.

Run this skill interactively. The ledger save in step 7 requires the user's explicit approval in the conversation, so it is not suitable for an unattended scheduled prompt.

## INPUTS YOU GATHER

1. Scan window. Default is the last 24 hours. Read the "Last run" line in the ledger header first: if the last run was more than 24 hours ago, extend the window back to that timestamp so nothing falls in a gap, and tell the user the window you used. The user may override (for example "since Monday").
2. Optional focus. The user may narrow the sweep to one person, project or source ("just my mail", "anything I owe Dana").
3. First run only. Tell the user the ledger will be created at /Documents/Cowork/commitments/commitments.md in their OneDrive. The location is fixed: a future conversation has no memory of a custom choice and can only find the ledger at this path, so do not offer or accept a different folder.

Do not ask for anything else. Everything other than the three items above comes from the sources themselves.

## WORKFLOW

1. Load state. Open the ledger at /Documents/Cowork/commitments/commitments.md (use Enterprise Search if the direct path fails). If it cannot be found, do not declare a first run yet: search Enterprise Search for the ledger header line "Commitments ledger" (per references/ledger-format.md) and report the result of that search to the user. Only when that search also returns nothing, treat this as the first run: tell the user the ledger will be created at the fixed path, then create it from the template in references/ledger-format.md with empty sections.

2. Scan email with the built-in Email skill. Pull messages the user SENT in the window (candidate commitments MADE) and messages RECEIVED in the window (candidate commitments OWED). Apply the exclusions in references/commitment-language.md: skip newsletters, automated notifications, out-of-office replies and calendar responses.

3. Scan Teams with the built-in Communications skill. This is a bounded search, not an exhaustive message-by-message scan: query chats and channel messages in the window for the commitment-language phrases in references/commitment-language.md, plus any focus names or topics from INPUTS #2. Classify the user's own messages for MADE and other people's messages for OWED. The run summary must state that Teams coverage is search-based and may miss commitments phrased in ways the search did not match.

4. Scan meetings with the built-in Meetings skill. For each meeting in the window that has a transcript or AI-generated notes, extract commitments spoken by the user (MADE) and commitments spoken by others to the user (OWED). If a meeting has no transcript or notes, do not guess its content: name the meeting in the run summary as not scannable.

5. Classify every candidate using references/commitment-language.md. For each one record: direction (MADE or OWED), counterparty, the deliverable in one sentence, due date (explicit, or inferred from relative phrases and marked "(inferred)", or "none stated"), and the source (channel, sender, date, subject or meeting title). A request that nobody agreed to is not a commitment: keep it out of the ledger and list it in the run summary under "awaiting confirmation".

6. Reconcile against the ledger. Deduplicate: the same counterparty plus the same deliverable is one commitment, not two. Mark an existing entry done when the window contains evidence it was fulfilled (for example the user sent the file they promised), and cite that evidence in the entry. Mark any open entry whose due date is before today as overdue. Assign new entries the next IDs in the existing C-NNN sequence; never reuse an ID.

7. Write the updated ledger. Order the sections Overdue, Open, Done (last 14 days), Archive, exactly as specified in references/ledger-format.md, and update the "Last run" header line. Before saving, show the user a change summary in the conversation (new entries, items marked done, items now overdue) and ask for explicit approval to save over /Documents/Cowork/commitments/commitments.md. Never delete an entry: items only ever change status, and done items older than 14 days move to the Archive section at the bottom of the same file.

8. Create To Do entries. For each NEW open commitment the user MADE, attempt to create a task in the Microsoft To Do list named "Commitments", titled with the ledger ID, deliverable and due date (for example "C-014 Send Q3 forecast to Dana, due 12 Jun"). To Do writes are known to fail silently: read the list back and verify each task exists. If read-back is not possible, or any task is missing, append the missing items to /Documents/Cowork/commitments/actions.md as a dated checkbox section (format in references/ledger-format.md) and carry on. Never treat a To Do write as done without verification.

9. Report in the conversation, in this order: overdue items first with who and what; counts for the run (new MADE, new OWED, marked done, now overdue, awaiting confirmation); the full OneDrive path of every file written; and which To Do path was taken (verified in To Do, or written to actions.md, and why). If the platform saved any file to a session folder instead of the named path, say so explicitly and give the actual location.

## OUTPUT ARTIFACTS

| Artifact | Exact location | When |
|---|---|---|
| Commitments ledger | /Documents/Cowork/commitments/commitments.md | Every run, after user approval |
| To Do tasks | Microsoft To Do, list "Commitments" | New MADE commitments, only counted when read-back verifies |
| To Do fallback | /Documents/Cowork/commitments/actions.md | Only when a To Do write fails or cannot be verified |

Always state the full path of each artifact in the run summary. If a save lands in a session folder, report the real location and offer to move the file to the named path.

## FALLBACKS AND EDGE CASES

- Ledger missing or unreadable: run the Enterprise Search check in step 1 and report its result before treating the run as a first run. The ledger location is fixed at /Documents/Cowork/commitments/; never create a ledger in any other folder.
- To Do write fails silently: detected by read-back in step 8; fall back to actions.md and report it. Do not retry more than once.
- A source is unavailable (no Teams access, mail search fails): scan the remaining sources, and name each gap in the run summary rather than presenting a partial sweep as complete.
- Meeting without transcript or notes: name it in the summary as not scannable; do not infer commitments from the invite alone.
- More than 50 candidates in one run: ledger the ones with due dates first, list the rest in the summary, and ask the user whether to add them all.
- Counterparty unclear: use the best name available from the source plus the source reference. Never invent a name, an organisation or a due date.
- User says an item is done, or no longer needed: mark it done with a dated note (for example "cancelled by user, 10 Jun 2026"). Never delete the row.
- Conditional commitments ("if the client signs, I'll book the kick-off"): record with the condition in the deliverable text, status open, due date "none stated" until the condition is met.

## SAFETY RULES

- Never delete or overwrite any file without explicit user approval in the conversation. The ledger save in step 7 happens only after the user approves the change summary.
- Ledger entries are never deleted, only status-changed with a date. Old done items move to Archive inside the same file.
- Email: this skill reads mail only. If the user asks to chase a counterparty about an overdue item, create a Draft only, never send, and label the drafted text DRAFT.
- Never invent commitments, counterparties, dates or statistics. Every ledger entry must cite a real source the user can open.
- To Do failures are always reported in the summary, never silently dropped.
- Any generated document beyond the ledger and fallback file is labelled DRAFT until a human reviews it.

## QUALITY SELF-CHECK

Before finishing a run, confirm every box:

- [ ] All three sources (Email, Communications, Meetings) were scanned, or each gap is named in the summary
- [ ] Every ledger entry has an ID, direction, counterparty, deliverable, due date (or "none stated"), source and status
- [ ] Overdue items sit at the top of the ledger and lead the conversation summary
- [ ] No ledger entry was deleted and the C-NNN sequence is unbroken
- [ ] The user explicitly approved the ledger save before any overwrite
- [ ] Every To Do write was verified by read-back, or the actions.md fallback was used and reported
- [ ] The full OneDrive path of every file written appears in the summary
- [ ] The summary gives counts for both directions, MADE and OWED
