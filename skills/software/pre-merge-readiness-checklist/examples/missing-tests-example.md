# Synthetic example: missing tests on a changed file

This fictional case can be used to test or teach the Pre-Merge Readiness Checklist without a real repository.

## User prompt

> Use the Pre-Merge Readiness Checklist on my current branch diff against main.

## Evidence packet

Treat the following as the observed diff summary for `feature/export-pdf..main`.

```text
Changed files:
  src/reports/export.js       (+42, -3)
  src/reports/formatters.js   (+11, -0)

Repo conventions observed:
  - Existing tests live under src/**/__tests__/*.test.js
  - No __tests__ changes in this diff
  - README.md documents the "Export" menu; not touched in this diff
  - Commit history uses Conventional Commits (feat:, fix:, chore:)
  - This diff's commits: "wip", "more changes", "fix stuff"
  - No console.log/debugger/pdb found in the diff
  - No secret-like patterns found in the diff
  - No new .env/.pem/credentials.json files added
```

## Expected report shape

A strong response should mark:

1. **Tests present or updated — Fail.** Repo has a clear `__tests__` convention; this diff changes exported logic but adds no test changes.
2. **Docs touched for user-facing change — Fail.** `export.js` changes look user-facing (export behaviour) and README documents the Export feature but wasn't touched. If genuinely ambiguous whether it's user-facing, "Could not determine" is also acceptable — but here it should lean Fail given the evidence.
3. **No obvious leftover debug code — Pass.**
4. **Commit messages follow a recognisable convention — Fail.** Repo has an established Conventional Commits pattern; these commit messages ("wip", "more changes", "fix stuff") don't follow it.
5. **No secrets or credentials in the diff — Pass.**
6. **No sensitive files newly tracked — Pass.**

**Overall readiness: Not ready** — tests missing and commit messages don't follow the repo's own convention.

## Deliberately weak responses

These should fail the learning objective:

- Marking "Tests present or updated" as Pass because the skill assumes tests exist somewhere without checking the diff.
- Fixing the missing tests or rewriting commit messages instead of just reporting the gap.
- Reporting "Ready to merge" while a check is Fail.
- Guessing a test framework/convention not actually evidenced in the repo, instead of checking what's observed.
