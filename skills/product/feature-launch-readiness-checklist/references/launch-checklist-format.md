# Feature launch readiness report format

## Feature

- **Feature described:** 
- **Source:** ticket, PRD, or user's own description

## Checklist

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | Rollback plan exists | Pass / Fail / Could not determine | |
| 2 | Rollout control configured | Pass / Fail / Could not determine | |
| 3 | Success metric defined | Pass / Fail | |
| 4 | Docs or help content updated | Pass / Fail / Could not determine / N/A | |
| 5 | Support/customer-facing team briefed | Pass / Fail / Could not determine | |
| 6 | No known blocking issues open | Pass / Fail | |

Status definitions:

- **Pass:** the check was evaluated and satisfied.
- **Fail:** the check was evaluated and not satisfied.
- **Could not determine:** not enough information was supplied to evaluate this check. Never substitute for Pass.
- **N/A:** genuinely does not apply (e.g. a backend-only change with no user-visible behaviour, for the docs check).

## Overall readiness (input to a decision, not the decision itself)

State one of:

- **No blockers found:** all checks Pass or N/A.
- **Blockers found:** at least one check Fail.
- **Blockers unclear:** no Fail, but one or more checks are Could not determine — name each gap explicitly.

## Not performed

List anything this checklist does not cover (e.g. legal/compliance review, security review, performance testing) so the summary isn't mistaken for a full launch review.
