---
name: content-publish-readiness-agent-autonomous
description: Chain the Content Brief Gap Investigator, a content draft, and the Content Publish Readiness Checklist into one run, pausing only once — right before the single write. Use for a content request that needs to go from a rough brief to a publish-readiness report in one pass; do not use when you want approval at every hand-off — use the controlled variant instead.
---

# Content Publish Readiness Agent — Autonomous

Run three steps toward one goal — is this content actually ready to
publish — proceeding through all of them without pausing, except for the
one point where something is actually written. This is the autonomous
counterpart to
[../content-publish-readiness-agent-controlled](../content-publish-readiness-agent-controlled/):
same three steps, same skills, one checkpoint instead of three.

"Autonomous" here means fewer pauses, not fewer rules — this is still a
Markdown instruction set followed by your AI CLI, and your CLI's own
approval requirements for the write itself still apply (see
[../../README.md](../../README.md)).

## Operating boundary

- Carry forward the operating boundaries of each underlying skill for its
  own step: the gap-investigation step does not draft anything; the
  readiness-checklist step does not decide whether to publish or edit
  anything.
- The **only** file write in this entire chain is the content draft in
  step 2, and it happens only after the approval described in that step.
- Label every claim across all three steps as **Stated**, **Reported**,
  **Inferred**, or **Unknown**, consistent with the Content Brief Gap
  Investigator's scheme — carry the same labels into the draft and the
  checklist rather than re-classifying them.

## Workflow

### 1. Investigate gaps (no pause)

Run the same investigation as the Content Brief Gap Investigator against the
content brief: frame the request, establish what's stated/reported/inferred/
unknown, identify conflicts, compare interpretations. Produce the gap report
internally and proceed directly to drafting — do not stop here to ask the
user to review it first.

If the brief is too thin or contradictory to draft anything useful from,
stop now rather than proceeding on invented assumptions — this is the one
exception to "no pause before step 2."

### 2. Draft the content — stop for approval before writing

Using the gap report from step 1, draft the content — see
[references/content-readiness-format.md](references/content-readiness-format.md).

Show the complete draft. **This is the one mandatory stop in this agent —
do not write the file until the user approves.** State plainly what file
this will be written to.

### 3. Run the readiness checklist (no pause)

Once the draft is approved and written, immediately run the same six checks
as the Content Publish Readiness Checklist against it (proofreading, links,
SEO basics, alt text, sourced claims, brand tone), and produce the final
report in the same turn — do not pause between the write and the checklist.

## Report and stop

Present, in one final response: the gap-report summary, the approved and
written draft, and the full readiness checklist table. State the overall
picture without making the publish decision — that's the same rule the
underlying checklist follows.

## Stopping conditions

Stop and ask, breaking the "no pause" default, when:

- step 1's gaps are severe enough that any draft would be built on invented
  assumptions;
- the draft in step 2 is not approved as-is — do not proceed to step 3 on a
  rejected or modified-without-re-approval draft;
- resolving a gap or checklist item requires a decision only a named
  stakeholder can make; or
- the user asks this agent to also decide whether to publish.

## Quality check

Before the final report, confirm that:

- the only write that occurred is the one approved in step 2;
- gap labels (stated/reported/inferred/unknown) are consistent from the
  investigation through the draft and the checklist;
- the checklist did not silently mark something as passing that the draft
  left as an open question; and
- the final summary reads as input to a publish decision, not the decision
  itself.
