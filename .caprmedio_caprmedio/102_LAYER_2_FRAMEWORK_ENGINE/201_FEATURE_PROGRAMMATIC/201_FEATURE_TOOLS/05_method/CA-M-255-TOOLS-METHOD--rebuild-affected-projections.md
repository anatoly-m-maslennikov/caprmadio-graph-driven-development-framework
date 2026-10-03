---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 8
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1156
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Rebuild affected Projections

## Applicable when

use this Method **when** `PROJECTION_REBUILD` **must** refresh Projections affected by declared changed source frontiers.

## Procedure

1. confirm that `PROJECTION_REBUILD` is registered as one `unordered_unit` Doer owned immediately by `TOOLS` at Structural level `4`, with prefix `PROJECTION_REBUILD`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PROJECTION_REBUILD`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/PROJECTION_REBUILD/`.
2. resolve the changed source frontiers **and** derive the complete affected Projection set using declared Projection dependencies.
3. order affected Projections by those dependencies **and** reject an unresolved **or** cyclic dependency order.
4. preview **every** derived output effect, including output identity, source frontier, **and** expected currentness state.
5. materialize **only** the explicitly approved preview outputs **and** attach their source frontier **and** generator provenance; verify currentness **and** idempotence **after** publication by rebuilding against the unchanged frontier **and** comparing the resulting outputs.

## Outcome

one `PROJECTION_REBUILD` operation materializes **every** **and** **only** affected approved Projection **in** dependency order **and** verifies its currentness **and** idempotence.

## Failure or stop

do **not** publish on an unresolved dependency, incomplete affected set, unapproved output, changed source frontier, failed currentness check, **or** failed idempotence check.
