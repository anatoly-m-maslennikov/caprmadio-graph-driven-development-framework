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
      - CAPRMEDIO-META-REQU-249--seven-content-roles-and-three-governance-loci
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-092--authority-evaluation-and-ops-remain-distinct
      - CAPRMEDIO-META-REQU-093--analysis-and-ops-fact-boundary
      - CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms
      - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
      - CAPRMEDIO-META-REQU-100--preserve-external-and-relational-boundary-obligations
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
---

# Requirement — Use eight Content roles with Delivery and Ops

CAPRMEDIO classifies the primary semantic contribution of every governed artifact through exactly eight `content_role` values:

1. `concern` identifies a matter requiring disposition, including a question, problem, risk, opportunity, or conflict.
2. `analysis` interprets concerns or operational facts and develops understanding without independently establishing the desired result.
3. `requirement` states the outcome that the governed product or project must, may, or must not provide.
4. `method` specifies how an accepted Requirement will be realized, or how an existing governed realization will be transformed while preserving its declared obligations, in code or another governed construction medium.
5. `evaluation` specifies how the project can establish that a Requirement, Method, Delivery path, or Implementation works as intended.
6. `delivery` specifies how a realized package, application, or other deliverable reaches its end users, including target-environment topology, environment-specific runtime-configuration sourcing, packaging, release, deployment, distribution, installation, migration, upgrade, and rollback.
7. `implementation` is the concrete project realization of accepted Requirements, Methods, Evaluation mechanisms, and Delivery mechanisms, including code, configuration, configuration-source adapters, executable tests and evaluations, packages, installers, and delivery automation.
8. `ops` captures enacted execution and factual results after an Implementation is run or used, including test and evaluation results, delivery outcomes, runtime evidence, logs, measurements, incidents, and verification outcomes.

Governance locus remains an independent semantic axis with exactly three `governance_locus` values:

- `internal` for project-owned meaning;
- `external` for meaning imposed or owned outside the project; and
- `relation` for meaning that exists between explicit endpoints.

Delivery is distinct from Method: Method governs construction or governed transformation of the product, while Delivery governs the target environments and the path from a realized product to availability for its end users. This includes selecting the source from which each environment obtains its runtime configuration. Delivery authority flows forward into Implementation, which realizes that selection without silently redefining it. Implementation may realize accepted claims from Requirement, Method, Evaluation, and Delivery.

The Ops Content role is independent of an Ops structural layer or scope. An Ops scope may contain artifacts of any Content role; an artifact has the Ops Content role only when its primary contribution is enacted operation or a factual result.

Artifact form is an independent structural axis. `scope_path` remains a structural ownership coordinate rather than a semantic role or locus.

## Primary claim

CAPRMEDIO uses Concern, Analysis, Requirement, Method, Evaluation, Delivery, Implementation, and Ops as its eight Content roles, with Delivery governing the path to end users and Ops governing enacted operation and factual results.

## Rationale

Construction or transformation, evaluation, and delivery answer different questions: how to build or structurally change the product, how to establish that it works, and how to make it available to users in its target environments. Environment-specific configuration-source selection belongs to Delivery because it governs the path into an enacted environment; readers, adapters, containers, and other concrete mechanisms belong to Implementation. A behavior-preserving transformation remains Method because it changes the realization path without inventing a new required outcome. Implementation materially realizes those prescriptions, while Ops captures what actually happens when the resulting mechanisms run.
