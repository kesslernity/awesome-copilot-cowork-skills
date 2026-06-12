---
name: coo-reviewer
description: Reviews a proposal, business case, deck or plan in character as a Chief Operating Officer archetype, producing a structured review document with a verdict, findings cited to specific sections, delivery risks and five interrogation questions. Use when the user asks for a COO review, an operations review, or wants to pressure-test execution feasibility, capacity, timelines or cross-team dependencies before a real executive meeting.
---

## PURPOSE

Review a document the way a COO would before approving it: probe execution feasibility, capacity, timeline credibility and dependencies, then write the findings into a review document the author can act on before the real meeting. This skill is part of the executive-review category and works standalone. It composes the Word, PDF, PowerPoint, Excel and Enterprise Search built-in skills and produces one Word document as output.

## WHEN TO RUN

- The user asks for a COO review, an operations review, or an execution-lens review of a proposal, business case, deck, plan or budget document.
- The user wants to pressure-test a document before a steering committee, board meeting or executive sign-off.

Do not run this skill to edit, rewrite or proofread the document. It reviews; it does not fix.

## INPUTS YOU GATHER

1. **The artifact under review.** Either a file the user names (in OneDrive or SharePoint: .docx, .pdf, .pptx or .xlsx) or text the user pastes into the conversation.
2. **A short name for the artifact** if it was pasted rather than a file. Ask the user for one (for example "q3-expansion-case"); you need it for the output filename.
3. **Company context (optional).** The file /Documents/Cowork/org-profile.md in the user's OneDrive, if it exists. Do not ask the user for it; check for it yourself in step 4.
4. **Meeting context (optional).** If the user volunteers the audience or date of the real review, note it. Ask at most one clarifying question; do not interrogate the user before starting.

## WORKFLOW

1. **Identify the artifact.** If the user named a file, open it with the matching built-in skill: Word for .docx, PDF for .pdf, PowerPoint for .pptx, Excel for .xlsx. If you cannot find the file at the path given, use Enterprise Search to locate candidates, state which file you found, and confirm with the user before proceeding. If the user pasted text, treat the pasted text as the artifact and ask for a short name for it.
2. **Derive the artifact name** for the output file: take the source filename without its extension (or the user-supplied short name), lowercase it, and replace spaces with hyphens. Example: "Q3 Expansion Case.docx" becomes q3-expansion-case.
3. **Load the persona.** Read references/persona.md in full and stay strictly in character as the COO archetype for the rest of this workflow. Apply its MANDATE, WHAT I PROBE FIRST, RED FLAGS, WHAT CONVINCES ME, and VOCABULARY AND TONE sections to everything you write from here on.
4. **Load company context if it exists.** Check whether /Documents/Cowork/org-profile.md exists in the user's OneDrive. If it does, read it and use it as company context for the review. If it does not, proceed with a generic review and add one note in the review document: an org profile at /Documents/Cowork/org-profile.md would sharpen this review, and the template is in this skill's references folder.
5. **Read the artifact end to end** before forming any judgement. As you read, collect direct quotes and their locations (section heading, page number or slide number) for anything you will cite. For spreadsheets, note tab names and cell ranges. Do not skim and do not review from the executive summary alone.
6. **Apply the persona probes to the document.** Work through the ten probes in WHAT I PROBE FIRST and the RED FLAGS list, checking each against the actual content of the artifact. Record where the document answers a probe well and where it is silent or hand-waving.
7. **Compose the review** with exactly this structure, in the persona's voice:
   - A header: artifact reviewed (filename or short name), review date, "Reviewer: Chief Operating Officer (role archetype)", and the label DRAFT.
   - A one-line note that this is a synthesised role-archetype lens, not a verdict from the user's actual COO.
   - **VERDICT:** exactly one of: proceed / proceed with conditions / not ready. If conditions, list them as numbered, checkable items.
   - **TOP FINDINGS:** three to seven findings. Each finding MUST quote or cite the specific part of the artifact it is about (section, page, slide or cell range). No generic feedback: if a finding could apply to any document, delete it.
   - **RISKS:** delivery and operational risks visible from the COO lens, each tied to something in the document (or to a named gap in it).
   - **WHAT WOULD CHANGE MY MIND:** the specific evidence, drawn from the persona's WHAT CONVINCES ME section, that would move the verdict up one level.
   - **5 INTERROGATION QUESTIONS:** the five questions the real executive would ask in the meeting, in the persona's voice, each anchored to the document. Exactly five.
