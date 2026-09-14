# Synthetic example: UI and API field mismatch

This fictional case can be used to test or teach the Root Cause Investigator without accessing a real application.

## User prompt

> Use the Root Cause Investigator. The Orders page says "No orders found," but the browser network response contains three orders. Diagnose the problem and do not change anything.

## Evidence packet

Treat the following as supplied evidence. A real investigation should verify equivalent evidence in the available environment.

### API response

```json
{
  "items": [
    { "id": "A-101", "status": "ready" },
    { "id": "A-102", "status": "pending" },
    { "id": "A-103", "status": "ready" }
  ],
  "total": 3
}
```

### UI behaviour description

The page reads the response body successfully. It renders an order row for every entry in a property named `orders`. When `orders.length` is zero, it shows "No orders found."

### Recent change note

The API response contract was changed last week from an `orders` property to an `items` property. No corresponding UI change is recorded in the evidence packet.

## Expected investigation shape

A strong response should:

1. Label the prompt and evidence packet as reported or supplied evidence, not as live observations.
2. Trace the path from the successful response to response mapping and UI rendering.
3. Identify the field-name boundary as the earliest described divergence.
4. Compare the field mismatch with alternatives such as request failure, empty backend data, filtering, or rendering failure.
5. Explain why the packet weakens those alternatives without claiming they were tested in a live application.
6. Report the root cause as probable rather than established, because no source files or runtime were directly inspected.
7. Stop before changing the UI or API.

## Example conclusion

**Investigation status:** Probable

**Confidence:** Medium

The leading root cause is an uncoordinated response-contract change. The API now supplies records under `items`, while the UI behaviour description says it reads `orders`. The UI therefore evaluates a missing or default-empty collection and renders the empty state even though the response contains three records.

The described successful response weakens request-failure and empty-database hypotheses. A filtering defect remains possible but is less consistent with the stated behaviour. The conclusion is not established because the UI mapping code and live runtime were not inspected.

**Recommended next check — not performed:** inspect the UI response type and mapping at the network-to-state boundary and confirm which property is read. Do not edit it without separate authorisation.

## Deliberately weak conclusions

These responses should fail the learning objective:

- "The frontend is broken." This names a broad area but provides no mechanism.
- "Rename `orders` to `items`." This jumps to a fix without reporting the evidence and uncertainty.
- "The API change definitely caused it." The supplied packet supports that conclusion, but live behaviour was not verified.
- "The database returned no rows." This contradicts the supplied response.
