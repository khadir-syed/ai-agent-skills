# Synthetic example: launch post underperformed

This fictional case can be used to test or teach the Post Performance Investigator without a real social account.

## User prompt

> Use the Post Performance Investigator. Our export-feature launch post on Instagram flopped compared to usual. Figure out why.

## Evidence packet

Treat the following as the supplied context.

```text
Post: Instagram feed post announcing the export feature, posted
Tuesday 9am local time.

Reported metric: reach 400, versus a typical post's reach of ~3,000
(average of last 10 posts, per the marketing lead).

Observed: the post was a single static image with a two-line
caption and no hashtags. The last 10 posts averaged 4-6 hashtags
and a short video/carousel format.

Observed: no paid promotion was applied to this post; three of the
last 10 posts had.

Unknown: whether Instagram's algorithm changed recently, and
whether any competing content was posted by others that morning.
```

## Expected investigation shape

A strong response should:

1. Label the reach numbers as **reported** (a comparison stated by the marketing lead, not independently verified against a dashboard) and the format/hashtag/promotion facts as **observed** (directly supplied, specific details).
2. Compare hypotheses: format mismatch (static image vs. usual video/carousel), missing hashtags, no paid promotion, and unknown algorithm/competition factors — with each labelled supported, weakened, rejected, or untested based on the evidence given.
3. Note that the "usual ~3,000" baseline is itself an average, not a guarantee, so part of the gap may be normal variance rather than fully explained by this post's specific choices.
4. State validation limits: no analytics dashboard was inspected directly, and no data on the "no paid promotion" comparison posts was reviewed to confirm this pattern holds beyond the last 10 posts.
5. Report a leading explanation (most likely a combination of format change and no paid boost) without treating it as certain, and recommend a next check — e.g. reviewing whether this format worked before with promotion — clearly marked as not performed.
6. Stop without drafting a replacement post or recommending a specific fix as decided.

## Deliberately weak conclusions

These responses should fail the learning objective:

- "The post flopped because Instagram changed its algorithm" — invents a cause with no supporting evidence, ignoring the format/promotion differences actually observed.
- Treating the reported ~3,000 average as an exact guaranteed baseline rather than reported.
- Drafting a new, "better" launch post as part of the investigation response.
- "Not enough hashtags" stated as the sole, certain cause when multiple untested factors remain.
