"""Plain-assert self-check for the loop logic in agent.py — no test framework.
Run: python3 test_agent.py
"""
from unittest.mock import patch
import subprocess

from agent import loop, redact_secrets

PASS = subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")
FAIL = subprocess.CompletedProcess(args=[], returncode=1, stdout="assert 1 == 2", stderr="")
CLI_OK = subprocess.CompletedProcess(args=[], returncode=0)
CLI_BROKEN = subprocess.CompletedProcess(args=[], returncode=127)


def test_stops_on_first_pass():
    with patch("agent.run_tests", return_value=PASS) as tests, patch("agent.run_cli_fix") as fix:
        assert loop("pytest -q", "claude", "", 5, out=lambda *_: None) == 0
        assert tests.call_count == 1
        fix.assert_not_called()


def test_stops_at_attempt_cap_when_never_fixed():
    with patch("agent.run_tests", return_value=FAIL) as tests, patch(
        "agent.run_cli_fix", return_value=CLI_OK
    ) as fix:
        assert loop("pytest -q", "claude", "", 3, out=lambda *_: None) == 1
        assert tests.call_count == 3
        assert fix.call_count == 2  # no fix attempt after the final test run


def test_stops_if_cli_itself_fails():
    with patch("agent.run_tests", return_value=FAIL), patch(
        "agent.run_cli_fix", return_value=CLI_BROKEN
    ) as fix:
        assert loop("pytest -q", "missing-cli", "", 5, out=lambda *_: None) == 2
        assert fix.call_count == 1


def test_redact_secrets_masks_common_shapes():
    text = "Connecting with api_key=sk-abc123 and PASSWORD: hunter2hunter2"
    redacted = redact_secrets(text)
    assert "sk-abc123" not in redacted
    assert "hunter2hunter2" not in redacted
    assert "[REDACTED]" in redacted
    assert redact_secrets("assert 1 == 2") == "assert 1 == 2"


def test_fix_on_second_attempt_then_passes():
    responses = iter([FAIL, PASS])
    with patch("agent.run_tests", side_effect=lambda _: next(responses)), patch(
        "agent.run_cli_fix", return_value=CLI_OK
    ):
        assert loop("pytest -q", "claude", "", 5, out=lambda *_: None) == 0


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"ok  {name}")
    print("All checks passed.")
