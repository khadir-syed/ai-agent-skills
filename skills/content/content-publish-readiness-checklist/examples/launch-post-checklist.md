# Synthetic example: pre-publish check on a launch post

This fictional case can be used to test or teach the Content Publish Readiness Checklist without a real CMS.

## User prompt

> Use the Content Publish Readiness Checklist on draft-blog-post.md before we publish it.

## Supplied draft (excerpt)

```text
Title: (none set)
Body: "...check out our new export feature [insert stat here] and
see the difference for yourself! Read more at #."
Image: <img src="export-screenshot.png"> (no alt attribute)
Brand guide: not supplied.
```

## Expected checklist shape

A strong response should:

1. Mark **Proofread for errors and placeholder text** as **Fail** — `[insert stat here]` is a leftover placeholder.
2. Mark **Links resolve to a real destination** as **Fail** — the link target is `#`, a placeholder.
3. Mark **SEO basics present** as **Fail** — no title is set.
4. Mark **Images have alt text** as **Fail** — the image tag has no alt attribute.
5. Mark **Facts and claims are sourced** as **Could not determine** — no specific claim exists yet since the stat is a placeholder, but flag it as something to source once filled in.
6. Mark **Tone matches brand/style guide** as **Could not determine** — no brand guide was supplied to check against.
7. Summarize clearly that this is not ready to publish, without phrasing it as "don't publish this" (a decision) — instead: "several checks fail or can't be confirmed; here's what needs attention before a publish decision is made."

## Deliberately weak conclusions

These responses should fail the learning objective:

- "Looks good, ready to publish!" — ignores multiple clear failures.
- Editing the draft to fix the placeholder text or add alt text, instead of just reporting it.
- Marking "Facts and claims are sourced" as **Pass** because no claim was checked, rather than **Could not determine**.
- Telling the user "don't publish this" as if it were the skill's decision to make.
