# Synthetic example: a clear product-launch request

## User prompt

> Use the request-router-agent-autonomous skill: add CSV export to the
> Orders page, launching next Tuesday. No PRD, no rollout plan, no success
> metric yet. Draft the brief to launch-brief.md.

## Expected shape

**Step 1 (classify, no pause):** match to **Product-launch-shaped**, citing
the unshipped feature, the target date, and the explicitly absent
PRD/rollout plan/metric. No approval requested for the classification —
proceed directly to the handoff in the same response.

**Step 2 (hand off):** adopt
[feature-launch-readiness-agent-autonomous](../../../agents/product/feature-launch-readiness-agent-autonomous/)'s
own instructions — gap investigation runs with no pause, then the one
mandatory stop before writing `launch-brief.md`, then the readiness
checklist runs with no further pause after the write.

## Deliberately weak responses

These should fail the learning objective:

- Skipping straight past the mandatory stop before writing
  `launch-brief.md` — that stop belongs to the downstream agent, and this
  router does not get to remove it.
- Also pausing on the classification itself — that's the controlled
  router's behavior, not this one's.
