---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - lifecycle
version: 9
updated_at: 2026-08-29 01:16:37 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-397--artifact-creation-setting
  relates_to:
    - CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-authority-configuration-and-the-scope-unit-graph
  child_of:
    - CA-R-1054
---
# Gate atomic admission and promotion

The Project Configuration Atom selects `medium` **or** `high` through `artifacts.creation_strictness`; the default is `medium`.

At medium strictness, CAPRMEDIO requires accepted authority, one primary claim, one enabled artifact type, owning scope, creation provenance, material relations, priority, **and** sufficient precision to establish a stable artifact identity **and** initial committed revision. Optional non-authoritative context **may** remain explicitly unknown.

At high strictness, CAPRMEDIO stops **before** emission while **any** material authority, meaning, boundary, classification, scope, lineage, conflict, **or** evaluation question remains ambiguous. It asks focused questions **until** the atom meets the same one-primary-claim identity standard.

the two levels assess one-step promotion eligibility. Promotion is proposed **only** **when** the claim applies unchanged at the broader enabled scope **and** always requires explicit operator acceptance.

Admission does **not** prohibit later same-ID revisions. **every** later change passes the atomic change-class gate; changing the primary claim identity requires a replacement.
