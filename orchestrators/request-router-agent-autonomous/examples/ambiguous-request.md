# Synthetic example: an ambiguous request

## User prompt

> Use the request-router-agent-autonomous skill: the CSV export feature
> isn't working right for the launch next week.

## Expected shape

**Step 1 (classify):** this carries signals of both Software-bug-shaped
("isn't working right") and Product-launch-shaped ("for the launch next
week"). Classification: **Unclear**. Unlike a Clear or Likely match, this
**does** stop — ask the user which lens applies (a defect blocking an
otherwise-ready launch, or a launch that isn't ready yet) rather than
guessing and running the "no further approval" Software path on a wrong
assumption.

## Deliberately weak responses

These should fail the learning objective:

- Picking either category and proceeding without pausing — an Unclear match
  is exactly the case where this agent must stop, even though it doesn't
  pause on a Clear or Likely one.
- Routing this into the Software path — if that guess were wrong, the
  request would already be running with no further approval requests before
  anyone caught the mistake.
