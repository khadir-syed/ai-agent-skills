# Synthetic example: launching the CSV export feature

This fictional case can be used to test or teach the Feature Launch Readiness Checklist without a real product backlog. It continues the CSV export example used in the other two Product skills.

## User prompt

> Use the Feature Launch Readiness Checklist on the CSV export feature we're shipping this week.

## Evidence packet

```text
Feature: CSV export of the currently filtered Reports view, for
Analyst-role users and above.

Known so far:
- Behind a feature flag, currently enabled for 100% of eligible users
  (no staged rollout planned).
- No rollback plan beyond "turn the feature flag off."
- Success metric: PRD states the goal is reducing export-related support
  tickets (~15/month baseline) but no target number or dashboard exists yet.
- No documentation or help-center article has been written.
- Support team has not been given any advance notice.
- One open bug: export fails silently for reports with >10,000 rows;
  not yet fixed, not yet explicitly accepted as a known limitation.
```

## Expected report shape

A strong response should mark:

1. **Rollback plan exists — Pass.** Turning off the feature flag is a stated rollback mechanism, even if minimal.
2. **Rollout control configured — Fail.** Flag exists but is already at 100%; no staged rollout is planned, which is what this check is actually asking about.
3. **Success metric defined — Fail.** A baseline is known, but no target or dashboard was defined — "reduce tickets" without a number or tracking mechanism isn't a checkable metric.
4. **Docs or help content updated — Fail.** Explicitly stated as not done, and this is a user-visible change.
5. **Support/customer-facing team briefed — Fail.** Explicitly stated as not done.
6. **No known blocking issues open — Fail.** The silent-failure bug on large exports is open and not accepted as a known limitation.

**Overall: Blockers found** — 5 of 6 checks failed; this is explicitly reported as input to the launch decision, not as a decision to delay or proceed.

## Deliberately weak responses

These should fail the learning objective:

- Marking "Rollout control configured" as Pass because a feature flag exists, without checking whether it's actually being used for staged rollout.
- Saying "Ready to launch" or "Don't launch" — the skill reports facts, it doesn't make the call.
- Fixing the open bug or writing the missing documentation instead of just reporting the gap.
- Treating the support-ticket baseline as if it were itself a defined success metric.
