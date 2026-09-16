# Synthetic example: an ambiguous request

## User prompt

> Use the request-router-agent-controlled skill: the CSV export feature isn't
> working right for the launch next week.

## Expected shape

**Step 1 (classify):** this carries signals of both — "isn't working right"
(`bug-fix-agent`) and "for the launch next week"
(`feature-launch-readiness-agent-controlled`) — per the "when neither fits,
or both seem to" section of
[references/target-agents.md](../references/target-agents.md). Confidence:
**Unclear**. Do not pick either agent; ask the user directly: is this a
defect blocking an otherwise-ready launch (→ `bug-fix-agent`), or is the
launch itself not yet ready and this is one of several open gaps (→
`feature-launch-readiness-agent-controlled`)? **Stop** here regardless.

## Deliberately weak responses

These should fail the learning objective:

- Picking `feature-launch-readiness-agent-controlled` because the launch
  date was mentioned, without ever flagging the bug-shaped language.
- Treating "isn't working right" as enough to confidently route to
  `bug-fix-agent` while ignoring the launch context entirely.
- Any response that produces a **Clear** or **Likely** confidence label here
  — this example exists specifically to test that **Unclear** is used
  honestly, not just as a fallback for requests with zero signals.
