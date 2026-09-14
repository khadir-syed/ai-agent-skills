---
name: prd-draft-assistant
description: Draft one section of a product requirements document (PRD) from notes, a ticket, or a confirmed brief, and write it to a file only with explicit approval. Use when requirements are already reasonably clear and need to be written up; do not use on a vague or conflicting request — use the Requirements Gap Investigator first.
---

# PRD Draft Assistant

Draft one PRD (or a single section of one) from material the user supplies, show it before writing, and write only with the user's approval.

## Operating boundary

- Touch only the single PRD file named or clearly implied by the user (e.g. `PRD.md`, a named doc, or a specific section within one). Do not edit unrelated files.
- Base every drafted statement on the supplied notes, ticket, or brief. Do not invent requirements, metrics, or scope not present in the source material.
- If the source material is vague or contains conflicting signals, say so and recommend the Requirements Gap Investigator instead of drafting around the ambiguity.
- Never treat access to write a file as permission to write it. Always get approval first (see below).

## Workflow

### 1. Gather the source material

Identify what you're drafting from: a ticket, a set of notes, a confirmed brief, or a prior gap-investigation report. State which one you used.

If the source material leaves a needed section un-fillable (e.g. no success metric was ever stated), say so explicitly in the draft rather than inventing a plausible-sounding one.

### 2. Draft the section(s)

Use standard PRD sections as needed — see [references/prd-section-format.md](references/prd-section-format.md) — such as Problem Statement, Goals, Non-Goals, User Stories, Success Metrics, and Open Questions. Only draft sections the source material actually supports; leave others explicitly marked as needing input rather than filling them with plausible-sounding filler.

Keep language concrete and checkable — prefer "reduces average export time from 40s to under 5s" over "makes exports faster," when the source material supports a specific number; otherwise state it as an open question rather than inventing a number.

### 3. Show the draft and get approval

Show the complete drafted section(s) to the user before writing anything. Do not write first and confirm after.

**Approval model:**

- Default: one-time approval. Ask before this specific write; a "yes" or "go ahead" authorises this write only.
- Session-scoped approval: only if the user's own request explicitly grants standing permission for the session (for example, "draft each section as we go and save them without asking each time"). When this applies, say so out loud before proceeding, and continue asking again in any later session.
- Never infer standing approval from a single approval of one section.

### 4. Write and confirm

Write the approved section(s) to the named file, in the right place if the file already has other sections. Confirm what was written and where.

## Stopping conditions

Stop and ask rather than guessing when:

- the source material is too vague or conflicting to draft from confidently — recommend the Requirements Gap Investigator instead;
- a section would require inventing a metric, scope boundary, or user story not present in the source; state it as an open question instead;
- the target file or section is ambiguous; or
- the request also asks for a product decision (e.g. prioritisation, go/no-go) — that is out of scope for this skill.

## Quality check

Before writing, confirm that:

- every drafted statement traces back to the supplied source material;
- sections that can't be responsibly filled are marked as open questions, not invented;
- the draft was shown to the user before any write occurred; and
- the approval obtained matches what is being written (one-time vs. session-scoped, and for this write specifically).
