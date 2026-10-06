---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - lifecycle
version: 12
updated_at: 2026-09-04 04:05:44 +0400
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

the Framework Instance Settings Artifact selects `medium` **or** `high` through `artifacts.creation_strictness`; the default is `medium`.

**at** medium strictness, CAPRMEDIO requires accepted authority, one primary Claim, one enabled Artifact Type, owning Scope, creation provenance, material relations, priority, **and** sufficient precision to establish a stable Artifact identity **and** initial committed Revision. optional non-authoritative context **may** remain explicitly unknown.

**at** high strictness, CAPRMEDIO stops **before** emission while **any** material authority, definition, boundary, classification, Scope, lineage, Conflict, **or** Evaluation question remains ambiguous. it asks focused questions **until** the Atom meets the same one-primary-Claim identity standard.

the two levels assess one-step promotion eligibility. promotion is proposed **only** **when** the Claim applies unchanged at the broader enabled Scope **and** always requires explicit Operator acceptance.

admission does **not** prohibit later same-ID Revisions. **every** later change passes the atomic change-class gate; changing the primary Claim identity requires a replacement.
