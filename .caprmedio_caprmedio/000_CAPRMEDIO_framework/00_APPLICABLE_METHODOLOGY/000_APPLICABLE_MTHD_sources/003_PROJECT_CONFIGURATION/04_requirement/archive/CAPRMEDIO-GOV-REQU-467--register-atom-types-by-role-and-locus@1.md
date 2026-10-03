---
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-463--base-role-locus-types-and-qa-cases
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-250--internal-atom-types-equal-content-roles
      - CAPRMEDIO-META-REQU-251--coordinate-artifacts-without-a-63-type-bijection
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
      - CAPRMEDIO-META-REQU-230--external-boundary-obligations
      - CAPRMEDIO-GOV-REQU-456--separate-route-catalog-and-project-whitelist
      - CAPRMEDIO-GOV-REQU-314--production-evaluation-checklists
---

# Requirement — Register Atom Types by Content role and Governance locus

The GOV artifact catalog registers this canonical Atom-form Type surface:

| Content role | Internal Atom Type | External Atom Type | Relational Atom Type |
|---|---|---|---|
| `concern` | `concern` | `external_problem` | `conflict` |
| `analysis` | `analysis` | `external_analysis_report` | `conflict_analysis` |
| `requirement` | `requirement` | `constraint` | `contract` |
| `method` | `method` | `implementation_methodology` | `integration_decision` |
| `evaluation` | `evaluation` | `evaluation_standard` | `review_protocol` |
| `implementation` | `implementation` | `external_git_commit` | `pull_request` |
| `observation` | `observation` | `external_evidence_record` | `verification_record` |

The seven internal names are derived by META and cannot be renamed or replaced by project policy. GOV owns the external and relational names and may revise them through governed successors without changing their Content roles or Governance loci.

Every relational Atom declares explicit endpoints appropriate to its meaning. Every external Atom identifies the outside authority, system, repository, or other origin that owns or imposes its meaning. Authority, provenance, priority, lifecycle, and `scope_path` remain separate metadata.

## Evaluation boundary

GOV admits two direct internal `evaluation` subtypes:

- `qa_case` defines one mechanism-neutral bounded check, including the claim
  checked, applicable conditions, acceptance criteria, and disposition rule;
  and
- `evaluation_control` defines one condition or invariant continuously checked
  during real production operation, including its signal, healthy boundary,
  evaluation window, ownership, and failure response.

Automated tests, evaluation prompts, rubrics implemented as executable
configuration, statistical evaluators, model judges, monitors, alerts, and
health checks are internal `implementation`, not Evaluation subtypes. Their
results are `observation`.

One QA Case may have distinct Test and Evaluation implementations, and one
implementation may cover several QA Cases when coverage remains explicit and
individually attributable. Test and Evaluation chains remain distinguishable
even when they assure the same Case.

A Production Evaluation Checklist is an Evaluation-role Catalog Projection over
applicable `evaluation_control` Atoms. The Projection organizes controls but
does not absorb or restate their claims.

Another Evaluation pattern may use the top-level `evaluation` Type only when
neither admitted subtype applies. A subtype is never a sub-subtype and never
replaces the canonical top-level Type.

## Method and Implementation boundaries

An internal `method` Atom selects how accepted Requirements will be approached or realized. An internal `implementation` Atom identifies one governed realized change or executable/configured realization. Native code and configuration remain normal project carriers and may realize an Implementation Atom without becoming control-plane documents.

A Pull Request remains a relational Implementation connecting declared source and target endpoints. Its rationale, evaluation, and observations retain their own roles and do not become Implementation merely because the Pull Request contains links or summaries.

## Primary claim

GOV registers the canonical Atom-form Type for each Content-role and
Governance-locus coordinate, derives all internal names directly from their
Content roles, and distinguishes mechanism-neutral QA Cases from continuous
production Evaluation Controls.

## Rationale

Direct role-equals-Type naming makes internal Atoms predictable, while direct
subtypes preserve operationally meaningful Evaluation distinctions. A
mechanism-neutral QA Case avoids duplicating one obligation across Test and
Evaluation implementations, while Evaluation Control keeps real production
operation distinct from bounded QA.
