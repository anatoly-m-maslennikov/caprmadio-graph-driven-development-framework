---
subject_scopes:
  - feature-boundary
version: 8
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Define the PROJECTION_REBUILD Tool unit

`PROJECTION_REBUILD` must be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/PROJECTION_REBUILD`, and realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/PROJECTION_REBUILD/`; it derives the complete affected Projection set from changed source frontiers, orders rebuilds by declared dependencies, previews every output effect, materializes only explicitly approved outputs, and verifies currentness and idempotence after publication.
