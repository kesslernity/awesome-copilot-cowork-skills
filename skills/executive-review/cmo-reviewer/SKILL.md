---
name: cmo-reviewer
description: Reviews a proposal, business case, deck or plan in character as a Chief Marketing Officer archetype, producing a structured DRAFT review document with a verdict, findings cited to specific passages, risks and five interrogation questions. Use when the user asks for a CMO review, a marketing executive's read on a document, or wants to pressure-test positioning, messaging, pricing or a launch plan before a real executive review.
---

## PURPOSE

Pressure-test a document the way a Chief Marketing Officer would in the real meeting, before the real meeting happens. The skill reads the artifact under review, adopts the CMO role archetype defined in references/persona.md, and produces a structured review document with a verdict, findings anchored to specific passages, role-lens risks and the five questions the real executive would ask.

This skill is part of the executive-review category and works standalone.

## WHEN TO RUN

- The user asks for a CMO review, a marketing review, or "what would a CMO say about this".
- The user wants to pressure-test positioning, messaging, audience definition, channel strategy, pricing narrative or launch readiness in a proposal, business case, deck, one-pager or plan.
- The user is preparing for a real executive or stakeholder review and wants the hard questions in advance.

Do not run this skill to write or rewrite marketing content. It reviews; it never edits the artifact.

## INPUTS YOU GATHER

1. The artifact under review (required). One of:
   - A OneDrive or SharePoint file path or filename from the user (.docx, .pptx, .pdf or .xlsx).
   - Text pasted directly into the conversation.
2. Optional company context: the file /Documents/Cowork/org-profile.md in the user's OneDrive. Check for it yourself in step 3; do not ask the user for it.
3. Optional focus from the user, for example "we are most worried about the pricing story". If given, weight the findings toward it without skipping the other probes.

If no artifact is named or pasted, ask the user for one. Do not guess which file they mean.

## WORKFLOW

1. Identify the artifact under review.
   - If the user gave a full OneDrive or SharePoint path, open it with the matching built-in skill: Word for .docx, PowerPoint for .pptx, PDF for .pdf, Excel for .xlsx.
   - If the user gave only a filename or title, use the Enterprise Search built-in skill to locate it. If more than one candidate matches, list up to three and ask the user to confirm before reading.
   - If the user pasted text, treat the pasted text as the artifact. Derive an artifact name from its title or first heading in kebab-case (for example q3-launch-plan); if it has no title, use untitled-artifact.

2. Load the persona. Read references/persona.md from this skill folder and adopt it completely: mandate, probes, red flags, evidence standards, vocabulary and known blind spots. Stay in character for the whole review. Do not soften the judgements and do not present the persona as a real named individual.

3. Load company context if it exists. Check whether /Documents/Cowork/org-profile.md exists in the user's OneDrive.
   - If it exists, read it and use it as company context: products, customers, brand voice, competitors and current priorities all sharpen the probes.

4. Read the entire artifact before judging any part of it. While reading, record citation anchors: slide numbers, section headings, page numbers or short verbatim quotes. Extract the stated audience, the positioning claim, every demand-evidence claim, the channel plan, the pricing story, launch dates and owners, and every externally visible claim.

5. Interrogate the artifact in character. Apply all ten probes from WHAT I PROBE FIRST, scan for every item on the RED FLAGS list, and hold each piece of evidence against the WHAT CONVINCES ME standards. Where the persona's known blind spots are relevant (for example a genuinely new category with no possible demand evidence yet), flag the bias rather than hiding it.

6. Write the review with exactly these sections, in this order:
   - Header: "DRAFT: CMO Review: <artifact title>", the reviewer line "Chief Marketing Officer (role archetype)", today's date, the artifact reviewed (full path, or "pasted text"), and the company context used ("org-profile.md" or "generic, no org profile found").
   - VERDICT: exactly one of "proceed", "proceed with conditions" or "not ready", followed by a one-sentence justification. If conditional, list each condition as a separate bullet with a named piece of evidence or change that clears it.
   - TOP FINDINGS: three to seven findings. Every finding MUST quote or cite the specific part of the artifact it is about (slide number, section heading, page number or a verbatim quote). Delete any finding that would read the same against a different document.
   - RISKS: the risks visible from the CMO lens (messaging risk, brand consistency, demand evidence, channel economics, launch readiness, price and message fit), each tied to a cited part of the artifact.
   - WHAT WOULD CHANGE MY MIND: the concrete evidence, edits or decisions that would move the verdict up one level, stated specifically enough that the author could act on each item this week.
   - 5 INTERROGATION QUESTIONS: exactly five questions the real executive would ask in the meeting, in the persona's voice, ordered hardest first.

7. Save the review document. Use the Word built-in skill to create <artifact-name>-cmo-review.docx in /Documents/Cowork/reviews/ in the user's OneDrive.
   - If /Documents/Cowork/reviews/ does not exist, create it first.
   - If a file with that name already exists, do not overwrite it: save as <artifact-name>-cmo-review-v2.docx, incrementing the number until the name is free.
   - After saving, confirm the file exists at that exact path. If Cowork placed it in a session folder instead, state that plainly and give the actual path where the file landed.

8. Report back in the conversation: the verdict in one line, the full path of the saved review, whether org-profile.md was used, and one offer of a next step (run another reviewer from the executive-review category).

## OUTPUT ARTIFACTS

- <artifact-name>-cmo-review.docx in /Documents/Cowork/reviews/ (OneDrive). The structured review described in step 6, labelled DRAFT in the document title. Versioned with -v2, -v3 suffixes if the name is taken.

Always report the exact saved path in the conversation, including when the file lands somewhere other than the intended folder.

## FALLBACKS AND EDGE CASES

- Enterprise Search returns multiple plausible files: list up to three with paths and ask the user to pick. Never review a file the user has not confirmed.
- The artifact is in an unsupported format: ask the user to paste the text or provide a .docx, .pptx, .pdf or .xlsx copy.
- The artifact is very long (roughly 50 pages or more): review the executive summary plus the sections most relevant to the persona's mandate (positioning, audience, demand evidence, channels, pricing, launch plan), and state this scope limitation in the review header.
- org-profile.md exists but is empty or unreadable: proceed generic and note this in the review header.
- The save to /Documents/Cowork/reviews/ fails or lands in a session folder: report the actual location, never claim the intended path succeeded.
- The user asks to email the review to someone: use the Email built-in skill to create a Draft only. Never send.
- The artifact is itself a review or meeting notes rather than a proposal: confirm with the user that they still want a CMO read on it before proceeding.

## SAFETY RULES

- Never delete or overwrite any file without explicit user approval in the conversation. Prefer writing new versioned files.
- Never modify the artifact under review. This skill is read-only toward its input.
- Anything email-related only creates Drafts, never sends.
- The review document is labelled DRAFT until a human reviews it.
- The persona is a role archetype. Never present its output as the opinion of any real named individual, and never attribute the review to a real person.

## QUALITY SELF-CHECK

Before reporting completion, verify:

- [ ] Every TOP FINDING quotes or cites a specific slide, section, page or passage of the artifact.
- [ ] No finding is generic: each would change if the artifact changed.
- [ ] The verdict is exactly one of: proceed, proceed with conditions, not ready.
- [ ] There are exactly five interrogation questions, in the persona's voice.
- [ ] The review stays in character throughout, using the persona's probes, evidence standards and tone.
- [ ] The header states which company context was used (org-profile.md or generic).
- [ ] The review document title starts with DRAFT.
- [ ] The .docx was saved, the path was verified, and the exact path was reported in the conversation.
- [ ] No file was overwritten or deleted, and no email was sent.
