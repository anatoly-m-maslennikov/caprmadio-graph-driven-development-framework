---
atom_id: CA-M-224
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    continuant:
      - Applicable Methodology/Sources
      - Applicable Methodology
      - Local Configuration
      - Artifact/Revision
version: 7
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Compile Applicable Methodology Deterministically

**to** compile Applicable Methodology, the Compiler **must** perform **all** of:

1. resolve the exact current source set from Local Configuration.
2. require CORE_META_MODEL **and** LOCAL_CONFIGURATION **and** include **only** explicitly selected active Extension revisions.
3. select **`=1`** current active revision of **every** retained source Atom whose Content Role is **in** (REQUIREMENT, METHOD, EVALUATION, DELIVERY, OPERATIONS).
4. preserve **every** selected Atom ID, exact source revision, authority owner, **and** Claim **without** synthesis **or** merge.
5. detect **every** duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, **and** unresolved priority.
6. calculate one deterministic digest of the exact selected source frontier.
7. report the complete deterministic conflict set **before** changing Applicable Methodology membership.
8. apply a conflict resolution **only** **if** source authority records one unambiguous Operator approval bound to that exact conflict **and** source-frontier digest.
9. fail **without** changing Applicable Methodology membership **if** **any** conflict remains unresolved **or** **any** approval is stale, partial, missing, ambiguous, **or** mismatched.
10. never use source order, Claim synthesis, Claim merge, **or** LLM inference to resolve a conflict.
11. produce the same ordered Applicable Methodology membership from the same resolved source frontier.
