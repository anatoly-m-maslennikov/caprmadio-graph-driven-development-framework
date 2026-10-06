---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-REQU-398--all-toml-artifact-requirement
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-EVAL-026--verbose-project-settings-test-case
      - CAPRMEDIO-GOV-EVAL-028--native-package-successors-test-case
      - CAPRMEDIO-GOV-EVAL-029--legacy-structured-snapshots-test-case
---

# Test Case — Complete the all-TOML artifact cutover

The repository and migration suites require zero `.yaml` or `.yml` files under
`dset/` and zero DSET Markdown YAML-frontmatter carriers. Every former
standalone YAML edition has one distinct adjacent `<stem>.legacy.toml` envelope
unless parsed equality permits the current owner to serve both roles.

The transition ledger covers every changed carrier exactly once. Normalized
values, selector fragments, Markdown bodies, physical links, classifications,
current owners, generated views, and the bootstrap bundle remain valid. The
transaction rejects collisions, incomplete mappings, stale input, partial
resealing, semantic drift, loss, broken references, and rollback mismatch.
Preview and apply are both no-ops after cutover.

JSON Schema and other externally prescribed formats remain outside this Test.
This Test definition is immutable; runs and Evidence Records are separate.

## Primary claim

Deterministic tests prove complete lossless TOML cutover of every CAPRMEDIO-owned YAML artifact and Markdown YAML-frontmatter carrier with reference closure, rollback parity, and second-run idempotency.

## Rationale

A zero-YAML claim is valid only when every historical edition, link, seal, and normalized value is preserved in the new representation.
