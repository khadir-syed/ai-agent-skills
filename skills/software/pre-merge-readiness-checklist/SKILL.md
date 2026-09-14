---
name: pre-merge-readiness-checklist
description: Run a fixed pre-merge readiness checklist — tests, docs, leftover debug code, commit convention, secrets, sensitive files — and report pass, fail, or could-not-determine per check. Use before merging a change to catch gaps; do not use to implement fixes or as a general code review.
---

# Pre-Merge Readiness Checklist

Run a fixed set of non-destructive checks against a pending change and report the result of each. Never report a check as passing when it could not actually be determined.

## Operating boundary

- Read-only. Do not edit files, run tests that mutate state, install dependencies, or fix anything found.
- Do not guess a stack-specific convention you cannot detect from the repository itself. When a check cannot be determined, report it as **could not determine**, never as a silent pass or a silent skip.
- Redact secret-like values found during the secrets check; report that a match was found and where, not the value itself.

## The checklist

Run all six checks below, in order, against the pending change (staged diff, branch diff against its base, or a range the user specifies — state which one was used).

1. **Tests present or updated** — for each changed source file, is there a corresponding changed or added test? Base this on file naming/location conventions actually observed in the repo (e.g. a `tests/` or `__tests__/` directory, `*_test.*` / `*.test.*` / `*.spec.*` naming). If no test convention is detectable in this repo, mark **could not determine**, not fail.
2. **Docs touched for user-facing change** — if the diff changes user-facing behaviour (CLI flags, API surface, README-documented features), is a doc file also touched? If it's unclear whether the change is user-facing, mark **could not determine** rather than assuming either way.
3. **No obvious leftover debug code** — scan the diff for things like stray `console.log`/`print` debugging statements, `pdb.set_trace()`, `debugger;`, or `TODO: remove before merge` markers introduced by this change.
4. **Commit messages follow a recognisable convention** — only evaluate this if the repo's existing history shows a discernible convention (e.g. Conventional Commits). If no convention is evident from history, mark **N/A**, not fail.
5. **No secrets or credentials in the diff** — scan added/changed lines for patterns consistent with API keys, tokens, passwords, or private-key material. Flag any match for human review; do not attempt to judge whether a matched value is a real secret or a placeholder — always flag it.
6. **No sensitive files newly tracked** — check whether this diff adds a file matching common sensitive patterns (`.env`, `credentials.json`, `*.pem`, `*.key`, and similar) that was not previously tracked.

See [references/checklist-report-format.md](references/checklist-report-format.md) for the report table.

## Report and stop

Produce one table, one row per check, each with a status of **Pass**, **Fail**, **Could not determine**, or **N/A**, plus the evidence behind that status.

State an overall readiness summary. Do not report overall readiness as "ready to merge" if any check is Fail, or if any check is "Could not determine" without explicitly calling out that gap as unresolved.

Stop after the report. Do not fix anything found, and do not proceed to remediation unless the user separately asks and authorises it.

## Stopping conditions

Stop and explain the boundary when:

- the diff or change range is ambiguous;
- the repository's testing or commit conventions cannot be established well enough to run checks 1 or 4 meaningfully;
- a likely secret is found — report it and recommend the user rotate/remove it themselves; do not attempt to remove it.

## Quality check

Before returning the report, confirm that:

- every row has a status and the evidence behind it;
- no check reports Pass without actual supporting evidence from this repository;
- checks that could not be evaluated are labelled "Could not determine," not silently omitted;
- the overall summary does not overstate readiness given the individual results.
