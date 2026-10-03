---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - provenance
tier: core
version: 3
updated_at: 2026-08-23 15:00:38
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-353--bind-proof-records-to-dependency-frontiers
---
# Encode proof frontiers as typed reference lists

CAPRMEDIO MUST encode a proof carrier's machine-readable dependency frontier as `proof_frontier_refs`, a YAML list whose entries use `atom:<atom-name>@<version>,<updated_at>` for exact Atom revisions or `<kind>:<repository-relative-locator>@sha256:<digest>` for `file`, `configuration`, `evaluator`, and `input` dependencies. An `environment` dependency uses `environment:<name>@sha256:<fingerprint>`. Prose `invalidation_conditions` make currentness `unknown` until a governed checker resolves them.
