---
atom_id: CA-P-935
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Project Scope Unit Graph Generator
    occurrent:
      - Project Scope Unit Graph Generator Authority Coverage Completion
  depends_on:
    occurrent:
      - CA-P-934
version: 2
updated_at: 2026-08-31 21:55:15 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Complete Project Scope Unit Graph Generator Authority Coverage

**when** CA-P-934 is Done, **then** the Assignee **must** make the canonical generator emit every required Scope Unit row value and exact source binding from current active authority.

## Scope

`((GENERATE_PROJECT_GRAPH_STATE Tool source and tests) union (current Project Scope Unit Directory Carriers and receipts) union (their active Delivery Atoms) union (Project Scope Unit Graph generation metadata authority))`

## Definition of Done

the Task is **not done if** (**any** current Scope Unit row omits Unit Name, Project Boundary Position, Type value, Child Composition, Structural Level, applicable Local Order, effective Unit Type Name, effective Navigational Order Number, parent, authority path, **or** Delivery path **or** **any** emitted value lacks an exact applicable source Artifact revision, digest, and Work Journal record **or** **either** Projection lacks generator identity and digest **or** source and installed execution serialize different canonical generator identity **or** identical source frontiers produce different bytes **or** tests fail).

## Details

derive Type value from Local Order participation, keep Unit Type Name as the independent Operator navigation label, derive Child Composition from direct typed children, and read Delivery path from the owning active Delivery Atom. serialize canonical source-generator identity separately from executed installed-generator identity.

## Completion Evidence

two byte-identical dry-runs discovered 13 current Scope Units and no admitted contributions. the in-memory graph serializes Unit Name, Project Boundary Position, Type value, Child Composition, Structural Level, applicable Local Order, Unit Type Name, Navigational Order Number, parent, authority path, and Delivery path for every row.

the generated source map creates 250 exact bindings. each Scope Unit Directory Carrier binding uses its exact current revision, digest, and Work Journal receipt; each Delivery path binding uses its owning active Delivery Atom revision and digest plus the exact Directory Carrier Work Journal receipt that includes that Atom entry. both Projections serialize the canonical source-generator Carrier `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py` and its digest independently from the execution Carrier and digest. the execution-independent canonical Projection bytes are identical for source and installed execution carriers. all eight focused tests pass. the non-authoritative execution evidence is stored in `execution_evidence/CA-P-935-project-scope-unit-graph-generator-authority-coverage.projection.json`.
