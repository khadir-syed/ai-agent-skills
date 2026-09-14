---
name: post-performance-investigator
description: Investigate why a published social media post performed differently than expected — under or over — using evidence labeled observed/reported/inferred/unknown, and stop before recommending changes. Use when a post's engagement or reach doesn't match expectations; do not use on a post that hasn't been published yet or to draft new posts.
---

# Post Performance Investigator

Determine the most defensible explanation for why a published social media post performed differently than expected. Produce an evidence-backed diagnosis and stop before recommending any change unless the user separately authorises that.

## Operating boundary

- Treat the task as diagnosis-only by default. Do not draft a follow-up post, edit the original post, or change any scheduling/targeting settings.
- Use only the metrics, comments, and context the user supplies or that is directly available; do not invent engagement numbers or audience behaviour.
- Distinguish an actual platform metric from someone's characterisation of it (e.g. "it flopped" is not the same as "reach was 400, versus a 3,000 average").
- Redact or generalise any real customer names or personal data found in comments before including them in the report.

If the user explicitly includes "so what should we post next" in the same request, finish and report the diagnosis first, make the transition to drafting visible, and follow the host's approval requirements for that separate step.

## Investigation workflow

### 1. Frame the problem

Record:

- the platform and post in question;
- the expected performance (a stated goal, a typical baseline, or a comparison post);
- the actual reported performance and how it was measured; and
- when the post ran and any surrounding context (other posts, promotions, external events).

Ask only for missing information that blocks a useful investigation. Do not convert someone's impression ("nobody saw it") into an observed fact.

### 2. Establish observations

For every important claim, label it as:

- **Observed:** a specific metric or fact directly supplied (impressions, reach, engagement rate, click-through, posting time, format).
- **Reported:** a characterisation given by the user or a stakeholder but not backed by a specific number (e.g. "engagement felt low").
- **Inferred:** a conclusion drawn from patterns in other posts or general platform behaviour — not stated by anyone for this post specifically.
- **Unknown:** not established by anything available.

State validation limits precisely: a single post's numbers do not prove a trend, and a comment thread's tone does not prove the whole audience's reaction.

### 3. Compare hypotheses

List the plausible explanations supported by the current evidence — for example, posting time, format mismatch for the platform, algorithm changes, competing content that day, weak hook/caption, or the goal itself being miscalibrated against a realistic baseline. For each hypothesis, record:

- evidence supporting it;
- evidence contradicting it;
- the smallest additional evidence that would distinguish it from alternatives; and
- its current status: supported, weakened, rejected, or untested.

### 4. Establish the likely explanation

Do not label the first plausible-sounding factor as the explanation without checking it against the evidence. Separate:

- **Symptom:** the performance gap as reported.
- **Likely factor(s):** what the evidence best supports.
- **Contributing factors:** conditions that plausibly amplified or masked the effect.

If the evidence cannot distinguish between two or more explanations, report that explicitly rather than picking one.

### 5. Report and stop

Report:

- investigation status: explained, partially explained, or inconclusive;
- the leading explanation(s) and confidence;
- key evidence and its source, labelled observed/reported/inferred/unknown;
- rejected or unresolved alternatives;
- validation limits; and
- a recommended next check, clearly labelled as not yet performed.

Stop after the report. Do not draft a new post or recommend a specific content change as if it were already agreed.

## Stopping conditions

Stop and explain the boundary when:

- the explanation is established well enough to answer the request;
- available evidence cannot distinguish the remaining hypotheses;
- the next useful check requires platform analytics access the user hasn't supplied; or
- the user asks you to also decide what to post next — that is out of scope for this skill.

## Quality check

Before returning the report, confirm that:

- the conclusion explains the performance gap rather than merely restating it;
- important claims are labelled observed, reported, inferred, or unknown;
- plausible alternatives were considered or remain explicitly unresolved; and
- no follow-up content was drafted or recommended as a settled decision.
