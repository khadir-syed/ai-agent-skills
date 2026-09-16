# Synthetic example: a clear content-publish request

## User prompt

> Use the request-router-agent-controlled skill: write something for launch
> day about our new export feature, should feel exciting. Draft it to
> blog-post.md.

## Expected shape

**Step 1 (classify):** match this to
**content-publish-readiness-agent-controlled**, confidence **Clear** — it
asks for a piece of content to be drafted and checked, names no failure and
no product-launch-readiness question, and mentions a channel-shaped output
(`blog-post.md`), all `content-publish-readiness-agent-controlled` signals
in [references/target-agents.md](../references/target-agents.md). State
this and **stop**.

On approval, hand off — the rest of the session should read like that
agent's own example,
[launch-blog-post.md](../../../agents/content/content-publish-readiness-agent-controlled/examples/launch-blog-post.md).

## Deliberately weak responses

These should fail the learning objective:

- Routing to `feature-launch-readiness-agent-controlled` because the words
  "launch day" appear — nothing here asks whether the *feature* is ready to
  ship; the ask is to write and check a piece of *content* about it.
- Beginning the gap investigation or drafting in the same turn as the
  classification.
