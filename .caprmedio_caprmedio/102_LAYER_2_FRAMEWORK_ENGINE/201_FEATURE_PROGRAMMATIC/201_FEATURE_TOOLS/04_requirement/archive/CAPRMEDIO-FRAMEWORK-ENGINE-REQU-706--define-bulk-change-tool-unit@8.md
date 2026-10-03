---
subject_scopes:
  - feature-boundary
version: 8
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  relates_to:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-536--plan-an-artifact-migration
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-537--apply-an-artifact-migration
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-538--verify-an-artifact-migration
---
# Define the BULK_CHANGE Tool unit

`BULK_CHANGE` must be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE`, and realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/BULK_CHANGE/`; it composes registered create, structured patch, relation change, rename, move, lifecycle, and replacement operations over one sealed target set, emits a complete mutation-free plan, and applies an explicitly approved unchanged plan as one validated rollbackable transaction.
