---
subjects:
  governs: "Subject Assignment"
  depends_on:
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Subject Path"
    - "Author"
    - "Subject"
    - "Term"
    - "Atom/Content Role: Evaluation"
    - "Evaluation For Relation"
    - "Entity"
    - "Dependent Entity"
version: 22
updated_at: "2026-09-25 22:01:55 +0000"
relations: {}
atom_id: "CA-M-125"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Archived"
author: "Anatoly Maslennikov"
type: "Method"
global_tier: 11
---
# Summary

Assign Subjects from the Claim

## Scope

Subject assignment for an Atom from its Claim **and** complete Markdown Main Content.

## Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. build an inventory of canonical Entity mentions with exact locations **and** full resolved paths.
2. select the **`=1`** canonical Entity that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.

   - for a Claim about entry **or** exit criteria of a Dependent Entity, apply this same narrowest-target rule rather than substituting its wider bearer.
   - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under CA-R-1018.
3. connect **every** other Entity **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. include mentions outside Claim; do **not** repeat GOVERNS **or** add unmentioned Entities. unresolved mentions block completion rather than disappearing from the inventory.
4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under CA-R-1279. resolve **every** named path component as a Term reference; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical targets.
6. verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Entity mentions.
7. serialize the direct references under CA-D-269. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.

## Details
