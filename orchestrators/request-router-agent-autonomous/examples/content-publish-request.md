# Synthetic example: a clear content-publish request

## User prompt

> Use the request-router-agent-autonomous skill: write something for launch
> day about our new export feature, should feel exciting. Draft it to
> blog-post.md.

## Expected shape

**Step 1 (classify, no pause):** match to **Content-publish-shaped**, citing
the request for drafted content and the absence of any product-readiness or
failure signal. No approval requested for the classification — proceed
directly to the handoff in the same response.

**Step 2 (hand off):** adopt
[content-publish-readiness-agent-autonomous](../../../agents/content/content-publish-readiness-agent-autonomous/)'s
own instructions — gap investigation runs with no pause, then the one
mandatory stop before writing `blog-post.md`, then the readiness checklist
runs with no further pause after the write.

## Deliberately weak responses

These should fail the learning objective:

- Routing to `feature-launch-readiness-agent-autonomous` because "launch
  day" appears — nothing here asks whether the feature itself is ready to
  ship.
- Skipping the mandatory stop before writing `blog-post.md`.
