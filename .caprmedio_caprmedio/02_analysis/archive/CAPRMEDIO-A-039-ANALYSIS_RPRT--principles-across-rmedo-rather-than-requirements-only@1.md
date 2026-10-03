---
subject_scopes:
  - applicability
  - content-roles
version: 1
updated_at: 2026-08-20 03:59:09
---
# Analyze Principles across RMEDO rather than Requirements only

## Starting assumption and correction

The initial Principle review treated every Project Principle as a Requirement because every current candidate had a `REQU` identity and `tier: principle`. That was an inference from the current realization, not an accepted semantic rule.

The correction is that Content role and applicability tier are independent axes:

- Content role states an Atom's primary semantic contribution.
- Applicability tier states how broadly that contribution applies within its governed scope.
- Relations state lineage and other direct dependencies.
- Operator acceptance is the only source of project authority; neither tier nor graph position creates authority.

Therefore `principle` does not mean `Requirement`. Requirement, Method, Evaluation, Delivery, and governing Ops Atoms may each exist at Principle, Core, or Standard tier when that tier is meaningful for their role.

## CAPRMEDIO lifecycle boundary

The complete framework is not one undifferentiated specification:

```text
CAP -> RMED -> (I)
 ^              |
 +------ O -----+
```

- CAP is pre-specification work: Concerns identify matters, Analysis preserves reusable reasoning, and Plans authorize and coordinate change.
- RMED is the layered, distributed specification.
- Implementation is a projection or realization of the specification.
- Ops is the loop that operates, observes, preserves evidence, and returns material outcomes to CAP.

CAP being before the specification does not prevent its Atoms from having applicability tiers, but CAP tiers do not make CAP part of the specification. The present analysis focuses on distributing Principles across RMEDO rather than keeping them Requirement-only.

## Implementation boundary

Implementation has no independent semantic tier. It can realize source Atoms from every specification Content role and every applicability tier, so assigning it one local tier would either discard source coverage or redundantly copy all source classifications.

An Implementation carrier should instead record direct realization lineage. Its effective Content-role and tier coverage is derived from the connected specification frontier. A material meaning introduced only in Implementation is ungoverned until the operator admits it through an appropriate specification Atom.

## Ops boundary

Ops is the loop, not merely a terminal evidence store. It may contain governing Atoms for continuous improvement, Extension evolution, Configuration changes, migrations, monitoring, feedback intake, and operational response. Those governing Ops Atoms may have Principle, Core, and Standard tiers.

Operational events and evidence records are different: recording a project-wide occurrence does not automatically make the record a Principle. Their scope is normally derived from the governed operation and its evidence bindings.

## Candidate Principle distribution

The existing identities below are trace labels for the candidates, not a decision to retain Requirement identities after reclassification.

### R - system and authority invariants

- `REQU-004` - The graph is the operating model
- `REQU-005` - Necessary complexity only
- `REQU-013` - Preserve discipline-independent semantics
- `REQU-042` - Operator acceptance establishes project authority
- `REQU-044` - Organize authority as a hierarchical graph

These candidates state what must remain true across CAPRMEDIO.

### M - ways of governing and structuring work

- `REQU-002` - Apply MECE to canonical decompositions
- `REQU-003` - Apply DRY across CAPRMEDIO
- `REQU-034` - Scale through structure

These candidates define how governed meaning is organized and maintained. Their Atom bodies should expand well-adopted abbreviations on first use and explain their exact CAPRMEDIO meaning while retaining abbreviations such as MECE and DRY in their summaries.

### E - evaluation and reliance

- `REQU-022` - Make accepted Requirements checkable
- `REQU-023` - Require explicit reliance boundaries

These candidates define how governed claims are checked and when conclusions may be relied upon. Checkability is independent of lineage completeness: an operator may create Standard Requirements before their Core or Principle parents, while a linked Evaluation can later supply the applicable check.

### D - delivery-independent realization

- `REQU-012` - Keep realizations replaceable across technical substrates

This candidate must be rewritten as a Delivery Principle so that it governs portable realization and Delivery without granting Implementation independent semantic authority.

### O - operation of the loop

- `REQU-009` - Govern capability evolution through Extensions
- `REQU-010` - Govern capability selection through Configuration
- `REQU-046` - Improve from observed outcomes

These candidates govern how Ops closes and repeats the loop by observing outcomes, evolving available capabilities, configuring their use, and returning necessary change into CAP.

## Proposed lineage model

Each RMEDO Content role owns its own applicability lineage:

```text
R Principle -> R Core -> R Standard
M Principle -> M Core -> M Standard
E Principle -> E Core -> E Standard
D Principle -> D Core -> D Standard
O Principle -> O Core -> O Standard
```

Cross-role dependencies should use explicit typed relations rather than overloading same-role lineage. Examples include a Requirement performed through a Method, evaluated through Evaluation, and delivered through Delivery, while Ops observes the realized result and feeds evidence back into CAP.

All Principles at the same applicability tier have equal tier authority. Presentation order belongs to a Projection and must not be stored as Principle authority or precedence.

## Consequences and unresolved implementation work

If this candidate model is accepted:

1. The metamodel must define applicability tier independently of Content role and admit Principle, Core, and Standard tiers across RMEDO.
2. Existing Requirement-only Principle candidates must be classified by primary semantic contribution and replaced through governed role-specific identities where their role changes.
3. Same-role tier lineage and cross-role semantic relations must have separate, explicit relation rules.
4. Ops must distinguish governing loop Atoms from operational event and evidence Atoms.
5. Validators and Projections must derive role-by-tier views without treating tier as the source of authority.
6. Implementation coverage must be derived from realization lineage rather than copied into independent tier metadata.

This Analysis records the candidate architecture and its reasoning. It does not itself change the metamodel, reclassify any Principle Atom, or authorize a migration.
