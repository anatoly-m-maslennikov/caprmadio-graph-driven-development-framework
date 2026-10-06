---
atom_id: CA-E-444
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Term/meaning validation"
  depends_on:
    - "Term"
    - "Project"
    - "Definition Atom"
    - "Atom/Claim"
    - "Atom"
    - "Subject"
    - "Entity"
    - "Subject Path"
    - "Terminology Projection"
    - "Concern"
    - "Action"
    - "Process"
    - "General Term"
    - "Artifact/Revision"
    - "Scope Unit"
    - "Actor"
    - "Projection"
    - "Relation"
    - "Relation Kind"
version: 3
updated_at: "2026-09-13 03:40:22 +0400"
relations:
  evaluation_for:
    - CA-R-1318
    - CA-R-1319
    - CA-R-1320
    - CA-R-1455
    - CA-R-1275
    - CA-R-1279
    - CA-R-1321
    - CA-R-1194
    - CA-R-1325
    - CA-M-114
    - CA-M-125
---
# Validate Project-specific Term meaning

## Claim checked

a Term has a Project-specific meaning that remains consistent across **all** its uses, distinct from an Atom's direct Subject reference; vocabulary diagnostic indexes preserve source evidence **and** uncertainty under CA-R-1455.

## Test case

create an active Definition Atom that gives a word **or** phrase a Project-specific meaning, **and** use that meaning consistently **in** several Claims. create an ordinary English word used consistently **without** a Project-specific definition. create a definition that merely repeats ordinary dictionary meaning, a Term used with conflicting Project-specific meanings, a Term's wording substituted for a direct Subject reference, **and** a complete composite Subject Path classified as a Term.

add a source occurrence with evidence of Project-specific use but no active defining authority **in** the declared applicable source authority boundary with complete checked definition coverage; two incompatible active definitions; duplicate active defining authority; **and** a case whose context **or** source coverage cannot settle classification. include sentence-initial ordinary vocabulary, Scope Unit **and** Actor names, identifiers, paths, **and** syntax tokens with no evidence of Project-specific vocabulary meaning. include a definition excluded by a filtered selection, source occurrences of the same spelling with different evidenced contexts, an entry lacking an exact occurrence **or** Revision, **and** invented edges between indexed entries.

## Acceptance criteria

the consistently used Project-specific Term passes **and** resolves **to** its active Definition Atom. the ordinary word remains valid general language **without** being classified as a Term. consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** establish a Term. a dictionary-only definition does **not** qualify for the Terminology Projection. conflicting meanings fail with the defining Atom **and** conflicting uses identified. a direct GOVERNS **or** DEPENDS_ON reference connects an Atom **to** its canonical Entity, Action, **or** Process target; substituting the Term's wording for a direct Subject reference **or** classifying a complete composite Subject Path as a Term fails. terminology entries retain their source references **without** independent authority.

the diagnostic index distinguishes supported ordinary English use, missing defining authority, conflicting defining authority **or** uses, **and** explicitly uncertain cases. **every** judgment retains the exact occurrence, surrounding Claim **or** reference context, Artifact Revision, source selection, **and** checked definition coverage. ordinary vocabulary requires no Project-specific definition; a source occurrence's capitalization does **not** become evidence of missing authority. names, identifiers, paths, **and** syntax tokens do **not** become unresolved Project-specific candidates **without** contextual evidence of that use. a missing-authority judgment requires complete checked definition coverage for its declared applicable source authority boundary; absence from incomplete **or** filtered coverage alone cannot establish that judgment. duplicate active defining authority fails uniqueness even **when** the definitions agree; the diagnostic identifies an authority conflict **without** inventing a meaning conflict. an evidence-backed candidate remains diagnostic **without** a fabricated definition; a case whose evidence is insufficient remains reviewable as uncertain **without** an established Term classification. spelling alone does **not** transfer classification across source contexts. missing occurrence **or** revision traceability, hidden uncertainty, unsupported semantic certainty, **or** invented graph edges fail. a source-backed uncertain result passes the diagnostic-index check while the underlying meaning **or** authority remains unresolved.

## Failure disposition

record a Concern identifying the affected wording, defining Atom, conflicting use, direct Subject reference, **or** Terminology Projection entry, together with its exact source occurrence **and** Revision. distinguish a failed index check from a faithfully reported unresolved source case; do **not** fabricate authority **to** make either pass.
