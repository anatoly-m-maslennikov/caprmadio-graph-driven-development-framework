---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Projection/Type: Catalog"
  depends_on:
    - "Term"
    - "Project"
    - "Definition Atom"
    - "Atom/Claim"
    - "Atom"
    - "Subject"
    - "Entity"
    - "Subject Path"
    - "Projection/Type: Terms Graph"
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
version: 7
updated_at: "2026-09-14 04:00:22 +0400"
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
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Project-specific Term meaning

## Claim checked

a Catalog used as a vocabulary diagnostic index **must** keep its assessment of Project-specific Term meaning **and** direct Subject use faithful **to** the governing definitions **and** exact source context, including the required consistency across **all** source uses covered by the assessment. its diagnostic judgments preserve source evidence **and** uncertainty under CA-R-1455. the relevant built Terms Graph, **when** available, **and** original Atom Claims **or** reference contexts supply evidence for this assessment; graph topology alone does **not** establish meaning, defining authority, **or** consistency of source use.

## Test case

create an active Definition Atom that gives a word **or** phrase a Project-specific meaning, **and** use that meaning consistently **in** several Claims. create an ordinary English word used consistently **without** a Project-specific definition. create a definition that merely repeats ordinary dictionary meaning, a Term used with conflicting Project-specific meanings, a Term's wording substituted for a direct Subject reference, **and** a complete composite Subject Path classified as a Term.

add a source occurrence with evidence of Project-specific use but no active defining authority **in** the declared applicable source authority boundary with complete checked definition coverage; two incompatible active definitions; duplicate active defining authority; **and** a case whose context **or** source coverage cannot settle classification. include sentence-initial ordinary vocabulary, Scope Unit **and** Actor names, identifiers, paths, **and** syntax tokens with no evidence of Project-specific vocabulary meaning. include a definition excluded by a filtered selection, source occurrences of the same spelling with different evidenced contexts, an entry lacking an exact occurrence **or** Revision, **and** invented edges between indexed entries.

## Acceptance criteria

the consistently used Project-specific Term satisfies the checked source-meaning condition **and** resolves **to** its active Definition Atom. the ordinary word remains valid general language **without** being classified as a Term. consistent use **or** capitalization alone does **not** establish a Term. **in** a Subject Path, **every** named component is a Term reference that requires validation; its occurrence does **not** establish the referenced Term's defining authority. a dictionary-only definition does **not** qualify for a Catalog's governed-definition entries; it **may** be retained as diagnostic source evidence under CA-R-1455. conflicting meanings fail the checked source-meaning condition with the defining Atom **and** conflicting uses identified. a Subject is the direct GOVERNS **or** DEPENDS_ON Relation connecting an Atom **to** its canonical Entity, Action, **or** Process target; the target is **not** the Subject Relation. substituting the Term's wording for a direct Subject reference **or** classifying a complete composite Subject Path as a Term fails the checked Subject-reference condition. terminology entries retain their source references **without** independent authority.

the diagnostic index distinguishes supported ordinary English use, missing defining authority, conflicting defining authority **or** uses, **and** explicitly uncertain cases. **every** judgment retains the exact occurrence, surrounding Claim **or** reference context, Artifact Revision, source selection, **and** checked definition coverage. ordinary vocabulary requires no Project-specific definition; a source occurrence's capitalization does **not** become evidence of missing authority. outside a named Subject Path component, names, identifiers, paths, **and** syntax tokens do **not** become unresolved Project-specific candidates **without** contextual evidence of that use. use as a named Subject Path component establishes a required Term-reference context; an unresolved reference stays visible, **without** the diagnostic inventing its definition. a missing-authority judgment requires complete checked definition coverage for its declared applicable source authority boundary; absence from incomplete **or** filtered coverage alone cannot establish that judgment. duplicate active defining authority fails uniqueness even **when** the definitions agree; the diagnostic identifies an authority conflict **without** inventing a meaning conflict. an evidence-backed candidate remains diagnostic **without** a fabricated definition; a case whose evidence is insufficient remains reviewable as uncertain **without** an established Term classification. spelling alone does **not** transfer classification across source contexts. missing occurrence **or** revision traceability, hidden uncertainty, unsupported semantic certainty, **or** invented graph edges fail. a source-backed uncertain result passes the diagnostic-index check while the underlying meaning **or** authority remains unresolved.

the Evaluation **must** distinguish the correctness of the diagnostic Projection from the source conditions it reports. a faithful diagnostic **may** pass its Projection-correctness checks while identifying a failed source-meaning, defining-authority, **or** Subject-reference condition; an unresolved source condition remains unresolved. a Projection omission, unsupported judgment, lost source traceability, **or** concealed uncertainty fails the diagnostic check. passing that check **must not** become an unqualified claim that the represented source model is valid **or** complete beyond the declared checked coverage.

## Failure disposition

record a Concern identifying the affected wording, defining Atom, conflicting use, direct Subject reference, **or** Catalog entry, together with its exact source occurrence **and** Revision. distinguish a failed index check from a faithfully reported failed **or** unresolved source condition; do **not** fabricate authority **to** make either pass.
