---
name: changelog-entry-drafter
description: Draft and append a dated CHANGELOG.md entry from recent commits or a diff. Use when the user asks to update the changelog, log recent changes, or prepare release notes for one version; do not use for editing unrelated files or for a general commit-message writer.
---

# Changelog Entry Drafter

Draft one dated `CHANGELOG.md` entry from recent commits or a diff, show it before writing, and write only with the user's approval.

## Operating boundary

- Touch only `CHANGELOG.md`. Do not edit source files, other docs, or configuration.
- Base every drafted line on an actual commit message, diff hunk, or user-supplied description. Do not invent changes that are not evidenced.
- Redact anything that looks like a secret, token, or credential found in commit messages or diffs; never copy it into the changelog.
- Never treat access to write a file as permission to write it. Always get approval first (see below).

## Workflow

### 1. Gather evidence

Identify the range to summarise: since the last tag, since the last changelog entry, a supplied commit range, or a supplied diff. State which one you used.

Read the commit log and/or diff for that range. Label each drafted line as based on an **observed** commit/diff, or **reported** if it comes from the user's own description rather than something you inspected.

### 2. Draft the entry

Group changes using Keep a Changelog–style categories (Added, Changed, Fixed, Removed, Security) — see [references/changelog-entry-format.md](references/changelog-entry-format.md). Omit categories with nothing to report. Keep each line short and user-facing; skip purely internal changes unless the user asks to include them.

Check whether an entry for today's date already exists in `CHANGELOG.md`:

- If yes, ask whether to append to it or replace it. Do not silently duplicate.
- If no, prepare a new dated heading.

### 3. Show the draft and get approval

Show the complete proposed entry to the user before writing anything. Do not write first and confirm after.

**Approval model:**

- Default: one-time approval. Ask before this specific write; a "yes" or "go ahead" authorises this write only.
- Session-scoped approval: only if the user's own request explicitly grants standing permission for the session (for example, "update the changelog after each change, don't ask me again this session"). When this applies, say so out loud before proceeding — e.g. "Proceeding without per-entry confirmation, as requested for this session" — and continue asking again in any later session.
- Never infer standing approval from a single approval of one entry. Never infer it from tool-level file-write access being available.

### 4. Write and confirm

Append (or replace, per step 2) the approved entry at the correct position in `CHANGELOG.md`. Confirm what was written and where.

## Stopping conditions

Stop and ask rather than guessing when:

- the commit range or diff to summarise is ambiguous;
- the evidence does not clearly indicate user-facing impact for a change;
- a possible secret or credential is detected in the source material; report this to the user instead of drafting around it silently;
- `CHANGELOG.md` does not exist or does not follow a recognisable format — ask whether to create one or use a different location.

## Quality check

Before writing, confirm that:

- every line in the draft traces to an observed commit/diff or a reported user description, labelled accordingly;
- the entry was shown to the user before any write occurred;
- the approval obtained matches what is being written (one-time vs. session-scoped, and for this write specifically);
- no secret, token, or credential appears in the drafted text.
