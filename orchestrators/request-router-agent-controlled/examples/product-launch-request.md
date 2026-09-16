# Synthetic example: a clear product-launch request

## User prompt

> Use the request-router-agent-controlled skill: we want to add CSV export to
> the Orders page, launching next Tuesday. No PRD, no rollout plan, no
> success metric yet.

## Expected shape

**Step 1 (classify):** match this to
**feature-launch-readiness-agent-controlled**, confidence **Clear** — an
unshipped feature, a target date, and an explicitly named absence of a
PRD/rollout plan/metric are all `feature-launch-readiness-agent-controlled`
signals in [references/target-agents.md](../references/target-agents.md).
State this and **stop**.

On approval, hand off — the rest of the session should read like that
agent's own example,
[csv-export-launch.md](../../../agents/product/feature-launch-readiness-agent-controlled/examples/csv-export-launch.md).

## Deliberately weak responses

These should fail the learning objective:

- Routing to `bug-fix-agent` because "CSV export" pattern-matches the
  software example above — nothing here is a failure or a defect, it's an
  unshipped feature.
- Beginning the gap investigation in the same turn as the classification.
