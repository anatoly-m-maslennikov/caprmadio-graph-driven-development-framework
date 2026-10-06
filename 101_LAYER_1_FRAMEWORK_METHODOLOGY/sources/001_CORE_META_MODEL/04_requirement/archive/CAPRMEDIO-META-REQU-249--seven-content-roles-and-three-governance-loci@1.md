---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-238--seven-content-roles-and-three-governance-loci
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-205--authority-and-evaluation-separation
      - CAPRMEDIO-META-REQU-224--analysis-and-observation-boundary
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
      - CAPRMEDIO-META-REQU-230--external-boundary-obligations
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
---

# Requirement — Use seven Content roles and three Governance loci

CAPRMEDIO classifies the primary semantic contribution of every governed artifact through exactly seven `content_role` values:

1. `concern` identifies a matter requiring disposition, including a question, problem, risk, opportunity, or conflict.
2. `analysis` interprets concerns or observations and develops understanding without independently establishing the desired result.
3. `requirement` states what the governed subject must, may, or must not satisfy, including a desired result, obligation, boundary, invariant, or required state.
4. `method` selects or prescribes how accepted Requirements will be approached or realized.
5. `evaluation` defines how a claim, realization, or real operating condition will be checked, including mechanism-neutral QA Cases and continuous production Evaluation Controls.
6. `implementation` is a realized project change or executable/configured realization, including code, configuration, committed implementation state, and executable evaluation machinery.
7. `observation` records what was observed, including evidence, measurements, test results, evaluation results, and verification outcomes.

Governance locus is an independent semantic axis with exactly three `governance_locus` values:

- `internal` for project-owned meaning;
- `external` for meaning imposed or owned outside the project; and
- `relation` for meaning that exists between explicit endpoints.

QA Cases and Evaluation Controls have the Evaluation role. Executable Test,
Evaluation, monitoring, alerting, and health-check mechanisms have the
Implementation role. Their results, production signals, and verification
records have the Observation role. Evaluation may check authority but cannot
create, edit, or override it.

Artifact form is an independent structural axis. `scope_path` remains a structural ownership coordinate rather than a semantic role or locus.

## Primary claim

CAPRMEDIO uses Concern, Analysis, Requirement, Method, Evaluation, Implementation, and Observation as its seven Content roles and internal, external, and relation as its three Governance loci.

## Rationale

Concern covers the full family of matters needing disposition, while
Requirement names the desired-result role directly instead of the overbroad
Definition label. Separating Evaluation definitions, executable
Implementations, and resulting Observations preserves both bounded QA and
continuous production-evaluation chains.
