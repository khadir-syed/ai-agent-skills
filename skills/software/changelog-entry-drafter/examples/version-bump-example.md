# Synthetic example: version bump changelog entry

This fictional case can be used to test or teach the Changelog Entry Drafter without a real repository.

## User prompt

> Use the Changelog Entry Drafter. We're about to tag v1.4.0 — draft a changelog entry from the commits since v1.3.0.

## Evidence packet

Treat the following as the observed commit log for the range `v1.3.0..HEAD`.

```text
a1b2c3d fix: correct timezone offset in report export
e4f5g6h feat: add CSV export option to reports page
h7i8j9k chore: bump lint config
k1l2m3n fix: handle empty project list without crashing
```

`CHANGELOG.md` currently ends with an entry dated `2026-08-02` and no entry exists yet for today.

## Expected draft shape

A strong response should:

1. State the commit range used (`v1.3.0..HEAD`) and that the entry is based on observed commit messages.
2. Group into categories: `Added` (CSV export option), `Fixed` (timezone offset in export, crash on empty project list).
3. Omit the lint-config chore — internal-only, no user-facing impact.
4. Show the full drafted entry to the user and explicitly ask for approval before writing.
5. Only after approval, append the entry under a new `## [2026-09-14]` heading (today's date) — not overwrite the `2026-08-02` entry.

## Example drafted entry

```markdown
## [2026-09-14]

### Added
- CSV export option on the reports page.

### Fixed
- Corrected timezone offset in report export.
- Report page no longer crashes when the project list is empty.
```

## Deliberately weak responses

These should fail the learning objective:

- Writing the entry directly to `CHANGELOG.md` without showing it first or asking approval.
- Including the "bump lint config" commit as a user-facing change.
- Treating a single "looks good" as permission to draft and write future entries without asking again next session.
