# Synthetic example: drafting a launch caption

This fictional case can be used to test or teach the Social Caption Drafter without a real social account.

## User prompt

> Use the Social Caption Drafter to draft a LinkedIn caption in caption.md for our new one-click CSV export, from this confirmed brief: aimed at existing customers who requested it, tone should be short and matter-of-fact, not hype-y, include a link to the changelog.

## Confirmed brief (source material)

```text
Feature: one-click CSV export, reports page.
Platform: LinkedIn.
Audience: existing customers who requested it (per support tickets).
Tone: short, matter-of-fact, no hype language.
Link: changelog entry (URL supplied separately).
```

## Expected draft shape

A strong response should:

1. State clearly that the brief above is the source used, and that the draft is for LinkedIn specifically.
2. Match the stated tone: no exclamation points, no "exciting news," no invented superlatives.
3. Include the changelog link as stated, without inventing a shortened/tracked version unless a tracking convention was supplied.
4. Avoid inventing a hashtag strategy, a customer quote, or an adoption statistic not present in the brief.
5. Show the drafted caption to the user and explicitly ask for approval before writing anything to `caption.md`.
6. Only write the file after the user approves, and confirm what was written and where.

## Deliberately weak conclusions

These responses should fail the learning objective:

- Writing directly to `caption.md` without showing the draft first.
- "🚀 Huge news!!!" — introduces hype language the brief explicitly ruled out.
- Adding hashtags or a customer quote not supported by the brief.
- Drafting the same caption for multiple platforms in one pass without treating each as a separate approval.
