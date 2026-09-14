---
name: feature-launch-readiness-checklist
description: Run a fixed feature-launch readiness checklist — rollback plan, rollout control, success metrics, docs, support readiness, known blockers — and report pass, fail, or could-not-determine per check. Use before shipping a feature to catch gaps; do not use to make the go/no-go decision or to implement anything the checks find missing.
---

# Feature Launch Readiness Checklist

Run a fixed set of checks against a feature that's about to ship and report the result of each. Never report a check as passing when it could not actually be determined, and never make the launch decision on the user's behalf.

## Operating boundary

- Advisory only. Do not decide whether the feature ships, edit any files, update tickets, or notify stakeholders.
- Do not assume a check passes because "it usually does" for this team. Base each result on what's actually supplied or checkable.
- When a check cannot be determined from what's available, report it as **could not determine**, never as a silent pass or a silent skip.

## The checklist

Run all six checks below, in order, against the feature described (from a ticket, PRD, or the user's own description — state which one was used).

1. **Rollback plan exists** — is there a documented way to disable or revert this feature quickly if something goes wrong (a feature flag, a config toggle, a deploy revert plan)? If nothing is stated, mark **could not determine**, not fail — unless the user confirms none exists, in which case mark **Fail**.
2. **Rollout control configured** — will this ship to everyone at once, or is there a staged/gradual rollout mechanism (feature flag percentage, beta cohort, region-by-region)? Ambiguous inputs are **could not determine**.
3. **Success metric defined** — is there a stated, checkable way to know if this launch worked (a number, a dashboard, an event to track)? If the source material only says something vague like "see how it goes," mark **Fail** — vague is not a defined metric.
4. **Docs or help content updated** — if this changes user-visible behaviour, is there updated documentation, a help-center article, or release note prepared? If it's unclear whether the feature is user-visible, mark **could not determine**.
5. **Support/customer-facing team briefed** — has the team who will field questions about this been given anything (a summary, an FAQ, advance notice)? Mark **could not determine** if this isn't mentioned either way.
6. **No known blocking issues open** — are there any known bugs, edge cases, or stated concerns against this feature that haven't been resolved or explicitly accepted? List them if so.

See [references/launch-checklist-format.md](references/launch-checklist-format.md) for the report table.

## Report and stop

Produce one table, one row per check, each with a status of **Pass**, **Fail**, **Could not determine**, or **N/A**, plus the evidence behind that status.

State an overall readiness summary. Do not report "ready to launch" if any check is Fail, or if any check is "Could not determine" without explicitly calling out that gap as unresolved. Never phrase the summary as a go/no-go decision — it is input to whoever makes that decision.

Stop after the report. Do not update tickets, notify anyone, or start closing gaps found — even ones that look easy to fix.

## Stopping conditions

Stop and explain the boundary when:

- the feature description is too thin to run the checklist meaningfully;
- resolving a gap requires a decision only the feature owner or a named stakeholder can make; or
- the user asks you to also decide whether to launch — that decision is theirs, not this skill's.

## Quality check

Before returning the report, confirm that:

- every row has a status and the evidence behind it;
- no check reports Pass without an actual stated or supplied basis;
- checks that could not be evaluated are labelled "Could not determine," not silently omitted; and
- the summary does not read as a launch decision, only as input to one.
