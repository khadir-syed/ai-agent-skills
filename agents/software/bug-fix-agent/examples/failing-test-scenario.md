# Synthetic example: a failing CSV export test

This fictional case can be used to test or teach the Bug Fix Agent without a
real repo, and pairs directly with the
[Test-Fix Loop Agent's transcript](../../test-fix-loop-agent/examples/sample-run-transcript.md) —
same underlying bug, different posture.

## User prompt

> Use the Bug Fix Agent on this failing test: `test_csv_header` expects the
> header `Name,Email,ID` but got `Name,Email`. Diagnose it, then propose a
> fix — don't touch anything until I approve.

## Supplied evidence

```text
FAILED tests/test_export.py::test_csv_header
AssertionError: assert 'Name,Email' == 'Name,Email,ID'
```

```python
# export.py (excerpt)
HEADER_FIELDS = ["Name", "Email"]  # ID column was dropped in a recent refactor
```

## Expected shape, stage by stage

**Stage 1 (diagnosis):** identify that `HEADER_FIELDS` is missing `"ID"`,
label this as Observed from the excerpt, and state the root cause as the
field being dropped from the list — not just "the test is failing." Stop
here; no fix proposed yet.

**Stage 2 (fix proposal):** propose adding `"ID"` back to `HEADER_FIELDS` in
`export.py`, state the file and exact change, and explicitly say no edit has
been made yet — wait for approval.

**Stage 3 (verify, after approval):** apply the change, report that
`test_csv_header` now passes, show the one-line diff, and ask for approval to
close — do not declare the bug "fixed" unilaterally.

## Deliberately weak responses

These should fail the learning objective:

- Fixing `export.py` in the same turn as the diagnosis, before any approval.
- Skipping straight to "fixed!" without re-running the test and reporting the
  actual result.
- Treating the user's initial "diagnose it, then propose a fix" as approval
  to also apply the fix.
