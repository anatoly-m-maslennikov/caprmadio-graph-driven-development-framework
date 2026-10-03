---
atom_id: CA-P-114
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Bootstrap Carrier Structure
    occurrent:
      - Bootstrap Structure Retirement
  depends_on:
    occurrent:
      - CA-P-113
version: 1
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Retire Mapped Obsolete Bootstrap Structures

**when** CA-P-113 is Done, **then** the Assignee **must** retire exactly the obsolete empty structures authorized by the accepted CA-P-108 migration map.

## Scope

`(all directories and ownership roots with an accepted retirement disposition in the CA-P-108 migration map)`

## Definition of Done

the Task is **not done if** (any mapped obsolete structure remains **or** any removed structure lacks an accepted CA-P-108 retirement disposition **or** any removed directory was non-empty at removal **or** any canonical successor and migrated content digest was unverified before removal **or** .caprmedio or .caprmedio_install remains **or** any archive, Journal, migration map, source manifest, or rollback evidence is removed **or** rollback cannot restore the exact pre-retirement directory state).

## Details

remove only structures recorded as empty in the frozen CA-P-102 structural manifest and still verified empty immediately before retirement. preserve every archive, Journal, migration map, source manifest, and validation record. stop and request Operator disposition when live state differs from the accepted map.
