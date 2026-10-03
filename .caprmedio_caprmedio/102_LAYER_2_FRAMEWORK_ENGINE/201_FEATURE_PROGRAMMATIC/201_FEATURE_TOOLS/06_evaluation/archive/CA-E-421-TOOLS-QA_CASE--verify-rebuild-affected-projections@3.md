---
atom_id: CA-E-421
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-04 03:10:59 +0400
relations:
  evaluation_for:
    - CA-M-255
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
