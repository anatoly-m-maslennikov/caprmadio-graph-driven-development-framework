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
version: 19
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
---
# Assign Subjects from the Claim

**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the complete Claim.
2. select the **`=1`** canonical Entity that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.

   - for a Claim about entry **or** exit criteria of a Dependent Entity, apply this same narrowest-target rule rather than substituting its wider bearer.
   - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under CA-R-1018.
3. select **every** canonical Entity that the Claim requires **without** governing it **and** connect the Atom **to** that Entity through DEPENDS_ON using its narrowest exact full Subject Path.
4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under CA-R-1279. resolve **every** named path component as a Term reference; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical targets.
6. record **every** distinct direct reference exactly once **without** creating an intermediate Subject object **or** repeating the target's kind **or** definition.
7. serialize the direct references under CA-D-269. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.
