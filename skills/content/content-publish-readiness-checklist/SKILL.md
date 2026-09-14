---
name: content-publish-readiness-checklist
description: Run a fixed pre-publish checklist — proofreading pass, working links, SEO basics, image alt text, sourced facts and citations, brand tone match — and report pass, fail, or could-not-determine per check. Use before publishing a piece of content; do not use to make the publish decision or to fix anything the checks find.
---

# Content Publish Readiness Checklist

Run a fixed set of checks against a piece of content that's about to publish and report the result of each. Never report a check as passing when it could not actually be determined, and never make the publish decision on the user's behalf.

## Operating boundary

- Advisory only. Do not edit the content, fix anything the checks find, or publish/schedule it.
- Do not assume a check passes because "this writer usually gets it right." Base each result on what's actually supplied or checkable.
- When a check cannot be determined from what's available, report it as **could not determine**, never as a silent pass or a silent skip.

## The checklist

Run all six checks below, in order, against the content described or supplied (a draft file, a doc, or pasted text — state which one was used).

1. **Proofread for errors and placeholder text** — check the supplied text for spelling/grammar issues and leftover placeholders (`TODO`, `[insert stat here]`, `Lorem ipsum`, bracketed notes to self). Mark **Fail** if any are found; **could not determine** only if no text was actually supplied to check.
2. **Links resolve to a real destination** — every link in the content should point somewhere specific and intentional, not a placeholder (`#`, `example.com`, empty href). Flag any that don't. This does not require fetching URLs over the network; mark **could not determine** if verifying reachability is out of scope for this session.
3. **SEO basics present** — for anything meant to be found via search (blog posts, articles), is there a title and meta description/summary? If the content type doesn't apply (an internal doc, a social caption), mark **N/A**.
4. **Images have alt text** — every image reference should have a non-empty, descriptive alt attribute. Mark **Fail** if any are missing; **N/A** if the content has no images.
5. **Facts and claims are sourced** — any statistic, quote, or factual claim should trace to a source stated in the brief or notes. Mark **Fail** for an unsourced claim presented as fact; **could not determine** if source material wasn't supplied to check against.
6. **Tone matches brand/style guide** — if a brand or style guide was supplied, does the content's voice match it (formality, person, banned words/phrases)? Mark **could not determine** if no guide was supplied.

See [references/publish-checklist-format.md](references/publish-checklist-format.md) for the report table.

## Report and stop

Produce one table, one row per check, each with a status of **Pass**, **Fail**, **Could not determine**, or **N/A**, plus the evidence behind that status.

State an overall readiness summary. Do not report "ready to publish" if any check is Fail, or if any check is "Could not determine" without explicitly calling out that gap as unresolved. Never phrase the summary as a publish decision — it is input to whoever makes that decision.

Stop after the report. Do not edit the content, fix gaps found, or publish/schedule anything — even fixes that look trivial (like a broken link).

## Stopping conditions

Stop and explain the boundary when:

- the content description or file is too thin to run the checklist meaningfully;
- resolving a gap requires a decision only the content owner or brand lead can make (e.g. whether a claim needs a source or can be removed); or
- the user asks you to also decide whether to publish — that decision is theirs, not this skill's.

## Quality check

Before returning the report, confirm that:

- every row has a status and the evidence behind it;
- no check reports Pass without an actual stated or supplied basis;
- checks that could not be evaluated are labelled "Could not determine," not silently omitted; and
- the summary does not read as a publish decision, only as input to one.
