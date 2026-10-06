---
subject_scopes:
  - artifact-catalog
version: 1
updated_at: 2026-08-19 04:28:57
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-727--permit-an-optional-direct-subtype-without-self-subtyping
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Governance-locus Atom subtypes

GOV registers these direct subtypes for external and relational Atom loci while internal Atoms use the naked Content-role Type or a separately registered internal subtype.

| Content role | External subtype | Relational subtype |
|---|---|---|
| `concern` | `external_problem` | `conflict` |
| `analysis` | `external_analysis_report` | `conflict_analysis_report` |
| `plan` | — | — |
| `requirement` | `constraint` | `contract` |
| `method` | `external_method` | `method_binding` |
| `evaluation` | `evaluation_standard` | `review_protocol` |
| `delivery` | — | — |
| `implementation` | `external_git_commit` | `pull_request` |
| `ops` | `external_evidence_record` | `verification_record` |
