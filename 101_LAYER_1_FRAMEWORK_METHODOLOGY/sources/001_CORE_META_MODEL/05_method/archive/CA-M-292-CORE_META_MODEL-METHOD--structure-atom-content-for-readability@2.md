---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Workflow/Relation Kind: On Result"
    - "Step"
    - "Atom"
    - "Author"
    - "CCE"
    - "Action"
    - "Workflow"
cce_version: cce_1
cce_form: method
version: 2
updated_at: "2026-09-18 14:16:20 +0000"
relations:
  child_of:
    - CA-M-113
  relates_to:
    - CA-M-229
    - CA-R-1270
    - CA-R-1508
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Structure Atom content for readability

**to** present an Atom Claim clearly, the Author **must** choose a readable structure that matches its content:

- use short, direct statements. a simple Claim **may** remain a short paragraph; do **not** compress several conditions **or** steps into dense prose.
- use bullets for unordered conditions **or** alternatives. state explicitly whether **all** conditions apply **or** **any** alternative suffices; retain the complete logical grouping.
- use a numbered list for sequential steps **only** **when** the content establishes that sequence. numbering **must not** invent execution order **or** priority.
- use a flow table for a Workflow with branches **or** loops. identify **every** Step, its **`=1`** Action reference **and** parameter/input bindings, **and** the typed Relation, result condition, **and** next Step **or** terminal outcome for **every** transition, preserving the Workflow model under CA-R-1508.

**when** applying the chosen layout, the Author **must** satisfy **all** of the following:

- preserve the complete Claim **and** its qualifications.
- retain the Atom boundary under CA-R-1270; list items, sentences, **and** table rows do **not** determine the number of independent Claims.
- express the authoritative content once rather than repeating the same Claim **in** prose **and** a list **or** table.
- apply the existing Term **and** CCE Operator rendering Method under CA-M-229 throughout.
