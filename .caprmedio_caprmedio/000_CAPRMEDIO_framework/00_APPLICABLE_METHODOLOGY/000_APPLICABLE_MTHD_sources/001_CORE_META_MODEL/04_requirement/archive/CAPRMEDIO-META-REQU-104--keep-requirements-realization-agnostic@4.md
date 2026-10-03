---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - semantics
version: 4
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-091--normative-atoms-are-the-caprmedio-specification
    - CAPRMEDIO-META-REQU-106--keep-meta-and-gov-implementation-neutral
---
# Requirement — Keep Requirements realization-agnostic

Every Requirement states an outcome, obligation, or externally observable boundary that the governed product or project MUST, MAY, or MUST NOT satisfy without prescribing its internal code or code organization.

A normative choice about programming languages, libraries, algorithms, functions, classes, modules, source-file structure, or another construction technique is Method. A normative choice about packaging, release, deployment, distribution, installation, migration, upgrade, or rollback is Delivery. The concrete code, configuration, schema realization, executable automation, or other operative asset is Implementation.

A Requirement MAY preserve an accepted external interface, protocol, data shape, or host obligation when conformance to that boundary is itself required. It does not thereby prescribe the project's internal realization. A candidate that combines an independently replaceable outcome with a code-facing Method or Delivery rule MUST be split before admission.

## Primary claim

Requirements are realization-agnostic; code-facing construction rules belong to Method, delivery-path rules belong to Delivery, and operative code and configuration belong to Implementation.
