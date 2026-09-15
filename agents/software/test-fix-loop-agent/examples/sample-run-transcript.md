# Synthetic example: a two-attempt fix, and a cap-hit run

These fictional transcripts show what `agent.py` actually prints — no real
repo needed to read them.

## Command

```bash
python3 agent.py "pytest -q" --max-attempts 3
```

## Run A: fixed on the second attempt

```text
=== Attempt 1/3: running tests ===
Tests failed. Output:
FAILED tests/test_export.py::test_csv_header - AssertionError: assert 'Name,Email' == 'Name,Email,ID'

=== Attempt 1: asking 'claude' for the smallest fix ===
[claude edits export.py, adds the missing ID column to the header]

=== Attempt 2/3: running tests ===
Tests passed after 1 fix attempt(s).
```

Exit code: `0`.

## Run B: cap hit, handed back to the human

```text
=== Attempt 1/3: running tests ===
Tests failed. Output:
FAILED tests/test_export.py::test_csv_header - AssertionError: assert 'Name,Email' == 'Name,Email,ID'

=== Attempt 1: asking 'claude' for the smallest fix ===
[claude edits export.py]

=== Attempt 2/3: running tests ===
Tests failed. Output:
FAILED tests/test_export.py::test_csv_header - AssertionError: assert 'Name,Email,Id' == 'Name,Email,ID'

=== Attempt 2: asking 'claude' for the smallest fix ===
[claude edits export.py again]

=== Attempt 3/3: running tests ===
Tests failed. Output:
FAILED tests/test_export.py::test_csv_header - AssertionError: assert 'Name,Email,ID ' == 'Name,Email,ID'

Stopping: 3 attempt(s) made, tests still failing. Handing back to you — see the last test output above.
```

Exit code: `1`.

## What this is meant to teach

Run B is the important one: the loop keeps getting close (a casing typo, then
a trailing space) without ever quite landing it, and the cap stops it rather
than letting it flail indefinitely. A human looking at three near-misses in a
row can spot the actual pattern (something is appending whitespace) in a way
the agent, prompted fresh each time with no memory of prior attempts,
couldn't.

## Deliberately weak "improvements" to this agent

These would defeat the point of the safety design, not make it better:

- Removing or raising the cap "so it keeps trying" — turns a bounded loop
  into an unbounded one.
- Auto-committing each attempt so "nothing is lost" — removes the clean,
  reversible working tree the safety notes rely on.
- Having the agent decide for itself that a test is "wrong" and edit the test
  instead of the code — this script only ever asks for a fix, never for a
  test rewrite.
