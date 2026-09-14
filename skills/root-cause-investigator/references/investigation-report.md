# Investigation report template

Use this template for investigations with several system boundaries, competing hypotheses, or meaningful uncertainty. Omit sections that add no value, but preserve the distinction between evidence, inference, and unknowns.

## Problem statement

- **Reported symptom:**
- **Expected behaviour:**
- **Affected scope:**
- **Environment:**
- **Reproduction status:** reproduced, intermittent, not reproduced, or unknown

## Investigation status

Choose one:

- **Established:** evidence supports a causal mechanism and credible alternatives have been rejected.
- **Probable:** one hypothesis is best supported, but an important confirming check is unavailable.
- **Inconclusive:** available evidence cannot distinguish the remaining hypotheses.
- **Not reproducible:** the symptom was not observed and existing evidence is insufficient to establish its cause.

## Root cause or leading hypothesis

State the cause in one or two sentences. Explain the mechanism, not only the failing component.

## Confidence

- **High:** the failure was reproduced or directly observed, the causal chain was verified, and credible alternatives were rejected.
- **Medium:** multiple pieces of evidence support the conclusion, but part of the chain is inferred or a confirming check is unavailable.
- **Low:** the conclusion is mainly inferential and competing explanations remain credible.

Explain why the selected confidence level is justified.

## Causal chain

```text
underlying condition -> failure point -> propagated effect -> user-visible symptom
```

## Evidence

| Classification | Evidence | Source | What it establishes |
|---|---|---|---|
| Observed, reported, inferred, or unknown | Concise finding | File, line, log, command, response, or user report | Supported conclusion and limits |

## Hypotheses considered

| Hypothesis | Supporting evidence | Contradicting evidence | Status |
|---|---|---|---|
| Candidate cause | Evidence or none | Evidence or none | Supported, weakened, rejected, or untested |

## Contributing factors

List conditions that made the defect more likely or harder to detect. Do not present a contributing factor as the root cause unless the causal mechanism supports that conclusion.

## Validation limits

State what was not verified, which environments were not inspected, and what the available checks do not prove.

## Recommended next step — not performed

Describe the smallest reasonable remediation or confirming check. Make clear that it has not been executed and requires separate authorisation when it would change state.

