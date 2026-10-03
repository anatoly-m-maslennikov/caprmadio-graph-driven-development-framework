---
subject_scopes:
  - lifecycle
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-416--identity-migration-preserves-atomic-content
    - CAPRMEDIO-GOV-REQU-417--semantic-immutability-boundary
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Preserve semantic atoms through lossless recoding

An Atomic Artifact is one independently identified claim with immutable
committed revisions. Its primary claim or proof intent determines identity.
Rationale, accepted provenance facts, creation-session provenance, scope and
applicability, priority, relation meanings and endpoints, and applicable
evaluation conditions remain governed semantic content.

A governed whole-graph migration may recode an artifact's identifier,
classification-label spelling, filename, path, heading label, carrier
encoding, seal, and stored target spelling only when it preserves the protected
meaning and connected identities. Archive relocation and lossless recoding are
`carrier_only` changes. They create committed repository revisions while
preserving semantic equivalence and existing exact-revision dependencies.

Any change to governed semantic content must be classified as a refinement,
semantic revision, or replacement. Refinement and semantic revision may keep
the artifact ID under their identity gates; replacement, resolution, or
recurrence creates another artifact when the primary claim identity requires
it.
