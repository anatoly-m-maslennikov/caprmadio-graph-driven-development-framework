---
cce_version: cce_1
cce_form: cardinality
subjects:
  declared:
    continuant:
      - semantics
tier: core
version: 8
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
---
# Nine content roles with plan

CAPRMEDIO classifies the primary semantic contribution of governed artifacts through exactly nine `content_role` values:

1. `concern` identifies a matter requiring disposition.
2. `analysis` develops understanding without independently committing work or establishing the desired result.
3. `plan` governs who MAY perform or authorize actions through tier-classified Action Policies, states one intended action through a Task Atom, or relates one Epic Atom to its contained Task Atoms without realizing those actions.
4. `requirement` states an outcome that the governed product or project MUST, MAY, or MUST NOT provide.
5. `method` specifies how an accepted Requirement will be realized or how an existing realization will be transformed.
6. `evaluation` specifies how the project can establish that governed claims and their realization work as intended.
7. `delivery` specifies how a realized deliverable reaches its users and target environments.
8. `implementation` is the concrete native project realization of accepted Requirements, Methods, Evaluation mechanisms, and Delivery mechanisms.
9. `ops` captures enacted execution and factual results after an Implementation is run or used.
