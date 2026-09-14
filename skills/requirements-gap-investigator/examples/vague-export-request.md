# Synthetic example: "Add an export button"

This fictional case can be used to test or teach the Requirements Gap Investigator without a real product backlog.

## User prompt

> Use the Requirements Gap Investigator. Sales asked for "an export button on the reports page." Figure out what's actually needed before we write it up.

## Evidence packet

Treat the following as the supplied context.

```text
Slack message from Sales lead (quoted):
  "Can we get an export on the reports page? Customers keep asking."

Linked ticket description (written by a PM):
  "Export button for reports page."

No further detail in the ticket. No mention of file format, which
report(s), permissions, or whether this applies to the mobile app.
```

## Expected investigation shape

A strong response should:

1. Label the Slack quote and ticket text as **stated**, and note everything else about the request is unknown.
2. Flag concrete gaps: export format (CSV? PDF? both?), which report(s) on a page that may show several, whether it applies on mobile, and whether all users or only certain roles should see the button.
3. Note the stated goal ("customers keep asking") without inventing an interpretation of what customers actually want beyond that.
4. Present at least two plausible interpretations (e.g. "one-click CSV export of the current view" vs. "a scheduled export/report subscription feature") without picking one as correct.
5. Recommend who to confirm each gap with (e.g. the Sales lead for the customer need, design/eng for scope) — without drafting a PRD.
6. Stop before writing any requirements document.

## Deliberately weak conclusions

These responses should fail the learning objective:

- "Add a CSV export button" — invents a format and scope never stated.
- Drafting a full PRD directly from the Slack message.
- "This is unclear" with no breakdown of *which* parts are unclear or who could resolve them.
- Treating the PM's ticket wording as if it settles the format or scope question, when it only restates the same one-line request.
