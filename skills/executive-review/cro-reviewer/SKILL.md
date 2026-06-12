---
name: cro-reviewer
description: Reviews a proposal, business case, deck or plan in character as a Chief Revenue Officer archetype, producing a structured review document with a verdict, evidence-cited findings, revenue risks and five interrogation questions. Use when the user asks for a CRO review, a revenue-lens pressure test, or to challenge a document the way a sales leadership executive would before a real review meeting.
---

## PURPOSE

Pressure-test a document through the eyes of a Chief Revenue Officer before it faces a real one. You read the artifact, adopt the CRO role archetype defined in references/persona.md, and produce a review document with a clear verdict, findings anchored to specific parts of the artifact, revenue risks, the evidence that would change the verdict, and the five questions the real executive would ask in the meeting.

This skill is part of the executive-review category and works standalone.

## WHEN TO RUN

- The user asks for a CRO, revenue, sales leadership or commercial review of a proposal, business case, deck, pricing plan, go-to-market plan or forecast.
- The user wants a document pressure-tested before a real executive review, board meeting or deal review.

Do not run this for general copy-editing or formatting requests; this skill judges substance through one executive lens only.

## INPUTS YOU GATHER

1. The artifact under review: a file name or path in OneDrive or SharePoint, or text the user pastes into the conversation.
2. If the artifact is pasted text, a short name (two or three words) to use in the output filename. If the user gives none, default to pasted-artifact-YYYY-MM-DD.
3. Optional: the meeting or decision this review is preparing for, so the verdict can speak to it.
4. /Documents/Cowork/org-profile.md, if it exists (checked automatically in the workflow, not requested from the user).

## WORKFLOW

1. Identify the artifact. If the user named a file without a full path, use the Enterprise Search built-in skill to locate it across OneDrive and SharePoint. If more than one candidate matches, list them and ask the user to confirm before reading anything. Open the confirmed file with the matching built-in skill: Word for .docx, PowerPoint for .pptx, PDF for .pdf, Excel for .xlsx. If the user pasted text, treat the pasted text as the artifact and confirm the short name for the output filename.
2. Read references/persona.md in full and adopt that persona for every judgement in this review. Do not soften it. Never present the persona as a real, named person, and never invent data about the business under review: where evidence is missing, say so and ask for it.
3. Check whether /Documents/Cowork/org-profile.md exists in the user's OneDrive. If it exists, read it and use it as company context for the whole review. If it does not exist, proceed generic and add one line to the review header noting that no org profile was found, and that creating one from the template in this skill's references folder would sharpen future reviews.
4. Read the artifact end to end before judging anything. Record its structure (section headings, slide numbers, page numbers) so that every finding in step 6 can cite an exact location.
5. Interrogate the artifact against the persona: work through MANDATE, all ten items in WHAT I PROBE FIRST, RED FLAGS and WHAT CONVINCES ME. For each probe, record whether the artifact answers it, dodges it, or is silent on it.
6. Write the review with exactly these five sections, in this order:
   - VERDICT: exactly one of proceed, proceed with conditions, not ready, followed by a two-sentence justification in the persona's voice. If the verdict is proceed with conditions, list the conditions as bullets.
   - TOP FINDINGS: three to seven findings, ordered by revenue impact. Each finding MUST quote the artifact directly or cite the exact slide number, page number or section heading it is about. Discard any finding you cannot anchor to a specific part of the artifact; generic feedback is not allowed.
   - RISKS: the risks this role specifically would flag (pipeline, sales motion fit, enablement burden, pricing, retention, forecast credibility), each tied to something in the artifact or to a named silence in it.
   - WHAT WOULD CHANGE MY MIND: the specific evidence, drawn from the persona's WHAT CONVINCES ME list, that would move the verdict up one level.
   - 5 INTERROGATION QUESTIONS: exactly five questions the real executive would ask in the meeting, in the persona's vocabulary and tone, ordered hardest first.
7. Use the Word built-in skill to save the review as a new file at /Documents/Cowork/reviews/<artifact-name>-cro-review.docx, where <artifact-name> is the artifact's filename without extension, or the short name from step 1, kebab-cased. Put DRAFT and today's date in the document header. Never overwrite an existing file: if the name is taken, append -v2, then -v3, and so on.
8. Confirm where the file actually landed. If it was written to a session folder instead of /Documents/Cowork/reviews/, re-save it to the explicit path before reporting.
9. Report back in the conversation: the verdict, the full confirmed path of the saved review, and whether org-profile.md was used as context.

## OUTPUT ARTIFACTS

- /Documents/Cowork/reviews/<artifact-name>-cro-review.docx: the review document, with DRAFT and the date in the header, containing the five sections from step 6.

No other files are created. The conversation reply restates the verdict and the confirmed save path.

## FALLBACKS AND EDGE CASES

- Artifact not found: if Enterprise Search returns nothing, say so, list the closest matches if any, and offer the user two options: give the exact path, or paste the text directly.
- Output lands in a session folder: re-save to /Documents/Cowork/reviews/ and report the final confirmed path. Never report a path you have not confirmed.
- /Documents/Cowork/reviews/ does not exist: create it. If creation fails, save to /Documents/Cowork/ and report that path instead, stating why.
- Word skill cannot create the file: save the identical content as /Documents/Cowork/reviews/<artifact-name>-cro-review.md and tell the user which format was used and why.
- Artifact has little revenue-relevant content (for example a pure engineering runbook): say so in the verdict justification, deliver findings only where the CRO lens genuinely applies, and suggest a better-matched reviewer from the executive-review category.
- Very long artifact (over roughly 50 pages or slides): review the executive summary plus every section that maps to the persona's MANDATE, and state in the review header exactly which sections were read.
- Planner or To Do: this skill never writes to Planner or To Do, so the known silent-failure risk does not apply here. All output goes to files.

## SAFETY RULES

- Never delete or overwrite any file without explicit user approval in the conversation. Always write new versioned files (-v2, -v3) when a name collides.
- The review document carries DRAFT in its header until a human reviews it.
- Nothing email-related is sent by this skill. If the user asks to email the review, use the Email built-in skill to create a Draft with the .docx attached, never to send.
- The persona is a role archetype. Never play it as, or attribute it to, any real, named individual.
- Never invent numbers, customer names, quotes or facts about the business under review. Every evidence gap is reported as a gap and turned into a question.

## QUALITY SELF-CHECK

- [ ] Every TOP FINDING quotes the artifact or cites an exact slide, page or section heading.
- [ ] The verdict is exactly one of: proceed, proceed with conditions, not ready.
- [ ] All five review sections are present, with exactly 5 interrogation questions, hardest first.
- [ ] The review reads in the persona's voice: numbers before narrative, direct, sceptical of vanity metrics.
- [ ] No data about the business under review was invented; every missing piece of evidence is named as missing.
- [ ] The file is saved as a new versioned file under /Documents/Cowork/reviews/ and the reported path is the confirmed final path.
- [ ] The document header contains DRAFT and today's date.
- [ ] The conversation reply states the verdict, the saved path, and whether org-profile.md was used.
