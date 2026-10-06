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
      - "Atom/Claim"
      - "Atom/Subjects"
      - "Subject Path"
      - "Subject/Relation Kind"
      - "Subject/Temporal Form"
      - "Author"
      - "Entity"
      - "Term"
      - "Atom/Content Role: Evaluation"
      - "Evaluation For Relation"
version: 13
updated_at: "2026-09-11 22:54:39 +0400"
relations: {}
---
# Assign Subjects from the Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the complete Claim.
2. select the **`=1`** Entity that the Claim governs **and** reference its narrowest exact Subject Path. **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the Entity whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under CA-R-1018.
3. assign GOVERNS **to** that Subject.
4. select **every** Entity that the Claim requires **without** governing it **and** assign DEPENDS_ON **to** its Subject.
5. assign CONTINUANT **when** the relation presents its referenced Entity as persisting through time **and** assign OCCURRENT **when** the relation presents its referenced Entity as happening **or** unfolding through time.
6. for a definition Claim, use the defined Term **in** the Subject Path that references the Entity being defined; the GOVERNS Subject is the connection **to** that Entity, **not** the word **or** phrase itself.
7. include **every** prerequisite Entity **in** DEPENDS_ON.
8. split the Atom **before** assignment **when** the Claim governs more than one Entity.
9. record **every** distinct Subject exactly once.
