---
atom_id: CA-P-920
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Local Configuration Atom Frontier
    occurrent:
      - Local Configuration Atom Normalization
  depends_on:
    occurrent:
      - CA-P-919
version: 1
updated_at: 2026-08-29 05:10:05 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Normalize Local Configuration Atoms

**when** CA-P-919 is Done, **then** the Assignee **must** make **every** active Local Configuration Atom **in** Task Scope comply with the normalized Core Meta-Model **and** the complete current authority accepted through CA-P-915.

## Scope

`((all CA-P-917 frontier entries whose owning Scope Unit is LOCAL_CONFIGURATION) union (every replacement or new Local Configuration Atom required solely to resolve a recorded noncompliance))`

## Definition of Done

the Task is **not done if** (**any** in-scope Atom violates a normalized Core invariant **or** **any** Claim, Claim Scope, Claim-Subject relation, Subject Expression, qualified Type **or** Status domain, Term use, CCE form, Summary, filename, frontmatter, H1, revision, **or** archive relation violates current authority **or** Local Configuration redefines a Core Term **or** primitive relation **or** a project choice is promoted into Core authority **or** an active Local Configuration Definition conflict, Term-system violation, **or** invalid dependency cycle remains **or** Installed Extensions contributes authority **or** **any** repair introduces an unapproved model decision).

## Details

keep Local Configuration responsible for CAPRMEDIO-specific choices, activation, compatibility, replacement, priority, **and** Project-local methodology resolution. preserve **every** valid Core invariant **and** use qualified Subjects rather than creating role-specific Property Terms.
