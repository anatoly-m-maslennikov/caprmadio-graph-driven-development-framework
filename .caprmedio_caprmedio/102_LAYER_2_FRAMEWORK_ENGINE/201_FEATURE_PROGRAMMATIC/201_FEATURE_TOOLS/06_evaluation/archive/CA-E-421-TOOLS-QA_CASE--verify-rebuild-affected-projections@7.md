---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 7
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-255
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify rebuild affected Projections

## Claim checked

CA-M-255 derives every affected Projection, materializes only approved outputs in dependency order, and verifies currentness and idempotence.

## Applicable when

Apply whenever affected-Projection derivation, dependency ordering, preview approval, currentness, or idempotence handling changes.

## Test case

Inspect the registered `PROJECTION_REBUILD` unit, then use changed source frontiers that affect one upstream Projection and one dependent Projection. Preview, approve, and rebuild them, then rebuild against the unchanged frontier and compare outputs; repeat with the dependent Projection omitted from the affected set.

## Acceptance criteria

`PROJECTION_REBUILD` has prefix `PROJECTION_REBUILD`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/PROJECTION_REBUILD`, and realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/PROJECTION_REBUILD/`. The valid case previews and materializes both affected outputs in dependency order with source-frontier provenance; the repeated build is identical and current. The incomplete affected set produces no accepted publication.

## Failure disposition

Reject the realization and preserve changed frontiers, dependency graph, preview, approvals, output provenance, repeated-output comparison, and incomplete-set finding.
