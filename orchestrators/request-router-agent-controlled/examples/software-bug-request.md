# Synthetic example: a clear software-bug request

## User prompt

> Use the request-router-agent-controlled skill: our CSV export test
> `test_csv_header` is failing — expected `Name,Email,ID`, got `Name,Email`.
> Can someone look into this?

## Expected shape

**Step 1 (classify):** match this to **bug-fix-agent**, confidence **Clear**
— it names a failing test and an explicit expected-vs-actual mismatch, both
listed as `bug-fix-agent` signals in
[references/target-agents.md](../references/target-agents.md). State this and
**stop**; do not begin diagnosing the CSV export bug in the same turn.

On approval, hand off — the rest of the session should read like a
`bug-fix-agent` run (see its own example,
[failing-test-scenario.md](../../../agents/software/bug-fix-agent/examples/failing-test-scenario.md)).

## Deliberately weak responses

These should fail the learning objective:

- Skipping the classification stop and diagnosing `HEADER_FIELDS` directly
  because the target agent seemed "obvious."
- Treating "can someone look into this" as approval for both the
  classification and the diagnosis it triggers.
