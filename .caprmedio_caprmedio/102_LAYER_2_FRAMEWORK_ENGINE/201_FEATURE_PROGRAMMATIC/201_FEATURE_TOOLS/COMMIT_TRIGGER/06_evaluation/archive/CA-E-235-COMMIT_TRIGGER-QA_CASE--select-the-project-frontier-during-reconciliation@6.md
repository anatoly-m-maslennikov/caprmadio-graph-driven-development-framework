---
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 6
updated_at: 2026-09-01 02:30:00 +0400
relations:
  evaluation_for:
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Select the project frontier during reconciliation

## Test case

Given admitted, ignored, pipeline-owned, and ambiguous repository paths, when the background reconciliation worker observes the frontier and the pure manager classifies its typed facts, then ordinary Git-eligible files and .caprmedio files are eligible, Git-ignored paths and top-level dot-directories other than .caprmedio are excluded, pipeline-owned Journal and Runtime writes are correlated rather than admitted as new subjects, and ambiguous ownership becomes blocked. COMMIT_TRIGGER performs no frontier scan.

## Sources

- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md)
