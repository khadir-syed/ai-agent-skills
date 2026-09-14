# Checklist report format

## Change scope

- **Range evaluated:**
- **Source:** staged diff, branch diff against base, or user-specified range

## Checklist

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | Tests present or updated | Pass / Fail / Could not determine | |
| 2 | Docs touched for user-facing change | Pass / Fail / Could not determine | |
| 3 | No obvious leftover debug code | Pass / Fail | |
| 4 | Commit messages follow a recognisable convention | Pass / Fail / N/A | |
| 5 | No secrets or credentials in the diff | Pass / Fail | |
| 6 | No sensitive files newly tracked | Pass / Fail | |

Status definitions:

- **Pass:** the check was evaluated and the repository satisfies it.
- **Fail:** the check was evaluated and the repository does not satisfy it.
- **Could not determine:** the check could not be meaningfully evaluated (e.g. no detectable test or commit convention). Never substitute for Pass.
- **N/A:** the check does not apply to this repository or change (e.g. no commit-message convention exists to check against).

## Overall readiness

State one of:

- **Ready:** all checks Pass or N/A.
- **Not ready:** at least one check Fail.
- **Ready with unresolved gaps:** no Fail, but one or more checks are Could not determine — name each gap explicitly rather than rounding up to "ready."

## Not performed

List anything this checklist does not cover and was not asked to cover (e.g. performance testing, accessibility review), so the summary isn't mistaken for a full review.
