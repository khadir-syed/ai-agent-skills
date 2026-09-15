# Bug fix agent report format

## Stage 1 — Diagnosis

- **Reported symptom:**
- **Investigation status:** Established / Probable / Inconclusive
- **Root cause or leading hypothesis:**
- **Confidence:** High / Medium / Low, with why
- **Evidence:** each item labelled Observed / Reported / Inferred / Unknown
- **Validation limits:**

Stop here for the fix proposal — do not include a proposed edit yet.

## Stage 2 — Fix proposal (stop for approval)

- **File(s) to change:**
- **Proposed change:** described precisely enough to review before it's made
- **Why this addresses the root cause:**
- **Expected side effects, if any:**

State plainly: "No edit has been made yet — approve to proceed."

## Stage 3 — Verification (stop for approval to close)

- **Change applied:** yes/no, with the diff shown
- **Re-run result:** the originally failing test's actual result
- **Any new or different failure introduced:** yes/no, described if yes
- **Requesting approval to close** — do not mark the bug fixed until this is
  granted.
