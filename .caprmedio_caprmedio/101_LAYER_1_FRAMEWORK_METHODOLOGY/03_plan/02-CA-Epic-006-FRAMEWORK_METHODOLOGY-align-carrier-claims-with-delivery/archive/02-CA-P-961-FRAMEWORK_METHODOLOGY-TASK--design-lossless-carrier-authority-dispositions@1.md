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
version: 1
updated_at: "2026-09-10 13:41:47 +0400"
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-960
---
# Design lossless Carrier authority dispositions

the Assignee **must** produce a lossless disposition for **every** Carrier-related Claim identified by CA-P-960.

## Claim Scope

(the Carrier-related Claims **and** existing authority owners identified by CA-P-960 **in** CORE_META_MODEL **or** LOCAL_CONFIGURATION)

## Definition of Done

the Task is **not** Done **if** (a candidate lacks a retain, revise, split, replace, **or** deduplicate disposition **or** an original clause has no surviving authority owner **or** a proposed result duplicates existing authority **or** reclassifies a semantic definition, Method, **or** Evaluation solely because it mentions a Carrier **or** an unresolved decision is presented as approved).

## Details

apply CA-R-1339, CA-R-1340, CA-R-1341, **and** CA-R-1342 together with current Project Principles, especially DRY **and** coherence. keep Content Role, source ownership, Local Tier, Claim, **and** Claim Scope as distinct decisions. do **not** equate Standard with Delivery.

for a mixed Claim, retain its R, M, **or** E contribution **and** place its independently authoritative Carrier contribution **in** existing **or** necessary new D authority. do **not** split a coherent composite Claim merely because it has several clauses. Type meaning **and** admission remain separate from concrete Carrier tokens; formatting rules remain M **and** their physical serialization remains D.

map CA-R-165 against CA-D-270, CA-R-1415, **and** CA-R-1416. preserve positive, monotonic Version **and** unambiguous date-time requirements wherever they are still distinct; do **not** retire a whole Claim merely because its YAML keys are already covered. perform the analogous comparison of Projection timestamp Claims with CA-D-310.

record exact before-to-after clause allocations, proposed identities, prior Revision preservation, affected references, **and** verification conditions. a Content Role change **must not** silently retain an Identifier whose role component denotes the previous Content Role. prefer reuse over allocating duplicate Atoms. keep the accepted Core / General / Standard classifier; justify **any** consequential tier change independently.

this is a disposition design Task, **not** source mutation. resolve questions from current Principles first; **if** confidence is below 99%, **then** ask the Operator **before** approving the affected disposition. selected Settings **and** pending source-owner decisions from Epic 005 remain outside this Epic.
