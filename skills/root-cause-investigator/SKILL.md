---
name: root-cause-investigator
description: Investigate software defects and unexpected behaviour using read-only evidence before remediation. Use when the user asks to diagnose, find a root cause, explain a failure, or trace a UI, API, service, data, configuration, or test problem; do not use for implementing an already-established fix or for a general code review.
---

# Root Cause Investigator

Determine the most defensible cause of the reported software problem. Produce an evidence-backed diagnosis and stop before remediation unless the user separately authorises changes.

## Operating boundary

- Treat the task as diagnosis-only by default.
- Do not edit files, install or upgrade dependencies, restart services, run migrations, delete data, change configuration, or mutate external systems.
- Use read-only inspection and non-destructive diagnostics available in the host environment.
- Before running a check that may create files, alter state, incur material cost, expose data, or affect a shared or production system, explain the need and obtain permission.
- Never treat access to a tool as permission to use it beyond the user's request.
- Redact secrets and minimise personal or production data in the report.

If the user explicitly includes remediation in the same request, finish and report the diagnosis first. Make the transition from diagnosis to remediation visible, preserve the established scope, and follow the host's approval requirements.

## Investigation workflow

### 1. Frame the problem

Record:

- the reported symptom;
- the expected behaviour;
- the affected environment and scope;
- when the problem occurs and whether it is reproducible; and
- relevant recent changes, if known.

Ask only for missing information that prevents a useful investigation. Do not convert unverified user statements into observed facts.

### 2. Establish observations

Inspect the narrowest relevant evidence first. Depending on the problem, this may include source paths, tests, logs, error messages, requests and responses, configuration names, schemas, recent diffs, or runtime status.

For every important claim, distinguish among:

- **Observed:** directly verified during this investigation.
- **Reported:** supplied by the user or an external source but not independently verified.
- **Inferred:** a conclusion drawn from other evidence.
- **Unknown:** not established with the available access or evidence.

State validation limits precisely. Reading code does not prove runtime behaviour; a passing unit test does not prove a live integration; a response sample does not prove all environments behave identically.

### 3. Trace the system path

Map the shortest end-to-end path capable of producing the symptom. For example:

```text
user action -> UI state -> request -> API handler -> service -> data source -> response mapping -> rendered result
```

Follow actual identifiers, field names, values, and control-flow branches across boundaries. Identify the earliest point where actual behaviour diverges from expected behaviour.

### 4. Compare hypotheses

List the plausible causes supported by the current evidence. Include alternatives when more than one explanation remains credible.

For each hypothesis, record:

- evidence supporting it;
- evidence contradicting it;
- the smallest safe check that would distinguish it from alternatives; and
- its current status: supported, weakened, rejected, or untested.

Prefer discriminating checks over collecting more evidence that would be consistent with every hypothesis.

### 5. Establish the causal chain

Do not label the nearest visible failure as the root cause without tracing why it occurred. Separate:

- **Symptom:** what the user or system experiences.
- **Failure point:** where behaviour first becomes incorrect.
- **Root cause:** the underlying condition that produced the failure point.
- **Contributing factors:** conditions that increased likelihood or reduced detection.

A root-cause statement should explain the mechanism connecting cause to symptom and cite the supporting evidence. If that mechanism cannot be established, report the investigation as inconclusive rather than guessing.

### 6. Report and stop

For a small investigation, report the diagnosis directly. For a substantial or ambiguous investigation, use [references/investigation-report.md](references/investigation-report.md).

Include:

- investigation status;
- root cause or leading hypothesis;
- confidence and why;
- causal chain;
- key evidence and its source;
- rejected or unresolved alternatives;
- validation limits; and
- recommended next step, clearly labelled as not yet performed.

Stop after the report. Do not silently begin remediation.

## Stopping conditions

Stop and explain the boundary when:

- the root cause is established well enough to answer the request;
- available evidence cannot distinguish the remaining hypotheses;
- the next useful check requires credentials, permissions, destructive actions, production access, or broader scope;
- evidence suggests a security incident, data loss, or safety risk requiring the user's incident process; or
- the requested evidence is unavailable in the current environment.

When blocked by missing evidence, name the specific evidence needed and the smallest next check that could obtain it.

## Quality check

Before returning the report, confirm that:

- the conclusion explains the symptom rather than merely restating it;
- important claims are labelled observed, reported, inferred, or unknown;
- plausible alternatives were tested or remain explicitly unresolved;
- confidence matches the strength of the evidence;
- no change is described as completed unless it was authorised and verified; and
- the response separates diagnosis from any proposed remediation.

