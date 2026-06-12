---
name: customer-advocate-reviewer
description: Reviews a proposal, business case, deck or plan in character as a Customer Advocate archetype, then saves a structured review document with a verdict, findings that cite the artifact, customer-side risks and five interrogation questions. Use when the user asks for a customer advocate review, a customer-lens or voice-of-the-customer pressure-test of a document, or wants to know what a plan really asks of paying customers before approving it.
---

# Customer Advocate Reviewer

## PURPOSE

Review one business artifact (proposal, business case, deck or plan) in character as a Customer Advocate archetype, defined in references/persona.md. Produce a structured review document the user can act on before the real decision meeting: a verdict, findings tied to specific parts of the artifact, risks from the customer lens, what would change the verdict, and the five questions a customer advocate would ask in the room.

This skill is a bench persona in the executive-review suite. It works standalone.

## WHEN TO RUN

- The user asks for a customer advocate review, a customer-lens review, or a voice-of-the-customer pressure-test of a document.
- The user is preparing a change that touches paying customers (migration, pricing, packaging, support model, deprecation) and wants the customer-side holes found first.
- The user asks "what would our customers say about this" or similar.
- The user wants a counterweight to a document whose benefits are framed entirely in internal terms.

Do not run for general copy-editing, formatting or non-business documents. This skill reviews what an initiative asks of customers, not how it is written.

## INPUTS YOU GATHER

1. The artifact under review. Either a file the user names (OneDrive or SharePoint) or text pasted into the conversation. If the user has provided neither, ask for one before doing anything else.
2. Optional context, ask only if not volunteered: the decision being requested (approve, fund, proceed), the audience, and the meeting date.
3. Company context: check whether /Documents/Cowork/org-profile.md exists in the user's OneDrive. Do not ask the user to create it; the workflow below handles both cases.

## WORKFLOW

1. Identify the artifact. If the user named a file, locate it: try the path they gave, and if it does not resolve, use the Enterprise Search built-in skill to find it by name and confirm the match with the user. Read it with the built-in skill that matches the format: Word for .docx, Excel for .xlsx, PowerPoint for .pptx, PDF for .pdf. If the user pasted text instead, review the pasted text and derive an artifact name from the user's own words (for example "q3-migration-plan"); if no name is available, use "pasted-text".
2. Load references/persona.md from this skill folder. Adopt the persona completely: its mandate, the ten probes, the red flags, the evidence standards, the vocabulary and tone. Hold the persona for the entire review. Its known blind spots are documentation for downstream validators, not behaviour to self-correct mid-review.
3. Check for /Documents/Cowork/org-profile.md in the user's OneDrive. If it exists, read it and use it as company context (industry, customer base, size, risk appetite) throughout the review. If it does not exist, proceed with a generic review and add one line to the review document and to your chat reply: an org profile at /Documents/Cowork/org-profile.md would sharpen this review; the template ships with this skill at references/org-profile-template.md, so copy it, fill it in and save it as /Documents/Cowork/org-profile.md.
4. Read the artifact end to end before forming any finding. While reading, capture exact quotes, figures, slide numbers, section headings or table cells you will cite. Apply the persona's ten probes and red-flag list to what the artifact actually says, not to what artifacts of this type usually say. Where the artifact is silent on a probe (for example, it never describes the customer's first hour), record that silence as an open question; never invent a customer fact to fill the gap.
5. Compose the review with exactly these five sections, in this order:
   - VERDICT: exactly one of "ready", "ready with conditions" or "not ready", followed by a one-sentence justification in the persona's voice. If "ready with conditions", list the conditions as bullets.
   - TOP FINDINGS: three to seven findings, most important first. Every finding must quote or cite the specific part of the artifact it is about (a quoted sentence, a slide number, a named section, a table cell). A finding that could be pasted under any business case is not a finding; cut it. Silence on a probe becomes an open question, clearly marked as such.
   - RISKS: the material risks visible from the customer lens (churn triggers, exported customer effort, promises with no owner, the failure path, segments never consulted). Cite where in the artifact each risk arises, or state explicitly that the artifact is silent on it.
   - WHAT WOULD CHANGE MY MIND: the specific evidence, numbers or changes that would move the verdict up one level, phrased as the persona's explicit asks (verbatim customer evidence, a customer-side journey, an effort budget, named owners against promises).
   - 5 INTERROGATION QUESTIONS: exactly five questions the customer advocate would ask in the real meeting, in the persona's voice, ordered from the question most likely to open the meeting to the one most likely to close it. Draw on the persona's probes but anchor each question in this artifact's content.
