---
atom_id: CAPRMEDIO-META-REQU-174
cce_version: cce_1
cce_form: separation
subjects:
  governs:
    continuant:
      - extension-model
  depends_on:
    continuant:
      - Framework Instance Settings
version: 10
updated_at: "2026-09-10 20:57:22 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-127-CORE_META_MODEL-CORE-REQUIREMENT--define-two-governance-origins
    - CAPRMEDIO-META-REQU-160-CORE_META_MODEL-CORE-REQUIREMENT--govern-extension-semantics
---
# Separate Extension ownership from application bindings

an Extension is an owned capability package whose Governance origin is internal **or** external relative **to** the current project. an Extension application is a separate binding Atom whose typed relations identify the applied Extension **and** target Scope Units.

the application binding does **not** own **or** duplicate current Extension activation **or** selected Extension revision decisions; those decisions remain owned by the Framework Instance Settings Artifact under CA-R-1207 **and** CAPRMEDIO-META-REQU-163.
