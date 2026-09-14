# Synthetic example: "Write something for launch day"

This fictional case can be used to test or teach the Content Brief Gap Investigator without a real product launch.

## User prompt

> Use the Content Brief Gap Investigator. Marketing asked for "something for launch day" about our new export feature. Figure out what's actually needed before we write it up.

## Evidence packet

Treat the following as the supplied context.

```text
Slack message from Marketing lead (quoted):
  "Can we get something ready for launch day about the export
  feature? Should feel exciting."

Linked ticket description (written by a PM):
  "Launch content for export feature."

No further detail in the ticket. No mention of format (blog post?
email? social post?), channel, target length, audience, or what
"exciting" should mean in terms of tone.
```

## Expected investigation shape

A strong response should:

1. Label the Slack quote and ticket text as **stated**, and note everything else about the request is unknown.
2. Flag concrete gaps: content format (blog, email, social, all three?), target channel and audience, desired length, and what "exciting" means as a tone direction.
3. Note the stated goal ("something exciting for launch day") without inventing an interpretation of what "exciting" means beyond that.
4. Present at least two plausible interpretations (e.g. "a short announcement blog post for existing customers" vs. "a social campaign aimed at new-user acquisition") without picking one as correct.
5. Recommend who to confirm each gap with (e.g. the Marketing lead for tone and channel, product for feature details) — without drafting any content.
6. Stop before writing any content.

## Deliberately weak conclusions

These responses should fail the learning objective:

- "Here's an exciting blog post about the export feature" — invents a format and tone never confirmed.
- Drafting social captions directly from the Slack message.
- "This brief is too vague" with no breakdown of *which* parts are unclear or who could resolve them.
- Treating the PM's ticket wording as if it settles the format question, when it only restates the same one-line request.
