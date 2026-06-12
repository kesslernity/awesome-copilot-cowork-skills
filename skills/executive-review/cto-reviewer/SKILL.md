---
name: cto-reviewer
description: Reviews a proposal, business case, deck or plan in character as a Chief Technology Officer archetype, producing a structured DRAFT review document with a verdict, findings cited to specific parts of the artifact, technology risks and five interrogation questions. Use when the user wants a CTO review, a technical pressure-test of a document, or to rehearse the technology seat of an executive review before the real meeting.
---

## PURPOSE

Review one business artifact (proposal, business case, deck or plan) through the eyes of a Chief Technology Officer archetype, and produce a review document the author can act on before facing a real executive. The review is specific to the artifact: every finding quotes or cites the exact part it is about. The output is a Word document saved to a known OneDrive path.

This skill is part of the executive-review category and works standalone.

## WHEN TO RUN

Run when the user asks for a CTO review, a technical pressure-test, a technology-lens critique of a document, or "what would a CTO ask about this". Do not run for general copy-editing, formatting or summarisation requests.

## INPUTS YOU GATHER

1. The artifact under review: a file the user names (search OneDrive and SharePoint via the Enterprise Search built-in skill if no path is given) or text the user pastes into the conversation.
2. A short kebab-case artifact name for the output filename. Derive it from the file name (for example `q3-platform-migration.docx` gives `q3-platform-migration`). If the artifact is pasted text with no obvious name, ask the user for a two-to-four word name before writing any file.
3. Optional: any specific concern the user wants probed hardest (for example "focus on the vendor terms"). Fold it into the review; do not skip the standard structure.
4. Company context, checked automatically in step 3 of the workflow: `/Documents/Cowork/org-profile.md`.

## WORKFLOW

1. Identify and read the artifact. If the user named a file, open it with the matching built-in skill: Word for .docx, PowerPoint for .pptx, Excel for .xlsx, PDF for .pdf. If only a title was given, use the Enterprise Search built-in skill to find it; if more than one file matches, list the matches with their paths and ask the user to pick one. Never guess. If the user pasted text, treat the pasted text as the artifact.
2. Load `references/persona.md` from this skill folder and stay strictly in character for the entire review: mandate, probes, red flags, evidence standards, vocabulary and tone. The persona is a role archetype, never a real, named individual.
3. Check whether `/Documents/Cowork/org-profile.md` exists in the user's OneDrive. If it exists, load it and use it as company context throughout the review. If it does not exist, proceed with a generic review and add one line under the review header: "No org profile found. A filled-in /Documents/Cowork/org-profile.md would sharpen this review; the template is in this skill's references folder."
4. Map the artifact against the persona. Work through the ten WHAT I PROBE FIRST items, the RED FLAGS list and the WHAT CONVINCES ME evidence standards, noting for each where the artifact answers, dodges or is silent. Record the exact location of each observation: quoted sentence, section heading, slide number or page number.
5. Compose the review with exactly these five sections, in this order:
   - **VERDICT**: one of `proceed`, `proceed with conditions`, `not ready`, followed by a two-to-three sentence justification. If `proceed with conditions`, list the conditions as numbered items.
   - **TOP FINDINGS**: three to seven findings, strongest first. Every finding must quote or cite the specific part of the artifact it is about (quoted phrase, section, slide or page). No finding may be generic enough to apply to a different document.
   - **RISKS**: risks visible from the CTO lens only (architecture and scalability, technical debt, build versus buy, security of design, engineering capacity and sequencing, vendor lock-in). For each risk state what in the artifact triggers it.
   - **WHAT WOULD CHANGE MY MIND**: the specific evidence, per the persona's WHAT CONVINCES ME section, that would move the verdict up one level.
   - **5 INTERROGATION QUESTIONS**: exactly five questions the real executive would ask in the meeting, in the persona's voice, each answerable on the spot by a prepared author.
6. Use the Word built-in skill to create the review document. Title it "CTO Review (DRAFT): <artifact name>", with a header block listing the date (today), the artifact reviewed (filename or "pasted text"), the persona ("Chief Technology Officer, role archetype, not a real individual") and whether an org profile was used.
7. Save the document as `<artifact-name>-cto-review.docx` in `/Documents/Cowork/reviews/`. Create the folder if it does not exist. If a file with that name already exists, do not overwrite it: save as `<artifact-name>-cto-review-v2.docx` (then -v3 and so on) and tell the user why.
8. Verify the file is at the exact path you intended, not in a temporary session folder. If it landed anywhere else, save a copy to `/Documents/Cowork/reviews/` and use that as the path of record.
9. Report back in the conversation: the verdict, the single strongest finding, and the full saved path of the document. Mention that the other standalone reviewers are available if the user wants more seats at the table.

## OUTPUT ARTIFACTS

- `/Documents/Cowork/reviews/<artifact-name>-cto-review.docx`: the review document with the five sections from step 5, labelled DRAFT in the title and header. This is the only file this skill writes. The artifact under review is never modified.

## FALLBACKS AND EDGE CASES

- **File not found**: ask the user for the exact OneDrive or SharePoint path, or to paste the text. Do not review from memory of a similarly named document.
- **Multiple matches in search**: list each match with its full path and last-modified date and ask the user to choose.
- **Unsupported format** (for example an email thread or an image): ask the user to paste the text content into the conversation and review that.
- **Very long artifact** (over roughly 50 pages or 60 slides): review the executive summary plus the sections that map to the persona's focus areas, and state in the review header exactly which sections were covered and which were not.
- **`references/persona.md` missing**: stop and tell the user the skill folder was copied incompletely (the references subfolder is missing) and to re-copy the whole `cto-reviewer` folder. Do not improvise a persona.
- **Output saved to a session folder instead of the named path**: re-save to `/Documents/Cowork/reviews/` and report the corrected path. Always state in the conversation where the file actually is.
- **No org profile**: proceed generic, note it in the review header as described in step 3. Never invent company facts.

## SAFETY RULES

- Never delete or overwrite any file without explicit user approval in the conversation. Name collisions get a new versioned filename instead.
- Never modify the artifact under review. This skill reads it and writes one new file.
- The review document is labelled DRAFT in its title and header until a human reviews it.
- If the user asks to email the review to anyone, use the Email built-in skill to create a Draft only. Never send.
- The persona is a role archetype. Never present the review as the opinion of any real, named person, and never adopt a real individual's identity even if the user asks.
- Never invent facts about the user's company, vendors, systems or numbers. Everything in the review traces to the artifact, the org profile or the persona's general standards.

## QUALITY SELF-CHECK

Before reporting completion, confirm every box:

- [ ] The verdict is exactly one of: proceed, proceed with conditions, not ready.
- [ ] Every TOP FINDING quotes or cites a specific quoted phrase, section, slide or page of the artifact.
- [ ] No finding would fit a different document unchanged.
- [ ] Risks stay inside the CTO lens and each names its trigger in the artifact.
- [ ] There are exactly five interrogation questions, in the persona's voice.
- [ ] The org profile was loaded, or its absence is noted in the review header.
- [ ] The document title and header carry the DRAFT label and the archetype disclaimer.
- [ ] The file is saved at `/Documents/Cowork/reviews/<artifact-name>-cto-review.docx` (or a -vN variant), the path was verified, and the full path was reported to the user.
- [ ] The artifact under review was not modified, and nothing was sent or deleted.
