---
atom_id: CAPRMEDIO-GOV-REQU-302
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - lifecycle
version: 14
updated_at: 2026-09-07 09:59:57 +0000
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-GOV-REQU-294-CORE_META_MODEL-REQUIREMENT--configure-interaction-reporting-mode
    - CAPRMEDIO-GOV-REQU-385-CORE_META_MODEL-REQUIREMENT--resolve-artifact-classification-from-authority-and-configuration
  child_of:
    - CA-R-1054
---
# Gate atomic admission and promotion

the Framework Instance Settings Artifact selects `medium` **or** `high` through `artifacts.creation_strictness`; the default is `medium`.

**at** medium strictness, CAPRMEDIO requires accepted authority, one primary Claim, one enabled Artifact Type, owning Scope, creation provenance, material relations, priority, **and** sufficient precision to establish a stable Artifact identity **and** initial committed Revision. optional non-authoritative context **may** remain explicitly unknown.

**at** high strictness, CAPRMEDIO stops **before** emission while **any** material authority, definition, boundary, classification, Scope, lineage, Conflict, **or** Evaluation question remains ambiguous. it asks focused questions **until** the Atom meets the same one-primary-Claim identity standard.

the two levels assess one-step promotion eligibility. promotion is proposed **only** **when** the Claim applies unchanged at the broader enabled Scope **and** always requires explicit Operator acceptance.

admission does **not** prohibit later same-ID Revisions. **every** later change passes the atomic change-class gate; changing the primary Claim identity requires a replacement.
