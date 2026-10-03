---
atom_id: CA-M-125
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Subject Assignment
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Subjects
      - Subject Path
      - Subject/Relation Kind
      - Subject/Temporal Form
version: 10
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-125-CORE_META_MODEL-CORE-METHOD--assign-subjects-from-the-claim.md
---
# Assign Subjects from the Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the complete Claim.
2. select the **`=1`** Entity that the Claim governs **and** reference its narrowest exact Subject Path.
3. assign GOVERNS to that Subject.
4. select **every** Entity that the Claim requires **without** governing it **and** assign DEPENDS_ON to its Subject.
5. assign CONTINUANT **when** the relation presents its referenced Entity as persisting through time **and** assign OCCURRENT **when** the relation presents its referenced Entity as happening **or** unfolding through time.
6. include the defined Term **in** GOVERNS for **every** definition Claim.
7. include **every** prerequisite Entity **in** DEPENDS_ON.
8. split the Atom **before** assignment **when** the Claim governs more than one Entity.
9. record **every** distinct Subject exactly once.
