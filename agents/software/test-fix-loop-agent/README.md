# Test-Fix Loop Agent

**Posture: Autonomous.** The only agent in this repo that's real, runnable
code rather than a Markdown instruction file — see [../../README.md](../../README.md)
for why this domain gets a code loop and Product doesn't.

Given a failing test command, it loops: run the tests, if they fail hand the
output to your AI CLI with a narrow "make the smallest fix" prompt, re-run,
repeat — up to a hard attempt cap. No human approval between attempts. It
stops (not "gives up") the moment it either passes or hits the cap.

## What it actually does

1. Runs the test command you give it.
2. If it fails, asks your AI CLI (`claude`, `codex`, whatever you point it at)
   to make the smallest possible edit, using only the failure output as
   context.
3. Re-runs the tests itself and checks the exit code — it does not trust the
   CLI's own claim of having fixed anything.
4. Repeats up to `--max-attempts` (default 5), then stops and hands the
   problem back to you with the last failure shown.

See [references/safety-notes.md](references/safety-notes.md) for exactly
what it can't do, and [examples/sample-run-transcript.md](examples/sample-run-transcript.md)
for what a run (and a cap-hit run) actually looks like.

## Requirements

- Python 3.8+ (standard library only — nothing to install)
- An AI CLI already installed and authenticated (`claude`, `codex`, `copilot`,
  or anything else that accepts `<cli> -p "<prompt>"` and exits non-zero on
  failure)

## Usage

```bash
python3 agent.py "pytest -q"
python3 agent.py "npm test" --cli codex --cli-flags "" --max-attempts 3
```

By default it also passes `--cli-flags "--permission-mode acceptEdits"` to
the CLI, so it can actually apply an edit without a human present to answer
an approval prompt — see [references/safety-notes.md](references/safety-notes.md)
for exactly what that does and doesn't bypass. If you point `--cli` at
something other than Claude Code, pass that CLI's equivalent flag (or `""`
to require interactive approval yourself).

## Self-check

```bash
python3 test_agent.py
```

Plain-assert checks against the loop logic itself (first-try pass, cap-hit,
CLI failure, fix-on-second-attempt) — no real CLI or test suite involved.
