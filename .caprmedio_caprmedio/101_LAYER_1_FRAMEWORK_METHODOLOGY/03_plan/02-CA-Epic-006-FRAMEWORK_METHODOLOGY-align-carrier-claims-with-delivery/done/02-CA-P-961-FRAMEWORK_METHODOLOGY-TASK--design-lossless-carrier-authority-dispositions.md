---
atom_id: CA-P-961
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    occurrent:
      - Atom/Content Role
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Scope
      - Carrier
      - Atom/Local Tier
      - Atom/Revision
      - Autonomous Confidence Threshold
version: 2
updated_at: "2026-09-10 17:35:45 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-960
---
# Design lossless Carrier authority dispositions

the Assignee **must** produce a lossless disposition for **every** Carrier-related Claim identified by CA-P-960.

## Claim Scope

(the Carrier-related Claims **and** existing authority owners identified by CA-P-960 **in** (CORE_META_MODEL, LOCAL_CONFIGURATION))

## Definition of Done

the Task is **not** Done **if** ((a candidate has no explicit disposition) **or** (an original clause has no allocated surviving authority owner) **or** (a proposed result duplicates existing authority) **or** (a proposed reclassification is based solely on mentioning a Carrier) **or** (an affected incoming reference needed for safe replacement has no target mapping) **or** (a disposition permits retirement **before** its required incoming-reference repairs) **or** (an unresolved decision is presented as approved)).

## Details

apply CA-R-1339, CA-R-1340, CA-R-1341, **and** CA-R-1342 together with current Project Principles, especially DRY **and** coherence. keep Content Role, source ownership, Local Tier, Claim, **and** Claim Scope as distinct decisions. do **not** equate Standard with Delivery.

for a mixed Claim, retain its R, M, **or** E contribution **and** place its independently authoritative Carrier contribution **in** existing **or** necessary new D authority. do **not** split a coherent composite Claim merely because it has several clauses. Type meaning **and** admission remain separate from concrete Carrier tokens; formatting rules remain M **and** their physical serialization remains D.

map CA-R-165 against CA-D-270, CA-R-1415, **and** CA-R-1416. preserve positive, monotonic Version **and** unambiguous date-time requirements wherever they are still distinct; do **not** retire a whole Claim merely because its YAML keys are already covered. perform the analogous comparison of Projection timestamp Claims with CA-D-310.

record exact before-to-after clause allocations, proposed identities, prior Revision preservation, affected references, **and** verification conditions. classify **every** affected incoming reference as a required pre-retirement repair, remaining non-blocking reconciliation, **or** out-of-scope follow-up. inspect out-of-scope consumers read-only. an out-of-scope repair required for safe retirement is a blocking prerequisite, **not** permission **to** expand the Task's mutation Scope. a Content Role change **must not** silently retain an Identifier whose role component denotes the previous Content Role. prefer reuse over allocating duplicate Atoms. keep the accepted Core / General / Standard classifier; justify **any** consequential tier change independently.

this is a disposition design Task, **not** source mutation. resolve questions from current Principles first. resolve the effective Autonomous Confidence Threshold under CA-M-271: direct Operator input, Task value, nearest enclosing Epic with an explicit value, **and** Framework Instance Settings default, **in** that precedence. **if** confidence is below the effective threshold, **then** ask the Operator **before** admitting the affected disposition. a sufficiently high confidence does **not** replace a separately required Operator approval. selected Settings **and** pending source-owner decisions from Epic 005 remain outside this Epic.
