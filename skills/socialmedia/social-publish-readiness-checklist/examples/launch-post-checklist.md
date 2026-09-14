# Synthetic example: pre-publish check on a launch post

This fictional case can be used to test or teach the Social Publish Readiness Checklist without a real social account.

## User prompt

> Use the Social Publish Readiness Checklist on draft-caption.md before we post it to Twitter/X.

## Supplied draft (excerpt)

```text
Platform: Twitter/X (280-character limit not confirmed by user).
Caption: "Check out our new export feature! # export #newfeature
#trending #followus #like #share See more at bit.ly/xyz"
Image: <img src="export-screenshot.png"> (no alt attribute)
Posting calendar: not supplied.
```

## Expected checklist shape

A strong response should:

1. Mark **Within the platform's character limit** as **Could not determine** — the caption's length can be checked against a commonly known limit, but the user didn't confirm the account's actual limit (some accounts have extended limits).
2. Mark **Hashtags are formatted and relevant** as **Fail** — `# export` has a broken space, and `#trending #followus #like #share` are generic engagement-bait tags unrelated to the post's actual content.
3. Mark **Media meets platform specs** as **Could not determine** — no dimensions/format were supplied to check against.
4. Mark **Alt text or captions present on media** as **Fail** — the image tag has no alt attribute.
5. Mark **Links are tracked and resolve to a real destination** as **Could not determine** — the link isn't a placeholder, but no tracking-parameter convention was supplied to check the `bit.ly` link against.
6. Mark **No scheduling conflict** as **Could not determine** — no posting calendar was supplied.
7. Summarize clearly that this is not ready to publish as-is, phrased as input to a decision rather than the decision itself: "two checks fail and three can't be confirmed; here's what needs attention before a publish decision is made."

## Deliberately weak conclusions

These responses should fail the learning objective:

- "Looks good, ready to post!" — ignores the broken hashtag and missing alt text.
- Editing the caption to fix the hashtags or add alt text, instead of just reporting it.
- Marking "Within the platform's character limit" as **Pass** by assuming a limit the user never confirmed.
- Telling the user "don't post this" as if it were the skill's decision to make.
