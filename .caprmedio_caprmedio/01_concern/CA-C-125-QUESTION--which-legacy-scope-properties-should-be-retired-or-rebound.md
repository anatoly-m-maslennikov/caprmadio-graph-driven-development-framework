---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Structural Entity"
    - "Scope Unit"
    - "Operator"
    - "Atom/Subjects"
priority: medium
version: 2
updated_at: "2026-09-17 17:41:11 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which legacy Scope Properties should be retired or rebound?

which legacy Atom Scope **and** Claim Scope Properties should be retired, retained, **or** rebound under the accepted structural-owner **and** Claim Scope Unit distinctions?

## Evidence

- CA-R-1014 still constructs Atom Scope from Scope Unit Scope, named Operator fallback, Atom Governed Subject, **and** content constraints; R-920 requires **=1** Scope. R-1363 now defines Atom Governed Subject as a Relation, distinct from its target.
- R-919 **and** R-1446 instead require **=1** Claim Structural Entity. R-1364 selects a set of Scope Units through a Claim Scope expression. these are different target domains, **not** spelling variants.
- R-126's definition-ownership boundary, R-1294's Demand direction, R-1465's Summary definition, **and** E-240's composite-scope fixtures still use the older terminology. a global text replacement would silently change what they constrain.
- `CAPRMEDIO-META-REQU-159@15` permits structural scope sets **to** be identical, overlapping, **or** different across owners, with explicit reuse **or** correspondence. its Claim does **not** establish whether these sets represent applicability selections, direct structural children, **or** another domain. the tree permits **=1** direct parent per Scope Unit, while applicability selections can overlap; neither interpretation can safely replace the other. preserve this Claim until its set domain is resolved.
- the Operator accepted Claim Scope Unit **and** ordinary use of scope without a separate special Scope definition. named Operator fallback remains required; it cannot simply be lost during retirement.

## Principle check

CA-M-002 rejects independent duplicate Properties; CA-M-006 requires coherent reference domains; CA-R-1490 protects explicit applicability constraints **and** external Goal ownership. the latest Operator input governs, but these Principles do **not** authorize inventing another target Property **or** silently replacing a target set with one Scope Unit.

## Disposition

defer the coordinated Property retirement/rebinding where its exact preservation mapping is uncertain. retain the source Claims **and** named fallback until their replacement responsibilities are explicit. C-118 separately records the narrower Task/Objective exception conflict, **and** C-117 records missing structural declarations. do **not** claim this family is normalized merely after fixing duplicated words.
