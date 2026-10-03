---
subject_scopes:
  - artifact-catalog
project_graph_state:
  artifacts:
    enabled_types:
      - concern:external_problem
      - concern:conflict
      - analysis:external_analysis_report
      - analysis:conflict_analysis_report
      - requirement:constraint
      - requirement:define_scope_for
      - requirement:demand_for
      - method:external_implementation_method
      - method:method_binding
      - evaluation:external_evaluation_standard
      - evaluation:review_protocol
      - implementation:external_git_commit
      - implementation:pull_request
      - ops:external_evidence_record
      - ops:verification_record
version: 7
updated_at: 2026-08-22 06:00:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-100--preserve-external-and-relational-boundary-obligations
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register non-default Atom Types

GOVERNANCE registers the following non-default Atom Types within their owning
Content roles. External Types derive external Governance origin. Additional
internal Types derive internal Governance origin and may use ordinary typed
frontmatter relations.

| Content role | External Type | Additional internal Type |
|---|---|---|
| `concern` | `external_problem` | `conflict` |
| `analysis` | `external_analysis_report` | `conflict_analysis_report` |
| `plan` | — | — |
| `requirement` | `constraint` | `define_scope_for`, `demand_for` |
| `method` | `external_implementation_method` | `method_binding` |
| `evaluation` | `external_evaluation_standard` | `review_protocol` |
| `delivery` | — | — |
| `implementation` | `external_git_commit` | `pull_request` |
| `ops` | `external_evidence_record` | `verification_record` |

The Requirement Types `define_scope_for` and `demand_for` are the only
Relational Atom Types. Their filename Type tokens are `DEFINE_SCOPE_FOR` and
`DEMAND_FOR`. Each filename contains its one Claim Scope token immediately
after its Type token. Neither Type targets another Atom or Content-role slice.
