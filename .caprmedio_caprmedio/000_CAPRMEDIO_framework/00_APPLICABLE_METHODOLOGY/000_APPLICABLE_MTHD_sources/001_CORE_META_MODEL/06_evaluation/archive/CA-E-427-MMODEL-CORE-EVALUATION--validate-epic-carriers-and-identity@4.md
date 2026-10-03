---
atom_id: CA-E-427
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Epic Carrier and Identity Validation
  depends_on:
    continuant:
      - "Atom Collection/Type: Epic/Identity"
      - "Atom Collection/Type: Epic/Identifier"
      - "Atom Collection/Type: Epic/Directory Carrier"
      - "Atom Collection/Type: Epic/Directory Carrier/Name"
      - "Atom Collection/Type: Epic/Status"
      - "Artifact/Revision/Status: Archived"
version: 4
updated_at: 2026-09-04 23:52:10 +0400
relations:
  evaluation_for:
    - CA-R-1298
    - CA-R-1299
    - CA-R-1304
    - CA-R-1366
    - CA-R-1369
    - CA-R-1419
    - CA-D-293
    - CA-D-295
---
# Validate Epic Carriers and Identity

## Claim checked

**every** Epic **must** be a Structural Entity with **`=1`** Directory Carrier, **`=1`** canonical Epic Identifier, **`=1`** canonical Directory Carrier name, **`=1`** Status allowed by its Epic Status domain, Status-qualified placement, **and** identity independent from member changes.

## Test case

create one valid Epic Revision for **every** allowed Epic Status; place the Active revision **in** its canonical current directory **and** place **every** other revision **in** its Status subdirectory; use canonical identifiers **and** Directory Carrier names; preserve Archived **only** for a prior revision **or** the final revision of a replaced, absorbed, **or** retired Epic; **and** add, remove, reorder, **and** change members **without** changing Epic identity. **then** create an Epic with **`!=1`** Directory Carriers, use malformed identifiers **or** names, use a Status outside its resolved domain, place a non-Active Epic outside its Status subdirectory, place an Active Epic inside a Status subdirectory, assign Archived to a current unreplaced Epic revision, **and** change Epic identity **after** a member change.

## Acceptance criteria

**all** valid fixtures preserve one Epic identity **and** pass. **all** invalid fixtures fail.

## Failure disposition

record a Concern naming the invalid Epic Carrier, Identifier, Status, placement, **or** identity fact.
