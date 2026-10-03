---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Validate Artifact Catalog"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Revision"
    - "Projection"
version: 2
updated_at: "2026-09-17 03:15:32 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Validate one generic Artifact catalog

Validate Artifact Catalog **means** the reusable Action that produces a complete read-**only** conformance result for one registered Artifact catalog against its declared source frontier under CA-R-1142. its modeled boundary is the complete requested result; partial comparison, incomplete attribution, **or** an unreported unresolved input is **not** an independently successful outcome.

## Applicable when

use this Action **when** one registered Artifact catalog **must** be checked against its declared current authoritative source frontier.

## Action

1. resolve the catalog definition, catalog carrier, **and** its declared authoritative source frontier.
2. recompute the expected catalog membership, ordering, **and** source facts from the declared authority **without** rebuilding **or** modifying the catalog.
3. compare the existing catalog **to** the expected result **and** classify missing, stale, duplicate, unknown, **and** inconsistent entries separately.
4. attribute each discrepancy **to** the catalog entry, expected authority contribution, **and** observed source frontier.
5. return a failed validation **when** **any** discrepancy exists; do **not** repair, regenerate, **or** accept the catalog.

## Outcome

one read-**only** catalog validation states whether the catalog exactly matches its declared authoritative source frontier **and** lists **every** discrepancy.

## Failure or stop

fail closed **when** the catalog definition, source frontier, **or** catalog carrier is unresolved **or** malformed; never mutate the catalog **or** authority sources.
