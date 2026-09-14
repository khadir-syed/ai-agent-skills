# Changelog entry format

Use a [Keep a Changelog](https://keepachangelog.com/)–style dated entry.

```markdown
## [YYYY-MM-DD]

### Added
- User-facing addition, in plain language.

### Changed
- User-facing behaviour change.

### Fixed
- User-facing bug fix.

### Removed
- User-facing removal.

### Security
- Security-relevant fix or change, described without exposing exploit detail.
```

Rules:

- Omit any category with nothing to report for this entry.
- One line per change, written for someone who did not read the diff.
- Do not include purely internal refactors, formatting, or test-only changes unless the user asks for them.
- Do not include secrets, tokens, credentials, internal hostnames, or other sensitive values, even if they appear in the source commits.
- If an entry for the same date already exists, append new bullets under the matching category rather than creating a second dated heading for the same day, unless the user asks to keep them separate.
