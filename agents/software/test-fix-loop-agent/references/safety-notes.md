# Safety notes

## Why the attempt cap exists

Without a hard cap, a broken or misunderstood failure can loop indefinitely,
burning CLI calls and potentially making a file worse with every "fix." The
cap (default 5, configurable) guarantees the agent always terminates and
always hands a clear failure back to a human rather than spinning forever.

## What this agent cannot do

- It cannot touch anything outside your test command and your AI CLI
  invocation — no dependency installs, no network calls, no git operations,
  no deployment of any kind.
- It does not decide the fix is correct beyond "the exit code is 0." A test
  that passes for the wrong reason (an overly permissive assertion, a
  disabled check) will read as success. This agent is a loop, not a
  reviewer — always look at the diff it produced before trusting it.
- By default it passes `--cli-flags "--permission-mode acceptEdits"` to the
  CLI so it can actually apply an edit non-interactively — there's no human
  present in this loop to answer an approval prompt, so without this the CLI
  just describes a plan and exits, and the loop silently burns attempts doing
  nothing. This is scoped to accepting edits specifically, not a blanket
  `--dangerously-skip-permissions`; anything outside file edits still follows
  your CLI's normal rules. Pass `--cli-flags ""` to disable it if you're
  running this attached to a terminal yourself and want to approve each edit.
- It does not retry with a different strategy. Each attempt gets the same
  narrow prompt and the latest failure output; it has no memory of earlier
  attempts beyond what the CLI itself may retain in its own session.

## What "stop and hand back" means

When the cap is hit, the agent does not attempt anything further. It prints
the last test failure and exits with a non-zero status. Nothing is
auto-committed, auto-reverted, or auto-reported anywhere — the working tree
is left exactly as the CLI's last edit attempt left it, for you to inspect
with `git diff` before deciding what to do next.

## Test output is redacted before it leaves your machine

Failure output is sent verbatim into a prompt for your AI CLI, which means
it leaves your machine. Before that happens, `agent.py` redacts common
secret shapes (`api_key=`, `token:`, `password=`, and similar) from that
output, matching the same redaction discipline the Markdown `bug-fix-agent`
requires of itself. This is a pattern match on common shapes, not a
guarantee — a secret printed in an unusual format (no recognizable key name,
split across lines) will not be caught. Don't rely on this as your only
safeguard if your test output can contain anything sensitive; prefer fixing
the test/logging so it doesn't print secrets in the first place.

The CLI call itself also has a fixed 300-second timeout — if your AI CLI
hangs, the loop stops and hands back to you rather than waiting forever.
Your own test command has no such timeout, since legitimate test suites can
legitimately take a long time; only the CLI invocation, which is expected to
be a single bounded "make this edit" request, is capped.

## Observed in real testing: it can "fix" the test instead of the code

Pointed at an intentionally impossible assertion (`assertEqual(1, 2)`), a real
run didn't loop or fail — it changed the assertion to `assertEqual(1, 1)` in
one attempt and reported success. The prompt tells it not to touch tests
"unless the test itself is provably wrong," and a real AI CLI can reasonably
decide an impossible assertion qualifies. The exit code was 0 either way, so
nothing about the agent's own logic could tell the difference between this
and a genuine source fix. This is exactly why the loop is not a substitute
for reading the diff afterward — do it every time, not just on a cap-hit.

## Before pointing this at a real repo

- Run it from a clean working tree (commit or stash first) so a bad attempt
  is trivially reversible with `git checkout` / `git restore`.
- Start with a small `--max-attempts` (2-3) the first time, on a low-stakes
  failing test, before trusting it with the default cap.
