---
subjects:
  governs: "Subject Assignment"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Subjects"
    - "Subject Path"
    - "Author"
    - "Subject"
    - "Term"
    - "Atom/Content Role: Evaluation"
    - "Evaluation For Relation"
    - "Entity"
    - "Dependent Entity"
version: 25
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-125"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Assign Subjects from the Claim

## Scope

Subject assignment for an Atom from its Claim **and** complete Markdown Main Content.

## Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. build an inventory of canonical Entity mentions with exact locations **and** full resolved paths. treat an Atom citation label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path. under `CA-R-1280-CORE_META_MODEL-CORE-REQUIREMENT--reference-every-prerequisite-subject-through-depends-on`, the label is readable reference evidence, **not** an Entity mention **or** Subject target, including **when** it occurs **in** the same sentence as Entity language; inventory an Entity **only** **when** surrounding prose independently uses it.

   recognize Terms through their existing definitions, including `Term` itself under `CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term`. `Evaluation` remains a Term **when** used inside an Evaluation Atom under `CA-R-1341-CORE_META_MODEL-CORE-REQUIREMENT--define-evaluation-content-role`. resolve its referenced Entity from that definition **and** the usage context. self-reference alone does **not** (remove a mentioned Entity from the inventory **or** establish a new Entity); a Term's spelling alone does **not** establish its Subject target. retain unresolved meaning as an explicit gap rather than treating it as ordinary wording.
2. select the **`=1`** canonical Entity that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.

   - for a Claim about entry **or** exit criteria of a Dependent Entity, apply this same narrowest-target rule rather than substituting its wider bearer.
   - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under `CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets`.
3. connect **every** other Entity **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. include mentions outside Claim; do **not** repeat GOVERNS **or** add unmentioned Entities. unresolved mentions block completion rather than disappearing from the inventory.
4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under `CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term`. resolve **every** named path component as a Term reference; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical targets.
6. verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Entity mentions.
7. serialize the direct references under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.

## Details
