---
subject_scopes:
  - lifecycle-traceability
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-085--separate-active-authority-from-preserved-history
    - CAPRMEDIO-META-REQU-130--define-atom-admission-and-lifecycle
---
# Restrict current RMED dependencies to active RMED Atoms

Every current semantic dependency owned by an active Requirement, Method,
Evaluation, or Delivery Atom must target either an active RMED Atom or a
Concern, Analysis, Plan, Implementation, or Ops Atom. CAP/IO targets remain
eligible until their role-specific lifecycle establishes a narrower rule.

Historical lineage relations, including `replacement_of`, are not current
semantic dependencies and may target archived RMED Atoms.
