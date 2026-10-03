---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 11
updated_at: "2026-09-17 02:43:52 +0000"
relations:
  evaluation_for:
    - CA-M-254
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify change one sealed target set

## Claim checked

CA-M-254 applies **only** an explicitly approved unchanged complete `BULK_CHANGE` plan as one validated rollbackable transaction.

## Applicable when

apply whenever registered bulk operations, plan sealing, approval gating, transaction validation, **or** rollback handling changes.

## Test case

inspect the registered `BULK_CHANGE` unit, **then** use one sealed target set **and** registered structured-patch **and** rename effects **to** derive a complete plan. change one target **after** plan approval, **then** restore it **and** apply the unchanged approved plan.

## Acceptance criteria

`BULK_CHANGE` has prefix `BULK_CHANGE`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/BULK_CHANGE`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/BULK_CHANGE/`. the stale plan changes nothing. the unchanged plan applies **every** declared effect exactly once, exposes one transaction identity **and** final target frontier, **and** leaves no unplanned mutation.

## Failure disposition

reject the realization **and** preserve target set, approved plan, precondition comparison, declared effects, final frontier, transaction identity, **and** rollback evidence.

## Post-effect failure coverage

use an independent fixture **and** the same admitted rollback boundary **to** exercise a failure **after** **`>=1`** planned effect has changed a Carrier **or** reference. inject a later effect failure **or** failed final verification. **if** the complete transaction is published atomically, inject the fault **after** publication **and** **before** successful verification.

- preserve the exact approved plan, sealed before-state, actual fault position, **and** changed-then-restored values.
- verify complete restoration of the planned mutable Carrier **and** reference frontier, **without** modifying unrelated targets **or** erasing accepted Journal history.
- report a failed transaction with its recovery outcome, **not** a successful final frontier. incomplete **or** unverified recovery fails this Evaluation.
- the existing stale-plan rejection case remains required but does **not** establish post-effect rollback.
