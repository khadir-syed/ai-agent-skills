# Target agents and routing criteria

What the Request Router hands off to, and the concrete signals that separate
one from the other. Classification should cite these signals directly, not a
general impression of the request.

## bug-fix-agent (software)

Located at `../../agents/software/bug-fix-agent/`. Route here when the
request:

- names a failing test, an error message, or a defect in existing behavior;
- describes something that used to work (or should already work) and
  currently doesn't; or
- includes reproduction evidence — a stack trace, a failing assertion, an
  error log, or steps to reproduce.

Signals: "fails", "throws", "broken", "expected X, got Y", "regression", a
pasted stack trace or test output.

## feature-launch-readiness-agent-controlled (product)

Located at `../../agents/product/feature-launch-readiness-agent-controlled/`.
Route here when the request:

- describes a feature or change that has not shipped yet, with a launch or
  rollout in mind;
- asks for a brief, a requirements-gap check, or a readiness assessment
  rather than a fix; or
- has no failure evidence — it's about deciding whether something is ready,
  not why something broke.

Signals: "add", "launch", "ship", "roll out", a target date, or an explicitly
absent PRD/rollout plan/success metric.

## content-publish-readiness-agent-controlled (content)

Located at `../../agents/content/content-publish-readiness-agent-controlled/`.
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

- General questions, social-media requests, or anything with no failure
  evidence, no launch context, and no content-drafting ask: none of the
  three agents apply. Say so plainly rather than forcing a match.
- A request describing a bug in a feature that hasn't shipped yet carries
  signals of both `bug-fix-agent` and
  `feature-launch-readiness-agent-controlled` — flag this explicitly as
  ambiguous instead of picking one. Ask the user which lens they want: is a
  launch otherwise ready and blocked by this one defect (→ `bug-fix-agent`),
  or is the launch itself not yet ready and this is one of several open gaps
  (→ `feature-launch-readiness-agent-controlled`)?
- A request to write launch-announcement content for a feature that isn't
  actually ready to ship carries signals of both
  `feature-launch-readiness-agent-controlled` and
  `content-publish-readiness-agent-controlled` — flag this as ambiguous too.
  Ask whether the immediate need is checking the feature's own launch
  readiness (→ `feature-launch-readiness-agent-controlled`) or drafting and
  checking the announcement content itself, treating the feature as already
  a given (→ `content-publish-readiness-agent-controlled`).
