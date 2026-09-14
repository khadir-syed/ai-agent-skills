# PRD section format

Use only the sections the source material actually supports. Mark anything unsupported as an open question rather than inventing content.

```markdown
## Problem Statement
What problem this solves and for whom, based on the supplied source.

## Goals
What success looks like, stated as concretely as the source material allows.

## Non-Goals
What this explicitly does not attempt to solve, if stated.

## User Stories
"As a [user], I want [capability], so that [benefit]" — only for stories
actually implied by the source material.

## Success Metrics
Only if the source states or implies a checkable measure. Otherwise list
as an open question rather than inventing a number.

## Open Questions
Anything the source material doesn't settle — missing scope, unconfirmed
metrics, unresolved stakeholder conflicts.
```

Rules:

- Omit any section with nothing to draft from.
- Do not invent a success metric, timeline, or user segment not present in the source material — list it under Open Questions instead.
- If the source material came from a Requirements Gap Investigator report, carry its unresolved gaps directly into Open Questions rather than silently resolving them.
