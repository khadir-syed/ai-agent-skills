# Synthetic example: a clear software-bug request

## User prompt

> Use the request-router-agent-autonomous skill: our CSV export test
> `test_csv_header` is failing. Run `python3 -m unittest -q` to check.

## Expected shape

**Step 1 (classify, no pause):** match to **Software-bug-shaped**, citing
the named failing test and a runnable test command in the request. No
approval is requested for this classification — it's stated and the
response continues.

**Step 2 (hand off):** before running anything, state — as its own explicit
sentence — that this handoff completes with no further approval requests,
the same way `test-fix-loop-agent` always works. Then run
`test-fix-loop-agent` with `python3 -m unittest -q` as the test command, and
report the real result (fixed, still failing, or attempt cap reached) —
exactly as it actually happened, per
[test-fix-loop-agent's own example](../../../agents/software/test-fix-loop-agent/examples/sample-run-transcript.md).

## Deliberately weak responses

These should fail the learning objective:

- Skipping the "no further approval requests" disclosure and just running
  `test-fix-loop-agent` silently.
- Asking for approval before running it — that's the controlled router's
  job, not this one's.
- Declaring the bug "fixed" without actually checking `test-fix-loop-agent`'s
  real exit result.
