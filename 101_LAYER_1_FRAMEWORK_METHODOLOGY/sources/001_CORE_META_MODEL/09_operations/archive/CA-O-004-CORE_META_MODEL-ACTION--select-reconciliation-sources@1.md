---
atom_id: CA-O-004
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Select Reconciliation Sources"
  depends_on:
    - "Action"
    - "Projection/Type: Reconciled Projection"
    - "Artifact/Revision"
    - "Atom/Claim"
version: 1
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
---
# Select reconciliation sources

Select Reconciliation Sources **means** the reusable Action that resolves the complete source selection required by applicable governing authority **and** returns the exact selected source identities **and** Revisions as one source frontier. it **must** preserve source-selection constraints, include **every** eligible source, **and** retain unresolved selection ambiguity as a reported failure rather than silently choosing **or** discarding a source. selection does **not** change source authority **or** publish a Projection.
