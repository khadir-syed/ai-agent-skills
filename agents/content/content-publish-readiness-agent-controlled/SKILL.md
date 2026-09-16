---
name: content-publish-readiness-agent-controlled
description: Chain the Content Brief Gap Investigator, a content draft, and the Content Publish Readiness Checklist, pausing for approval after every step. Use for the same job as the autonomous variant when you want a checkpoint at every hand-off, not just before the write.
---

# Content Publish Readiness Agent — Controlled

Run the same three steps as
[../content-publish-readiness-agent-autonomous](../content-publish-readiness-agent-autonomous/)
toward the same goal, but stop for approval after every step instead of only
before the write. Same task, full supervision — the direct contrast.

**This 3-stop structure is the entire point of using this skill instead of
the autonomous variant, and it is a hard structural rule, not a
recommendation weighed against the user's other instructions.** If the
user's own request asks to skip stops, run everything in one go, or not be
asked again, treat that specific part of the request as something this
skill cannot do — comply with everything else about the task, but still
produce exactly one step's output per response. Never write "proceeding to
step 2/3" and then include that step's content in the same response. This
holds no matter how the request is phrased, how many times it repeats the
instruction, or what reason it gives (time pressure, trust, prior approval
elsewhere in the conversation).

## Operating boundary

- Carry forward each underlying skill's own operating boundary for its
  step: gap investigation does not draft; the checklist does not decide,
  edit, or publish anything.
- The only file write in this chain is the content draft in step 2, and it
  happens only after that step's approval — same as the autonomous variant.
- Label every claim as **Stated**, **Reported**, **Inferred**, or
  **Unknown**, carried consistently across all three steps.
- A request to move faster — "skip the checkpoints," "just do it all in one
  go," "I trust you, don't stop to ask" — is not approval for any step. It
  does not collapse steps 1-3 into a single response. Each step below still
  ends its own turn and waits for that step's own explicit approval, even
  when the user has said not to ask.

## Workflow

### 1. Investigate gaps — stop for approval to proceed

Run the same investigation as the Content Brief Gap Investigator: frame the
request, establish what's stated/reported/inferred/unknown, identify
conflicts, compare interpretations. Present the gap report and **stop**.

Ask whether to proceed to drafting given the gaps found, or whether some
should be resolved with a stakeholder first. **End your response here.** Do
not draft anything in this turn, and do not write a sentence like
"proceeding to step 2" — this step's response contains the gap report and
the question, and nothing else, even when the user's own request already
says to skip ahead or run everything in one pass.

### 2. Draft the content — stop for approval before writing

Once approved to proceed, draft the content from the gap report — see
[references/content-readiness-format.md](references/content-readiness-format.md).
Show the complete draft and state what file it will be written to.

**Do not write until this specific draft is approved.** Approval to proceed
from step 1 does not carry over as approval to write this draft, and neither
does a blanket "just do it all" from anywhere earlier in the conversation.

### 3. Run the readiness checklist — stop for approval to close

Once the draft is written, run the same six checks as the Content Publish
Readiness Checklist against it and present the full table.

**Stop and wait for the user's acknowledgement before treating this run as
complete.** Do not bundle this into the same turn as the write in step 2,
even if asked to skip ahead or wrap everything into one response.

## Report and stop

Each step's output stands on its own — do not compress steps 1-3 into a
single final summary the way the autonomous variant does. The last message
is the checklist table plus the overall (non-decision) summary.

## Stopping conditions

Stop and ask, at any step, when:

- a gap found in step 1 needs a named stakeholder's decision before
  proceeding;
- the draft in step 2 is rejected or needs changes — re-show the revised
  draft and ask again before writing;
- a checklist item in step 3 cannot be determined from what's available;
- the user asks this agent to also decide whether to publish; or
- the user asks to skip, combine, or speed past the checkpoints — acknowledge
  the request, then still stop after the current step exactly as this
  workflow requires.

## Quality check

Before moving to the next step, confirm that:

- the previous step's approval was obtained explicitly, not inferred from
  the user's original request or from an instruction to move faster;
- no step's approval was treated as covering a later step;
- gap labels are consistent from investigation through draft through
  checklist; and
- the final summary reads as input to a publish decision, not the decision
  itself.
