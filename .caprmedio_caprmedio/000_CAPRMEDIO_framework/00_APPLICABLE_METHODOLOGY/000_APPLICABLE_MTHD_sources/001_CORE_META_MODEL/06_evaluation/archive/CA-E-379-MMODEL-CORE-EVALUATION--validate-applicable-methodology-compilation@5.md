---
atom_id: CA-E-379
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation Validation
  depends_on:
    continuant:
      - Applicable Methodology
      - Applicable Methodology/Sources
      - Local Configuration
version: 5
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Validate Applicable Methodology Compilation

the Applicable Methodology Compilation Validation **must not** pass **if** (CORE_META_MODEL **or** LOCAL_CONFIGURATION is omitted **or** an unselected **or** inactive Extension revision contributes **or** a selected Atom revision is **not** current **and** active **or** its Content Role is outside (REQUIREMENT, METHOD, EVALUATION, DELIVERY, OPERATIONS) **or** a selected Atom ID, exact source revision, authority owner, **or** Claim is changed **or** Claims are synthesized **or** merged **or** the conflict report omits a duplicate Atom identity, unresolved replacement, incompatible retained Candidate, **or** unresolved priority **or** **any** conflict is resolved **without** one unambiguous Operator approval **in** source authority bound to the exact conflict **and** source-frontier digest **or** **any** approval is stale, partial, missing, ambiguous, **or** mismatched **or** source order resolves a conflict **or** compilation uses LLM inference **or** the same resolved source frontier produces different Applicable Methodology membership).
