---
subject_scope: scope-topology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-201--canonical-layer-definitions
      - CAPRMEDIO-META-REQU-233--seven-role-artifact-model-and-qa-layer
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-202--layer-handoff-contracts
      - CAPRMEDIO-META-REQU-203--acyclic-layer-dependencies
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-META-REQU-231--forward-only-change-propagation
      - CAPRMEDIO-META-REQU-232--total-one-to-one-route-catalog
---

# Requirement — Use seven content roles and seven ordered layers

CAPRMEDIO classifies artifact meaning through seven Content roles:

1. Problem;
2. Analysis;
3. Definition;
4. Method;
5. Evaluation;
6. Implementation; and
7. Observation.

Governance locus remains an independent axis with exactly three values:
`internal`, `external`, and `relation`. Revision mode remains an independent
axis with exactly three values: `atomic`, `append_only`, and `maintained`.
`scope_path` remains structural and is not a semantic axis.

The canonical role-and-locus naming model is:

| Content role | Internal | External | Relation |
|---|---|---|---|
| Problem | Problem | External Problem | Conflict |
| Analysis | Analysis Report | External Analysis Report | Conflict Analysis |
| Definition | Requirement | Constraint | Contract |
| Method | Technical Decision | Implementation Methodology | Integration Decision |
| Evaluation | QA Case | Evaluation Standard | Review Protocol |
| Implementation | Git Commit | External Git Commit | Pull Request |
| Observation | Evidence Record | External Evidence Record | Verification Record |

Every concrete artifact classification resolves through its full
Revision-mode, Content-role, and Governance-locus route. Authority,
provenance, priority, lifecycle, and `scope_path` remain separate metadata.

## Canonical layer order

CAPRMEDIO uses seven ordered layers:

```text
META → GOV → TOOLS → SKILLS → QA → IMPL → OPS
```

| Layer | Canonical responsibility |
|---|---|
| META | Meanings, routing axes, universal invariants, layer topology, and inter-layer semantics |
| GOV | Governed carriers, identity, settings, provenance, lifecycle, applicability, scope, and conflict governance |
| TOOLS | Reusable executable CAPRMEDIO mechanisms, validation, resolution, diagnostics, generation, and repository mechanics |
| SKILLS | Thin provider-neutral orchestration, entry gates, workflow chaining, and session continuity |
| QA | Evaluation definitions, QA Cases, maintained Test and Eval planning surfaces, evaluation standards, review protocols, criteria, rubrics, and acceptance gates |
| IMPL | Development environments, implementation profiles, project code, executable Test and Eval implementations, adapters, migrations, and local execution evidence |
| OPS | Post-implementation delivery, release, publication, runtime supportability, investigation, containment, recovery, and hosted evidence |

The plural canonical names are **TOOLS** and **SKILLS**. Singular `TOOL` and
`SKILL` are retired as layer names, though ordinary prose may still describe
one tool or one skill.

## TOOLS–QA boundary

TOOLS owns reusable mechanisms and does not own project evaluation claims. QA
uses those mechanisms to define how accepted Definitions will be checked.
Generic validators, runners, resolvers, and reporting engines belong to TOOLS;
Test Cases, Eval Cases, plans, rubrics, criteria, and acceptance gates belong
to QA.

QA follows SKILLS and precedes IMPL. QA definitions may therefore govern
implementation entry gates without creating a backward dependency. IMPL owns
the executable code that realizes both the project behavior and its QA
implementations. Resulting evidence is recorded in the applicable downstream
IMPL or OPS scope and refers back to the governing QA definition.

QA does not establish product behavior. Requirements and Contracts remain the
authority for desired results; QA operationalizes their assessment. A failed
or inconclusive check produces new Problem or Analysis input for a later
cycle.

## Layer authority

Each responsibility has one canonical owner. A layer may depend on earlier
layers and may affect later layers, preferably its immediate successor. It
cannot redefine an earlier layer's responsibility. Horizontal, bidirectional,
or cyclic collaboration belongs in feature contracts rather than layer
authority.

## Rationale

Plural TOOLS and SKILLS name collections rather than individual artifacts.
Separating QA from TOOLS prevents reusable mechanisms from owning the claims
they execute. Placing QA before IMPL makes Test and Eval definitions explicit
implementation entry inputs while keeping executable code and observations in
downstream layers.