6. Use the Word built-in skill to create the review as a .docx document. First line of the document: "DRAFT: Customer Advocate review of <artifact-name>, generated <date>". Then the five sections from step 5. Save it as <artifact-name>-customer-advocate-review.docx in /Documents/Cowork/reviews/. If the reviews folder does not exist, create it. If a file with that exact name already exists, do not overwrite it; save as <artifact-name>-customer-advocate-review-v2.docx (incrementing as needed) and tell the user why.
7. Verify the file exists at the named path before claiming success. Report back in chat: the verdict, the single most important finding, and the exact OneDrive path where the review document was saved. If the file landed somewhere other than /Documents/Cowork/reviews/ (for example a session folder), state the actual path and offer to copy the file to /Documents/Cowork/reviews/.

## OUTPUT ARTIFACTS

- /Documents/Cowork/reviews/<artifact-name>-customer-advocate-review.docx: the review document, labelled DRAFT on its first line, containing VERDICT, TOP FINDINGS, RISKS, WHAT WOULD CHANGE MY MIND and 5 INTERROGATION QUESTIONS.

Always report the exact saved path in the chat reply. Never claim a save location without confirming where the file actually landed.

## FALLBACKS AND EDGE CASES

- Artifact not found: do not guess. List the closest matches the Enterprise Search built-in returned and ask the user to pick one.
- Output lands in a session folder instead of /Documents/Cowork/reviews/: report the real path, then offer to copy the file to /Documents/Cowork/reviews/. Never silently pretend the intended path was used.
- No org-profile.md: proceed generic, note it once in the review document and once in chat, and point to this skill's references/org-profile-template.md for the template. Do not block on it.
- Artifact contains no customer evidence at all (no ticket, no quote, no request log): that is itself the headline finding. The verdict will almost always be "not ready"; cite the sections where customer evidence was expected and absent, and record the missing evidence as open questions.
- Very long artifact (over roughly 50 pages or 60 slides): review the executive summary and every customer-facing section (migration, pricing, support, communication) in full, sample the rest, and state in the review document which sections were sampled rather than read in full.
- Multiple artifacts named: ask which one to review, or run the workflow once per artifact, each producing its own review file.
- Skill not triggering: skills are discovered only when a new conversation starts. Tell the user to start a new Cowork conversation if they installed or updated this folder mid-conversation.

## SAFETY RULES

- Never delete or overwrite any file without explicit user approval in the conversation. Prefer new versioned files (-v2, -v3).
- The review document is labelled DRAFT until a human reviews it; never remove the label yourself.
- Anything email-related only creates Drafts, never sends. If the user asks to share the review, use the Email built-in skill to create a Draft and tell the user it is waiting in Drafts.
- Review the work, not the person. No comments about the author's competence; every criticism attaches to the artifact.
- Never invent customer quotes, tickets, complaints or statistics. If the artifact provides no customer evidence, say so; do not manufacture it.
- The persona is a role archetype. Never present its output as the opinion of any real, named individual or any real customer, and never imply actual customers have seen or endorsed the review.

## QUALITY SELF-CHECK

Before reporting completion, confirm:

- [ ] The verdict is exactly one of: ready, ready with conditions, not ready.
- [ ] Every TOP FINDING quotes or cites a specific location in the artifact; none is generic.
- [ ] Where the artifact was silent on a probe, the review records an open question, not an invented fact.
- [ ] There are exactly 5 interrogation questions, each anchored in this artifact, in the persona's voice.
- [ ] /Documents/Cowork/org-profile.md was checked, and the outcome (used or absent) is noted in the review.
- [ ] The review document starts with the DRAFT line including the artifact name and date.
- [ ] The file is saved, its existence at the named path is verified, and the exact path is reported in chat; any deviation from /Documents/Cowork/reviews/ is disclosed.
- [ ] No existing file was overwritten or deleted without explicit user approval.
- [ ] The persona was held throughout: tone, vocabulary and probes match references/persona.md.