8. **Save the review** as a Word document using the Word built-in skill, explicitly to /Documents/Cowork/reviews/<artifact-name>-coo-review.docx in the user's OneDrive. If the reviews folder does not exist, create it. Do not let the file land in a session folder: if it does, re-save it to the explicit path above.
9. **Report back in the conversation:** the verdict in one line, the full OneDrive path where the review was saved, and whether org-profile.md was used or the review was generic.

## OUTPUT ARTIFACTS

| Artifact | Exact location |
|---|---|
| COO review document (DRAFT) | `/Documents/Cowork/reviews/<artifact-name>-coo-review.docx` |

The document contains, in order: header with DRAFT label, archetype note, VERDICT, TOP FINDINGS, RISKS, WHAT WOULD CHANGE MY MIND, 5 INTERROGATION QUESTIONS. Always report the saved path in the conversation; never assume the user will go looking for it.

## FALLBACKS AND EDGE CASES

- **File not found:** use Enterprise Search, present the closest match, and get the user's confirmation before reviewing. Never silently review a different file than the one the user named.
- **Output filename already exists:** do not overwrite. Save as `<artifact-name>-coo-review-v2.docx` (then -v3 and so on) and report which version you wrote.
- **Output lands in a session folder:** re-save to /Documents/Cowork/reviews/ and report the final path. The path you report must be the path the file actually sits at.
- **org-profile.md missing:** proceed generic; include the one-line note from step 4. Do not block the review on it.
- **Pasted text instead of a file:** there are no page numbers, so cite findings by quoting the exact phrase you are reacting to.
- **Very long artifact:** review section by section rather than from a summary. Every finding still cites its specific section.
- **Multiple files named:** ask the user which one is the artifact under review. Review one document per run; list the others in the header as "not reviewed".
- **Spreadsheet-only business case:** use the Excel built-in skill to read the key tabs; cite findings by tab name and cell range.
- This skill writes no Planner or To Do items. All output is a file at the path above, so there is no silent-failure task path to fall back from.

## SAFETY RULES

- Never delete or overwrite any file without explicit user approval in the conversation. When a name collides, write a new versioned file instead.
- The review document is labelled DRAFT until a human reviews it.
- This skill never sends anything. If the user asks to email the review, create an email Draft only (Email built-in skill) and tell the user it is sitting in Drafts; never send.
- Never invent facts the artifact does not contain. Every finding, risk and question must trace to something in the document or to a named gap in it.
- Quote the artifact accurately. If you paraphrase, say so.
- The persona is a role archetype. Never present its verdict as the opinion of any real, named person.

## QUALITY SELF-CHECK

Before reporting back, confirm every box:

- [ ] references/persona.md was read in full and the review is written in its voice.
- [ ] Verdict is exactly one of: proceed / proceed with conditions / not ready.
- [ ] Every TOP FINDING quotes or cites a specific section, page, slide or cell range. No generic feedback survived.
- [ ] RISKS are tied to the document, not to a generic risk checklist.
- [ ] Exactly 5 interrogation questions, each anchored to the document.
- [ ] No facts invented beyond the artifact and org-profile.md.
- [ ] File saved to /Documents/Cowork/reviews/ with the correct name; the reported path is where the file actually is.
- [ ] DRAFT label and archetype note are present in the document.
