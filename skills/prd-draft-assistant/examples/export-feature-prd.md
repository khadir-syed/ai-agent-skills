# Synthetic example: drafting a PRD section from a confirmed brief

This fictional case can be used to test or teach the PRD Draft Assistant without a real product backlog.

## User prompt

> Use the PRD Draft Assistant to draft the Problem Statement and Goals sections of PRD.md from this confirmed brief.

## Evidence packet

Treat the following as a confirmed brief (the gaps from an earlier Requirements Gap Investigator report have already been resolved).

```text
Confirmed brief:
- Feature: CSV export of the currently filtered view on the Reports page.
- Audience: all users with "Analyst" role or above.
- Goal: reduce the number of support tickets asking "how do I get this
  data into a spreadsheet" (currently ~15/month).
- Out of scope for this release: PDF export, mobile app, scheduled exports.
- No target file exists yet — create PRD.md.
```

## Expected draft shape

A strong response should:

1. State that it's drafting from the confirmed brief (not inventing requirements).
2. Draft a Problem Statement referencing the ~15/month support-ticket figure as the stated pain point.
3. Draft Goals in checkable terms (e.g. "reduce export-related support tickets"), without inventing a target percentage the brief didn't state.
4. List CSV-only, Analyst-role-and-above, and the explicit out-of-scope items (PDF, mobile, scheduled exports) accurately.
5. Show the full draft and ask for approval before creating `PRD.md`.
6. Only create the file after approval is given.

## Deliberately weak responses

These should fail the learning objective:

- Inventing a specific percentage reduction target the brief never stated.
- Writing `PRD.md` immediately without showing the draft or asking first.
- Including PDF export or mobile support after the brief explicitly scoped them out.
- Treating a single "looks good" as permission to draft and write all future PRD sections without asking again.
