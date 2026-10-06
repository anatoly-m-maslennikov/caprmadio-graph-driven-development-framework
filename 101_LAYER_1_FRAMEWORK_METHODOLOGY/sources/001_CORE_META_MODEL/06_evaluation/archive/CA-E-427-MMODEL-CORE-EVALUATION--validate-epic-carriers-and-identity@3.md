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
version: 3
updated_at: 2026-09-04 02:03:03 +0400
relations:
  evaluation_for:
    - CA-R-1298
    - CA-R-1299
    - CA-R-1304
    - CA-R-1366
    - CA-R-1369
    - CA-D-293
    - CA-D-295
---
# Validate Epic Carriers and Identity

## Claim checked

**every** Epic **must** be a Structural Entity with **`=1`** Directory Carrier, **`=1`** canonical Epic Identifier, **`=1`** canonical Directory Carrier name, **`=1`** Core Status **in** (Active, Done, Cancelled), Status-qualified placement, **and** identity independent from member changes.

## Test case

create one Active Epic **in** its canonical current directory, one Done Epic **in** `done`, **and** one Cancelled Epic **in** `cancelled`; use canonical identifiers **and** Directory Carrier names; **and** add, remove, reorder, **and** change members **without** changing Epic identity. **then** create an Epic with **`!=1`** Directory Carriers, use malformed identifiers **or** names, place a non-Active Epic outside its Status subdirectory, place an Active Epic inside a Status subdirectory, **and** change Epic identity **after** a member change.

## Acceptance criteria

**all** valid fixtures preserve one Epic identity **and** pass. **all** invalid fixtures fail.

## Failure disposition

record a Concern naming the invalid Epic Carrier, Identifier, Status, placement, **or** identity fact.
