---
subjects:
  governs: "Project Structure Maintenance"
  depends_on:
    - "Workflow/Relation Kind: On Result"
    - "Step Run"
    - "Workflow Run"
    - "Action"
    - "Step"
    - "Workflow"
    - "Project Structure"
    - "Select Reconciliation Sources"
    - "Prepare Structural Change"
    - "Assess Source Conflicts"
    - "Authorize Structural Change"
    - "Apply Structural Change"
version: 4
updated_at: "2026-09-18 14:16:20 +0000"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-M-291"
    - "CA-O-004"
    - "CA-O-005"
    - "CA-O-012"
    - "CA-O-013"
    - "CA-O-014"
---
# Maintain Project Structure

Project Structure Maintenance **means** the Workflow that maintains authoritative declarations through the following Step graph; Tools execute this Workflow **without** becoming its authority.

the entry Step is select. interpret Step bindings **and** run boundaries under CA-R-1509, CA-R-1510, **and** CA-R-1511.

## Steps

| Step | Action reference | Parameters **and** inputs |
|---|---|---|
| select | CA-O-004 | current Project Structure, relevant Settings, Goal/Atom references, **and** separate Carrier observations |
| prepare | CA-O-012 | the selected current state **and** requested structural change |
| assess-candidate | CA-O-005 | the bounded candidate **and** its stated checks |
| authorize | CA-O-013 | the assessed proposal, exact effects, **and** current state |
| apply | CA-O-014 | the exact authorized proposal **and** its unchanged source state |
| assess-result | CA-O-005 | the resulting declarations, references, Carrier observations, **and** accepted effects |

## Transitions

the transitions below use the Workflow-scoped ON_RESULT Relation under CA-R-1513 **when** the destination is a Step. a terminal outcome ends the Workflow Run; it is **not** another Step **or** Action.

| Step | Result condition | Next Step **or** outcome |
|---|---|---|
| select | exact current Project Structure, relevant Settings, Goal/Atom references **and** separate Carrier observations selected | prepare |
| prepare | bounded proposal ready | assess-candidate |
| assess-candidate | candidate conforms **and** required checks complete | authorize |
| assess-candidate | contradiction, incomplete check, **or** unresolved disposition | stop; request a corrected proposal **or** Operator decision |
| authorize | authorization valid for exact effects **and** current state | apply |
| apply | cutover completed | assess-result |
| assess-result | required checks complete **and** accepted effects verified | complete |
| **any** Step | failed, stale, ambiguous, unauthorized, **or** below-threshold outcome | stop **and** report the exact state; further attempts require applicable authorization **and** remaining retry allowance |

this Workflow produces authoritative source changes **and** validation results; it does **not** require **or** publish a separate Project Structure Projection. publication of an unrelated Projection remains a separately selected operation.
