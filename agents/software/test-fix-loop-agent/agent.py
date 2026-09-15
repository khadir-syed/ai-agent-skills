#!/usr/bin/env python3
"""Test-Fix Loop Agent — a small, autonomous tool-loop example.

Given a failing test command, this script repeatedly asks your existing
AI CLI (Claude Code, Codex, Copilot CLI — whichever you already have
installed) to make the smallest possible fix, then re-runs the tests
itself and checks the result. No API key, no SDK: it shells out to a CLI
you already use, the same way you would by hand.

Stops on:
  - tests passing (success)
  - the attempt cap being reached without success (hands back to you)
  - the CLI command itself failing to run (misconfiguration, not a code
    problem — stops rather than guessing)

Intentionally narrow: it only ever runs your test command and your AI
CLI. It does not touch dependencies, network access, or git history.
Read references/safety-notes.md before pointing it at a real repo.
"""
import argparse
import re
import shlex
import subprocess
import sys

DEFAULT_MAX_ATTEMPTS = 5
CLI_TIMEOUT_SECONDS = 300  # ponytail: fixed cap, make configurable if a slower CLI needs it

FIX_PROMPT = (
    "The following command is failing: {test_cmd}\n\n"
    "Here is its output:\n{output}\n\n"
    "Make the smallest possible edit to fix this one failure. "
    "Do not refactor unrelated code, do not touch tests unless the test "
    "itself is provably wrong, and do not run the test command yourself — "
    "just make the edit and stop."
)

# Test output can contain secrets accidentally printed by a failing assertion
# (an API key in a stack trace, a DB URL in a config dump). This is included
# verbatim in a prompt sent to an external AI CLI, so redact common shapes
# first — same discipline the Markdown bug-fix-agent requires of itself.
SECRET_PATTERN = re.compile(
    r"(?i)\b((?:api[_-]?key|secret|token|password|passwd|access[_-]?key)"
    r"\s*[:=]\s*)(\S+)"
)


def redact_secrets(text: str) -> str:
    return SECRET_PATTERN.sub(lambda m: m.group(1) + "[REDACTED]", text)


def run_tests(test_cmd: str) -> subprocess.CompletedProcess:
    return subprocess.run(shlex.split(test_cmd), capture_output=True, text=True)


def run_cli_fix(cli: str, cli_flags: str, test_cmd: str, output: str) -> subprocess.CompletedProcess:
    prompt = FIX_PROMPT.format(test_cmd=test_cmd, output=redact_secrets(output)[-4000:])
    cmd = [cli, "-p", prompt] + (shlex.split(cli_flags) if cli_flags else [])
    return subprocess.run(cmd, timeout=CLI_TIMEOUT_SECONDS)


def _print_flushed(msg: str) -> None:
    print(msg, flush=True)


def loop(test_cmd: str, cli: str, cli_flags: str, max_attempts: int, out=_print_flushed) -> int:
    for attempt in range(1, max_attempts + 1):
        out(f"\n=== Attempt {attempt}/{max_attempts}: running tests ===")
        result = run_tests(test_cmd)
        if result.returncode == 0:
            out(f"Tests passed after {attempt - 1} fix attempt(s).")
            return 0

        combined_output = result.stdout + result.stderr
        out("Tests failed. Output:")
        out(redact_secrets(combined_output)[-2000:])

        if attempt == max_attempts:
            break

        out(f"\n=== Attempt {attempt}: asking '{cli}' for the smallest fix ===")
        try:
            cli_result = run_cli_fix(cli, cli_flags, test_cmd, combined_output)
        except subprocess.TimeoutExpired:
            out(f"'{cli}' did not finish within {CLI_TIMEOUT_SECONDS}s; stopping rather than guessing.")
            return 2
        if cli_result.returncode != 0:
            out(f"'{cli}' exited non-zero ({cli_result.returncode}); stopping rather than guessing.")
            return 2

    out(
        f"\nStopping: {max_attempts} attempt(s) made, tests still failing. "
        "Handing back to you — see the last test output above."
    )
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Autonomous test-fix loop agent.")
    parser.add_argument("test_cmd", help='Test command to run, e.g. "pytest -q"')
    parser.add_argument(
        "--cli", default="claude", help='AI CLI command to invoke per attempt (default: "claude")'
    )
    parser.add_argument(
        "--cli-flags",
        default="--permission-mode acceptEdits",
        help=(
            "Extra flags passed to the CLI so it can actually apply an edit "
            "non-interactively, instead of just describing one and exiting "
            "(default matches Claude Code; pass the equivalent flag for your "
            "CLI, or \"\" to disable)"
        ),
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=DEFAULT_MAX_ATTEMPTS,
        help=f"Hard cap on fix attempts (default: {DEFAULT_MAX_ATTEMPTS})",
    )
    args = parser.parse_args()
    if args.max_attempts < 1:
        parser.error("--max-attempts must be at least 1")
    return loop(args.test_cmd, args.cli, args.cli_flags, args.max_attempts)


if __name__ == "__main__":
    sys.exit(main())
