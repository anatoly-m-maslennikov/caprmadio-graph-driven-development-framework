---
atom_id: CA-P-918
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Methodology Conformance Tool
    occurrent:
      - Methodology Conformance Tool Update
  depends_on:
    occurrent:
      - CA-P-917
version: 1
updated_at: 2026-08-29 05:10:05 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Methodology Conformance Tools

**when** CA-P-917 is Done, **then** the Assignee **must** make **every** in-scope conformance Tool enforce the accepted CA-P-915 authority **before** source normalization begins.

## Scope

`((GENERATE_ENTITY_GRAPH and its tests) union (COMPILE_APPLICABLE_METHODOLOGY and its tests) union (every current conformance Tool directly identified by CA-P-917 as enforcing an authority changed by CA-P-905 through CA-P-916))`

## Definition of Done

the Task is **not done if** (a Tool is restricted **to** one hard-coded Methodology folder **or** the Entity Graph omits declared Terms, complete DEPENDS_ON parent trees, **all** DEPENDS_ON Subjects, SUBTYPE_OF, IS_BORNE_BY, IS_ALLOWED_VALUE_OF, Root Terms, cycles, direct-parent cardinality violations, **or** role-specific Type-Term violations **or** the compiler omits duplicate governed-Term Definitions from its deterministic conflict set **or** a Tool treats **all** Subjects as Terms **or** a Tool collapses taxonomy, bearer dependence, allowed-value membership, Claim-Subject relations, **or** graph-specific relations **or** an unresolved conflict can produce output **or** Tool behavior lacks deterministic tests **or** **any** test writes authoritative source Carriers).

## Details

derive checks from accepted authority **and** keep Entity Graph generation read-only by default. preserve the rule that Terms are Subjects but **not** **all** Subjects are Terms. require conflict detection **to** report exact candidate Carrier paths, source-frontier digest, **and** a stable conflict identity **without** choosing source authority.
