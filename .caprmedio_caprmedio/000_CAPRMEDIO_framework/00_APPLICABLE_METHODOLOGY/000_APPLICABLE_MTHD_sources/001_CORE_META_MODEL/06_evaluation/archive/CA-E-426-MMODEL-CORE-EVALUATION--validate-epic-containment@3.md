---
atom_id: CA-E-426
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Epic Containment Validation
  depends_on:
    continuant:
      - "Atom Collection/Type: Epic/Direct Membership"
      - "Atom Collection/Type: Epic/Recursive Membership"
      - "Atom/Content Role: Plan/Type: Task/Epic Membership"
      - Structural Entity/Direct Containment
      - Structural Entity/Recursive Containment
      - Artifact/Status/Carrier Placement/Status Subdirectory
version: 3
updated_at: 2026-09-04 02:03:03 +0400
relations:
  evaluation_for:
    - CA-R-1300
    - CA-R-1301
    - CA-R-1302
    - CA-R-1303
    - CA-R-1370
    - CA-D-264
    - CA-D-265
    - CA-D-266
    - CA-D-352
---
# Validate Epic Containment

## Claim checked

the containment of an Epic **must** derive from the nearest ancestor Directory Carrier; its direct members **must** be **only** Epics **and** Plan/Task Atoms; one Plan/Task Atom **must** have **`<=1`** direct Epic; recursive membership **must** derive by transitive closure; containment **must not** contain a cycle; Status subdirectories **must not** alter containment; **and** derived containment **must not** be persisted as independent relation declarations.

## Test case

create a standalone Epic, an Epic with one direct Plan/Task Atom, a Plan/Task Atom below the Epic's `done` Status subdirectory, **and** a nested Epic below the containing Epic's `cancelled` Status subdirectory. **then** place another Artifact Type directly in an Epic, give one Plan/Task Atom two direct Epic memberships, add an Epic containment cycle, derive recursive membership outside the direct-membership transitive closure, treat a Status subdirectory as a Directory Carrier, **and** persist `CONTAINS` **or** `IS_CONTAINED_BY` as independent relations.

## Acceptance criteria

the valid fixtures derive the expected direct **and** recursive memberships. **all** invalid fixtures fail.

## Failure disposition

record a Concern naming the invalid Epic containment fact.
