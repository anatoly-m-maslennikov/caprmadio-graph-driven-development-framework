---
atom_id: CA-E-379
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Applicable Methodology Compilation Validation"
  depends_on:
    - "Applicable Methodology"
    - "Applicable Methodology/Sources"
    - "Project Configuration"
    - "Extension"
    - "Framework Instance Settings"
    - "Methodology Source/Expansion Boundary"
    - "Atom/Revision"
    - "Atom/Claim"
    - "Operator"
    - "Applicable Methodology Compilation"
version: 12
updated_at: "2026-09-14 01:36:43 +0400"
relations:
  evaluation_for:
    - CA-O-011
    - CA-R-1228
    - CA-R-1375
    - CA-R-1434
---
# Validate Applicable Methodology Compilation

the Applicable Methodology Compilation Validation **must not** pass **if** **any** of:

- CORE_META_MODEL, PROJECT_CONFIGURATION, **or** an applicable installed Extension Source under CA-R-1228 is omitted; an unselected **or** inactive Extension revision contributes.
- an eligible current active source Atom under CA-R-1315 is omitted, **or** an ineligible Atom Revision contributes.
- compilation requires a hard-coded Extension name **or** particular Project-specific Project Configuration contents, rejects a conforming source merely because its contents are new, **or** requires an empty INSTALLED_EXTENSIONS Carrier **when** no Extension is applicable.
- a selected Atom ID, exact source Revision, authority owner, **or** Claim changes; Claims are synthesized **or** merged; a projected member loses its required source traceability **or** Carrier form.
- the conflict report omits a Core expansion-boundary violation, duplicate Atom identity, unresolved replacement, incompatible retained Candidate, **or** unresolved priority; source Atoms are silently discarded **to** hide a conflict.
- a conflict is resolved **without** an unambiguous Operator approval **in** source authority bound to the exact conflict **and** source-frontier digest; an approval is stale, partial, missing, ambiguous, **or** mismatched; a prohibited Extension **or** Project Configuration override is accepted as conforming.
- source order **or** LLM inference resolves a conflict, projected Claims are directly corrected, **or** the same resolved source frontier produces different Applicable Methodology membership.

the Evaluation **must** cover an empty Extension contribution, a newly installed conforming Extension with a previously unknown name, changed conforming Project Configuration contents, **and** an expansion that violates Core authority. conforming input changes **must not** require edits to generic Core compilation rules merely **to** recognize their names **or** contents.
