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
      - CAPRMEDIO-META-REQU-234--seven-role-and-seven-layer-model
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-202--layer-handoff-contracts
      - CAPRMEDIO-META-REQU-203--acyclic-layer-dependencies
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
      - CAPRMEDIO-META-REQU-225--distinct-test-and-evaluation-chains
      - CAPRMEDIO-META-REQU-227--scope-path-is-structural
      - CAPRMEDIO-META-REQU-231--forward-only-change-propagation
      - CAPRMEDIO-META-REQU-232--total-one-to-one-route-catalog
---

# Requirement — Use scoped SPEC, PROFILES, and IMPL layers

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

CAPRMEDIO uses six ordered layers:

```text
META → GOV → SPEC → PROFILES → IMPL → OPS
```

| Layer | Canonical responsibility |
|---|---|
| META | Meanings, routing axes, universal invariants, layer topology, and inter-layer semantics |
| GOV | Governed carriers, identity, settings, provenance, lifecycle, applicability, canonical scope registration, and conflict governance |
| SPEC | Current project behavior, obligations, technical and integration choices, evaluation definitions, and cross-scope contracts |
| PROFILES | Selectable implementation profiles, environments, dependency policies, authoring practices, portability and security rules, and profile-specific gates |
| IMPL | Concrete source, skill packages, Test and Eval implementations, configuration, schemas, migrations, adapters, commits, pull requests, and implementation traceability |
| OPS | Post-implementation delivery, release, publication, runtime supportability, investigation, containment, recovery, and hosted evidence |

## Scope propagation

GOV registers each project scope once. SPEC, PROFILES, and IMPL reuse the same
scope IDs without independently redefining them.

For the CAPRMEDIO project, the initial canonical scopes are:

- `tools`;
- `skills`; and
- `qa`.

Each scope forms an aligned chain:

```text
SPEC/<scope> → PROFILES/<scope> → IMPL/<scope>
```

The layers answer different questions:

| Layer | Question |
|---|---|
| SPEC | What must this scope do, prevent, expose, and satisfy? |
| PROFILES | Which selectable implementation rules apply to this scope? |
| IMPL | Which concrete artifacts realize this scope? |

The aligned scopes are not duplicate truth. A downstream layer refers to the
upstream scope identity and owns only its distinct responsibility.

Project-level surfaces in each layer own cross-scope concerns:

- SPEC project truth owns global requirements, cross-scope Contracts,
  Integration Decisions, and end-to-end QA Cases;
- PROFILES project truth owns shared profile selections and rules that apply to
  multiple scopes; and
- IMPL project truth owns shared implementation, repository configuration,
  build integration, and cross-scope traceability.

## CAPRMEDIO scope boundaries

The `tools` scope specifies CAPRMEDIO toolchain capabilities, selects profiles such
as Local Python Tools, and maps to concrete CLI, resolver, validator, and
generator implementations.

The `skills` scope specifies provider-neutral agent behavior, selects the Agent
Skills profile, and maps to concrete skill packages and scripts.

The `qa` scope specifies the shared evaluation system, selects QA Automation and
LLM Evaluation profiles, and maps to common Test/Eval runners, fixtures,
graders, and reconciliation implementations.

QA artifacts retain the scope of the subject they check. A Test Case for Tools
belongs to the `tools` scope, and a Test Case for Skills belongs to the
`skills` scope. The `qa` scope owns only shared evaluation capabilities,
standards, protocols, and infrastructure.

## PROFILES boundary

PROFILES owns only rules that participate in a selectable implementation
profile. A rule that is not part of a selectable profile does not belong in
PROFILES.

Local Python Tools is a profile selected for implementations of the `tools`
scope. Agent Skills is a profile selected for implementations of the `skills`
scope. QA Automation and LLM Evaluation profiles are selected for applicable
implementations of the `qa` scope.

PROFILES never owns concrete source or project behavior. SPEC remains authority
for required results; IMPL remains authority for what currently exists in the
repository.

## Layer authority

Each responsibility has one canonical owner. A layer may depend on earlier
layers and may affect later layers, preferably its immediate successor. It
cannot redefine an earlier layer's responsibility. Horizontal, bidirectional,
or cyclic collaboration belongs in scope Contracts rather than layer
authority.

## Rationale

TOOLS, SKILLS, and QA are scopes of the CAPRMEDIO project rather than universal
methodology layers. SPEC makes their required behavior explicit, PROFILES
selects how each will be developed, and IMPL records the resulting concrete
realization. The narrow PROFILES name prevents development policy and concrete
implementation from sharing one owner.
