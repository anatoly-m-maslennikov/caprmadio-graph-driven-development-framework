---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - lifecycle-traceability
tier: core
version: 10
updated_at: 2026-09-05 00:51:50 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-007--full-minimal-traceability
    - CA-E-002
---
# Bind traceability to exact claims and revisions

**every** CAPRMEDIO traceability assertion identifies the exact governed claim revision on which a receiving artifact, implementation target, evaluation use, delivery action, operational observation, **or** other governed result relies.

The trace preserves the source identity **and** committed revision, the receiving identity **or** stable target locator, the typed relation between them, the bounded scope **and** use, **and** the provenance needed to replay that relation. A relation to an artifact ID **without** its relied-upon revision is insufficient **after** the Atom has more than one committed revision.

Traceability records relationships; it does **not** transfer authority **or** prove correctness, execution, delivery, **or** currentness. Git **may** preserve carrier history, while governed Journals preserve semantic relationships that **must** survive Git graph transformations.
