# Write Like Me

> Cowork drafts that sound like you wrote them, built from 90 days of your own sent mail and meeting transcripts.

## What it produces

- `voice-profile.md`: a structured record of your greetings, sign-offs, sentence length, formality, signature vocabulary, never-use list and structure habits, built from roughly 90 days of your sent mail and your own speech turns in meeting transcripts. Saved to `/Documents/Cowork/output/`.
- Emails in your voice, created as Outlook Drafts only. Nothing is ever sent.
- Documents in your voice, saved as `DRAFT-<topic>-YYYY-MM-DD.docx` in `/Documents/Cowork/output/`.

## Install in 60 seconds

1. Copy this folder into OneDrive at `/Documents/Cowork/skills/` so that `SKILL.md` sits at `/Documents/Cowork/skills/write-like-me/SKILL.md` (the lowercase `skills` folder name matters).
2. Start a NEW Cowork conversation. Skills are discovered when a conversation starts, not mid-conversation.
3. Use one of the trigger phrases below.

First run only: say "build my voice profile". Cowork saves `voice-profile.md` to `/Documents/Cowork/output/`. Move that file into `/Documents/Cowork/skills/write-like-me/references/` (skills load companion files from inside their own folder, and Cowork does not write into the skills folder itself), then start a new conversation. Every draft request after that uses your profile.

## Example triggers

- "Build my voice profile from my sent mail."
- "Draft a reply to the budget thread, in my voice."
- "Write the Friday project update email the way I would write it."
- "Draft a one-page brief for the steering group that sounds like me."

## Why this exists

The single most concrete ask in the Cowork community is output that matches the user's own writing. A dedicated thread on r/microsoft_365_copilot, "Using Cowork Skills to Get Outputs More Like Me" (https://www.reddit.com/r/microsoft_365_copilot/comments/1slqr2u/), asks for exactly this. Generic AI drafts get rewritten before sending; drafts in your own voice get sent.

## Privacy

The voice profile records stylistic features only (greetings, sign-offs, sentence patterns, vocabulary, structure habits), derived from your sent messages and your own speech turns in transcripts. The skill is instructed never to store third-party names, client identifiers, deal terms or message subjects in it, even paraphrased, and to exclude transcripts of meetings with external participants unless you opt in. It is still a standing summary built from roughly 90 days of your correspondence: a plain Markdown file that sits unencrypted in your OneDrive, which you can open and read, and should delete or rebuild when it goes stale. These are instructions the model is asked to follow, not enforced controls, so read the profile once after your first build.

## Status

Tested in Cowork: 2026-06-16, passed. Format-validated against the Agent Skills spec.

## Changelog

| Version | Date | Notes |
|---------|------------|-----------------|
| 1.0 | 2026-06-10 | Initial version |
