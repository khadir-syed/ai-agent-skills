# Target agents and routing criteria

What the autonomous Request Router hands off to, and the concrete signals
that separate one category from another. Classification should cite these
signals directly, not a general impression of the request. The category
signals are identical to the controlled router's — what differs here is
*which* agent within each category this one hands off to (the autonomous
counterpart, not the controlled one).

## Software-bug-shaped → test-fix-loop-agent

Located at `../../agents/software/test-fix-loop-agent/`. This is real code,
not a `SKILL.md` — see [How it works](../SKILL.md) for how the handoff
actually happens, and its own honesty requirement about disclosing that this
path never asks for approval.

Route here when the request:

- names a failing test, an error message, or a defect in existing behavior;
- describes something that used to work (or should already work) and
  currently doesn't; or
- includes reproduction evidence — a stack trace, a failing assertion, an
  error log, or steps to reproduce.

Signals: "fails", "throws", "broken", "expected X, got Y", "regression", a
pasted stack trace or test output.

## Product-launch-shaped → feature-launch-readiness-agent-autonomous

Located at `../../agents/product/feature-launch-readiness-agent-autonomous/`.
Route here when the request:

- describes a feature or change that has not shipped yet, with a launch or
  rollout in mind;
- asks for a brief, a requirements-gap check, or a readiness assessment
  rather than a fix; or
- has no failure evidence — it's about deciding whether something is ready,
  not why something broke.

Signals: "add", "launch", "ship", "roll out", a target date, or an explicitly
absent PRD/rollout plan/success metric.

## Content-publish-shaped → content-publish-readiness-agent-autonomous

Located at `../../agents/content/content-publish-readiness-agent-autonomous/`.
Route here when the request:

- asks for a piece of content — a blog post, article, campaign copy, or
  similar — to be drafted and checked before it publishes;
- has no failure evidence and no product/feature launch context — it's about
  writing and readiness-checking a piece of content, not fixing code or
  shipping a feature; or
- mentions a publish date, channel, audience, or tone, rather than a rollout
  plan or a test.

Signals: "write", "draft", "blog post", "article", "campaign", "publish",
a channel (blog, email, social), or an explicitly absent audience/tone/length.

## When none fit, or more than one seems to

This is the one case where this agent stops instead of proceeding — see
[SKILL.md](../SKILL.md)'s stopping conditions.

- General questions, social-media requests, or anything with no failure
  evidence, no launch context, and no content-drafting ask: none of the
  three agents apply.
- A bug in a feature that hasn't shipped yet carries signals of both
  software and product categories.
- A request to write launch-announcement content for a feature that isn't
  actually ready to ship carries signals of both product and content
  categories.
