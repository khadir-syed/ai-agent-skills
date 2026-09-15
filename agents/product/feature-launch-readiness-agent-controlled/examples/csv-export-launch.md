# Synthetic example: launching a CSV export feature

This fictional case pairs with the
[autonomous variant's example](../../feature-launch-readiness-agent-autonomous/examples/csv-export-launch.md) —
same request, a checkpoint at every hand-off.

## User prompt

> Use the Feature Launch Readiness Agent (controlled) on this: "Add CSV
> export to the Orders page, launching next Tuesday." Draft the brief to
> `launch-brief.md`.

## Supplied material

```text
Ask: "Add CSV export to the Orders page, launching next Tuesday."
No PRD, no rollout plan, no success metric mentioned.
```

## Expected shape

**Step 1 (stop):** present the gap report — no stated success metric, no
stated rollout plan, "next Tuesday" is a date not a mechanism — and ask
explicitly whether to proceed to drafting given these gaps, or resolve them
with a stakeholder first. Do not draft anything yet.

**Step 2 (stop, separate approval):** once told to proceed, show the drafted
`launch-brief.md` with the same open questions preserved, and ask
specifically for approval to write this file — approval to proceed from
step 1 does not count as approval to write.

**Step 3 (stop, separate turn):** once the file is written, run the
six-check table in its own turn and wait for the user's acknowledgement
before considering the run complete — do not bundle it into the same
response as the write.

## Deliberately weak responses

- Treating "yes, proceed" from step 1 as also covering the write in step 2.
- Compressing steps 2 and 3 into one response the way the autonomous variant
  does — that defeats the point of the controlled variant.
- Skipping the step 1 pause because the request "seems simple enough."
