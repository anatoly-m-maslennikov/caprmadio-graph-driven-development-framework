---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Claim-Subject Relation Assignment
  depends_on:
    continuant:
      - Claim
      - Subject Path
      - Claim-Subject Relation
version: 7
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Assign Claim-Subject Relations from the Claim

**to** assign an Atom's Claim-Subject Relations, the Author **must** perform **all** of:

1. read the complete Claim.
2. select **every** independent Entity that the Claim governs **or** requires **and** reference its narrowest exact Subject Path.
3. assign GOVERNS **when** the Claim establishes authority about the referenced Subject **and** assign DEPENDS_ON **when** the Claim requires the referenced Subject **without** establishing authority about it.
4. assign CONTINUANT **when** the relation presents its referenced Subject as persisting through time **and** assign OCCURRENT **when** the relation presents its referenced Subject as happening **or** unfolding through time.
5. include the defined Term **in** GOVERNS for **every** definition Claim.
6. include **every** prerequisite Subject **in** DEPENDS_ON.
7. retain **`>=1`** **and** **`<=2`** GOVERNS relations, with **`<=1`** GOVERNS relation for **every** Temporal Form.
8. apply no GOVERNS cardinality limit to DEPENDS_ON relations.
9. split the Atom **before** assignment **when** independently replaceable GOVERNS Subjects would share one Temporal Form.
10. record **every** distinct Claim-Subject Relation exactly once.
