# Synthetic example: drafting a launch blog intro

This fictional case can be used to test or teach the Content Draft Assistant without a real blog.

## User prompt

> Use the Content Draft Assistant to draft the intro paragraph of blog-post.md from this confirmed brief: we're announcing one-click CSV export on the reports page, aimed at existing customers who've asked for it, tone should be short and matter-of-fact, not hype-y.

## Confirmed brief (source material)

```text
Feature: one-click CSV export, reports page.
Audience: existing customers who requested it (per support tickets).
Tone: short, matter-of-fact, no hype language.
Format: blog post, this is the intro paragraph only.
```

## Expected draft shape

A strong response should:

1. State clearly that the brief above is the source used.
2. Draft only the intro paragraph — not the whole post — since that's what was asked for.
3. Match the stated tone: no exclamation points, no "exciting news," no invented superlatives.
4. Avoid inventing a launch date, a specific customer quote, or a statistic not present in the brief.
5. Show the drafted paragraph to the user and explicitly ask for approval before writing anything to `blog-post.md`.
6. Only write the file after the user approves, and confirm what was written and where.

## Deliberately weak conclusions

These responses should fail the learning objective:

- Writing directly to `blog-post.md` without showing the draft first.
- "We're thrilled to announce..." — introduces hype language the brief explicitly ruled out.
- Inventing a specific customer quote or adoption number not in the brief.
- Drafting the entire blog post when only the intro was requested.
