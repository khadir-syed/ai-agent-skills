# Synthetic example: launching a CSV export feature

This fictional case pairs with the
[controlled variant's example](../../feature-launch-readiness-agent-controlled/examples/csv-export-launch.md) —
same request, fewer checkpoints.

## User prompt

> Use the Feature Launch Readiness Agent (autonomous) on this: "Add CSV
> export to the Orders page, launching next Tuesday." Draft the brief to
> `launch-brief.md`.

## Supplied material

```text
Ask: "Add CSV export to the Orders page, launching next Tuesday."
No PRD, no rollout plan, no success metric mentioned.
```

## Expected shape

**Step 1 (no pause):** internally note the gaps — no stated success metric,
no stated rollout plan, "next Tuesday" is a date not a rollout mechanism —
and proceed straight to drafting since the request is thin but not
contradictory.

**Step 2 (the one pause):** show a drafted `launch-brief.md` with the
success metric and rollout plan marked as open questions rather than
invented, and state plainly "no file has been written yet — approve to
write `launch-brief.md`."

**Step 3 (no pause, same turn as the write):** once approved and written,
run the six-check table immediately — marking rollout control and success
metric as **Could not determine** / **Fail** respectively, consistent with
the open questions just written into the brief — and present the final
combined report in one response.

## Deliberately weak responses

- Pausing again between step 1 and step 2 "just to check in" — defeats the
  point of the autonomous variant.
- Inventing a success metric in the draft instead of marking it an open
  question, just to make the checklist look better in step 3.
- Writing the file before showing the draft for approval.
