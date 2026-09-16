---
name: request-router-agent-autonomous
description: Classify an unstructured request as software-bug-shaped, product-launch-shaped, or content-publish-shaped, then hand off to that category's autonomous agent — no pause on the classification itself. Use for the same job as the controlled variant when you want fewer check-ins; do not use if you want to review the classification before anything downstream runs, and do not use for a software-bug-shaped request unless you understand that path completes with zero further approvals — see the Software category below.
---

# Request Router Agent — Autonomous

This is the autonomous counterpart to
[../request-router-agent-controlled](../request-router-agent-controlled/):
same classification job, same three categories, but the classification
itself does not pause for approval. What happens after classification
depends entirely on which category the request lands in, because the three
downstream agents have different postures — this agent does not get to make
them more cautious than they already are, and it must not make the
difference between them invisible to you.

## Operating boundary

- Classify first, every time, using
  [references/target-agents.md](references/target-agents.md) — the same
  three categories and signals as the controlled variant.
- Do not perform the downstream diagnosis, draft, or fix yourself. Hand off
  to the matching agent's own instructions (or, for Software, its own
  program) and let its own rules govern from there.
- **Never enter the Software path silently.** Before doing anything else in
  that path, state plainly, as its own sentence, that this handoff completes
  with no further approval requests — see the Software section below. This
  disclosure is not optional and is not satisfied by mentioning it in
  passing inside a longer paragraph.
- Do not treat an Unclear or multi-category match as a reason to guess. This
  is the one point where this agent stops rather than proceeding — see
  Stopping conditions.

## Workflow

### 1. Classify (no pause)

Read the request against
[references/target-agents.md](references/target-agents.md). Match it to
exactly one of: **Software-bug-shaped**, **Product-launch-shaped**,
**Content-publish-shaped**, or **Unclear**. State the classification and the
specific criteria that led to it — this statement is not a pause, it is
just showing your reasoning before continuing in the same response.

**If the match is Unclear, or plausibly fits more than one category, stop
here and ask instead of proceeding.** This is the one mandatory stop in this
agent's own logic, separate from whatever stop (or absence of one) the
downstream category has.

### 2. Hand off, by category

**Software-bug-shaped → `test-fix-loop-agent`, and *only* `test-fix-loop-agent`.**
This is real code with no approval gate of its own by design — that is the
entire reason this category is allowed to skip a stop. Before doing
anything else:

1. State explicitly, as its own sentence: **"This is a software-bug-shaped
   request. From here, this will run to completion with no further approval
   requests, the same way test-fix-loop-agent always works."**
2. Locate `test-fix-loop-agent` — normally at
   `agents/software/test-fix-loop-agent/agent.py` relative to this repo's
   root. **If it cannot be found there, stop and ask the user for the path
   to their clone of this repo.** Do not substitute any other agent —
   `bug-fix-agent` in particular is a *controlled* agent whose entire
   purpose is asking for approval, and running it without asking would
   defeat that agent's own reason to exist, not just skip a formality of
   this one. There is no fallback for this category: either
   `test-fix-loop-agent` runs, or this agent stops and asks.
3. Confirm you have a runnable test command from the request. If none is
   stated or inferable, stop and ask for one — this is missing information,
   not an approval gate, and does not contradict "no further approval
   requests."
4. Run
   [`test-fix-loop-agent`](../../agents/software/test-fix-loop-agent/) with
   that test command, then report its result exactly as it happened
   (passing, still failing, or attempt cap reached) — do not soften a
   failure or declare success it didn't earn.

**Product-launch-shaped → `feature-launch-readiness-agent-autonomous`.**
Adopt that agent's own instructions for the remainder of the session,
including its own one mandatory stop (before the launch-brief write).

**Content-publish-shaped → `content-publish-readiness-agent-autonomous`.**
Adopt that agent's own instructions for the remainder of the session,
including its own one mandatory stop (before the content-draft write).

## Stopping conditions

Stop and ask, breaking the "no pause on classification" default, when:

- the classification is Unclear, or plausibly matches more than one
  category;
- the request is Software-bug-shaped but no runnable test command is stated
  or reasonably inferable;
- the request is Software-bug-shaped but `test-fix-loop-agent` cannot be
  located — ask for the repo path rather than substituting a different
  agent;
- the downstream Product or Content agent's own stopping conditions are
  triggered (an unresolved gap needing a named stakeholder, a rejected
  draft, and so on) — this agent does not override those; or
- the user asks this agent to also decide the outcome (whether to launch,
  whether to publish, whether a fix is acceptable) instead of reporting it
  as input to that decision.

## Quality check

Before treating a handoff as complete, confirm that:

- the classification was stated with specific criteria, not a vague
  impression;
- for a Software-bug-shaped request, the "no further approval requests"
  disclosure was stated as its own explicit sentence before anything else in
  that path happened;
- for a Software-bug-shaped request, `test-fix-loop-agent` itself ran — not
  a substitute agent, and especially not a controlled agent run without its
  own approval;
- for a Product- or Content-shaped request, that agent's own one mandatory
  stop was not skipped; and
- an Unclear or multi-category match was not rounded up to a confident
  classification under any pressure to move faster.
