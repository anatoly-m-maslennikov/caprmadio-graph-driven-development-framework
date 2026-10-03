---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Term"
    - "Workflow/Relation Kind: On Result"
    - "Step"
    - "Atom"
    - "Author"
    - "CCE"
    - "Action"
    - "Workflow"
version: 2
updated_at: "2026-09-18 14:37:46 +0000"
relations:
  child_of:
    - CA-M-113
  relates_to:
    - CA-M-229
    - CA-M-294
    - CA-R-1270
    - CA-R-1508
---
# Make Atom Claims easy to understand

**to** make an Atom Claim easy **to** understand, the Author **must** express **and** organize its content so the intended reader can identify what is claimed, what it concerns, **and** how its conditions **and** consequences fit together **without** guessing unstated connections.

## Meaning and context

- provide the context needed **to** interpret the Claim. reference existing governing definitions **and** authority rather than independently restating them.
- choose familiar wording under CA-M-294 **without** losing precision, necessary distinctions, **or** exact canonical Terms.
- state conditions, alternatives, **and** relationships explicitly. preserve whether **all** conditions apply **or** **any** alternative suffices, including nested logical groups.

## Structure

- use short, direct statements. a simple Claim **may** remain a short paragraph; do **not** compress several points, conditions, **or** steps into one dense sentence.
- use bullets for unordered points, conditions, **or** alternatives.
- use a numbered list for sequential steps **only** **when** the content establishes that sequence. numbering **must not** invent execution order **or** priority.
- use a flow table for a Workflow with branches **or** loops. identify **every** Step, its **`=1`** Action reference **and** parameter/input bindings, **and** the typed Relation, result condition, **and** next Step **or** terminal outcome for **every** transition under CA-R-1508.

## Preservation

- preserve the complete Claim **and** its qualifications; easier wording **or** layout **must not** change its meaning.
- retain the Atom boundary under CA-R-1270. one Claim does **not** require one sentence; paragraphs, bullets, **and** table rows do **not** determine the number of independently governed Claims.
- express authoritative content once rather than repeating the same Claim **in** prose **and** a list **or** table.
- apply the Term **and** CCE Operator rendering Method under CA-M-229 throughout.

readable layout alone is insufficient **when** the Claim still requires the reader **to** reconstruct missing context **or** logical connections.
