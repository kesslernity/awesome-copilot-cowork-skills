# Commitment language patterns

How to decide whether a sentence is a commitment, which direction it runs, and what its due date is. Apply these rules in workflow step 5.

## Direction: MADE (the user promised someone)

Look in: messages the user SENT, and transcript lines spoken by the user.

Signals (first person, future action, identifiable deliverable):

- "I'll ...", "I will ...", "I can get that to you by ..."
- "Leave it with me", "Will do", "On it", "Consider it done"
- "I'll send / share / set up / book / review / follow up on ..."
- "Let me ..." followed by a deliverable ("Let me pull the numbers together")
- "I owe you ..."
- Accepting someone's request: a reply such as "yes", "sure", "sounds good" to a message that asks the user for something. The request being accepted defines the deliverable and any due date.

## Direction: OWED (someone promised the user)

Look in: messages the user RECEIVED, and transcript lines spoken by others.

Signals:

- "I'll get that over to you", "You'll have it by ...", "We'll send ..."
- "Leave it with me" or "On it" said by the counterparty
- The counterparty agreeing to the user's request ("sure, by Friday")
- Transcript action items assigned to someone else where the user is the requester or the recipient of the output

## Not a commitment: exclude from the ledger

- Hypotheticals and options: "we could", "maybe I'll", "one option is"
- Intentions without a deliverable: "I'll think about it", "let's see"
- Commitments that were declined or withdrawn later in the same thread
- Automated mail: newsletters, system notifications, out-of-office replies, calendar accept/decline messages
- Anything already completed within the window (use it only as evidence to mark an existing ledger entry done)
- A request that received no agreement. The other party has not committed. Keep it out of the ledger and list it in the run summary under "awaiting confirmation".

## Conditional commitments

"If the client signs, I'll book the kick-off": record it, with the condition included in the deliverable text, status open, due date "none stated" until the condition is met. Re-evaluate the condition on later runs.

## Due date extraction

- Explicit dates: record as written, normalised to YYYY-MM-DD.
- Relative phrases resolve against the timestamp of the message or meeting, not against today:
  - "tomorrow" = the next calendar day after the timestamp
  - "by Friday" = the first Friday at or after the timestamp
  - "end of week" = the Friday of the timestamp's week
  - "end of month" = the last working day of the timestamp's month
  - "next week" = the Friday of the following week
- Mark every resolved relative date "(inferred)" in the Due column.
- No date stated anywhere: record "none stated". Never invent a date.

## Counterparty naming

Use the display name from the source, plus the organisation when the person is external ("Dana Verma, Contoso"). For a commitment made to a group, name the group or channel ("the #q3-launch channel"). If the name is genuinely unclear, use what the source shows and rely on the source reference. Never guess an identity.
