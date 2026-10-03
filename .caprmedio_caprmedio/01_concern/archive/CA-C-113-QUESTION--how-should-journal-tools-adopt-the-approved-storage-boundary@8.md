---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Journal"
  depends_on:
    - "Journal/Record"
    - "Artifact/Carrier"
    - "Atom/Revision"
    - "Atom/Content Role: Evaluation"
version: 8
updated_at: "2026-09-17 13:04:01 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
priority: medium
---
# How should Journal Tools adopt the approved storage boundary?

which bounded Tool changes implement CA-R-1491, CA-D-340, CA-D-435, CA-E-462, CA-E-465, **and** CA-E-476 while retaining independent conformance checks **and** safe append integrity?

## Evidence

`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/work_journal.py` currently calls `_validate_replacement_payload` from `validate_sealed_event`. that path checks the current Atom-ID grammar, successor distinctness, archive placement, filename identity, **and** archive Version. the newer Core authority explicitly separates those Project checks from Journal admission.

eleven sealed batches remain pending because observed legacy predecessor identities fail that implementation:

- `.caprmedio_tmp/repairs/2026-09-16-release-readiness-journal-pending.json`: **14** events, including `CAPRMEDIO-GOV-REQU-301` retirement evidence.
- `.caprmedio_tmp/repairs/2026-09-17-project-boundary-retirement-journal-pending.json`: **2** events, including `CAPRMEDIO-REQU-008` retirement evidence.
- `.caprmedio_tmp/repairs/2026-09-17-projection-split-identity-journal-pending.json`: **2** events for the new `CA-R-1495` timestamp Requirement **and** retirement of `CAPRMEDIO-META-REQU-166` into `CA-R-1495`, `CA-R-1493`, **and** `CA-R-1494`. the source split **and** exact archives are present; neither event was appended because the current validator rejects the observed legacy predecessor ID.

- `.caprmedio_tmp/repairs/2026-09-17-authority-properties-split-journal-pending.json`: **7** events for the four new Property/separation Atoms `CA-R-1499` through `CA-R-1502`, the current dependent revision, **and** retirement of `CAPRMEDIO-META-REQU-129`. exact source **and** archive bytes are verified; the entire batch remains unappended because the observed legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-evaluation-mechanism-split-journal-pending.json`: **11** events for `CA-R-1503` through `CA-R-1506`, three dependent revisions, **and** retirement of `CAPRMEDIO-META-REQU-094`. the split sources **and** exact archives are present; the entire batch remains unappended because the observed legacy predecessor ID fails the same validator.

- `.caprmedio_tmp/repairs/2026-09-17-clarification-actor-journal-pending.json`: **2** events for replacement of `CAPRMEDIO-GOV-REQU-335` by `CA-O-056/Actor`, preserving the four clarification gates **and** the authority boundary. the exact predecessor is archived; the batch remains unappended because the legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-analysis-optional-actor-journal-pending.json`: **2** events for replacement of `CAPRMEDIO-META-REQU-120` by `CA-O-057/Actor`, preserving authorized direct Spec creation **and** optional Analysis. the exact predecessor is archived; the batch remains unappended because the legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-mutation-permission-dedupe-journal-pending.json`: **1** events for retirement of `CAPRMEDIO-META-REQU-146` into the existing `CA-O-049/Actor`; the broader current delegation policy already covers Atom mutation. the exact predecessor is archived; the batch remains unappended because the legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-scope-type-encoding-dedupe-journal-pending.json`: **1** event for retirement of `CAPRMEDIO-GOV-REQU-718` into existing `CA-D-442` **and** `CA-R-1484`. the distinct parent **and** Type declarations preserve the retired encoding rule; its exact predecessor is archived. the original sealed event remains unappended because the legacy predecessor ID fails the same validator.

- `.caprmedio_tmp/repairs/2026-09-17-tier-validation-ownership-journal-pending.json`: **3** events for absorption of `CAPRMEDIO-GOV-REQU-685` into `CA-E-456` **and** `CA-D-285`, preserving Goal/Type restrictions **and** tierless external Goal interpretation. the current sources **and** exact archives are verified; the complete sealed batch remains unappended because its legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-relation-status-validation-ownership-journal-pending.json`: **3** events for absorption of `CAPRMEDIO-GOV-REQU-768` into `CAPRMEDIO-GOV-EVAL-005` **and** `CA-D-295`, preserving the Active-source RMED-to-RMED boundary **and** canonical lifecycle placement. the current sources **and** exact archives are verified; the complete sealed batch remains unappended because its legacy predecessor ID is rejected.

## Principle check

CA-R-1490 requires preservation of valuable evidence. CA-M-002 rejects duplicate authority; the existing independent CA-E-462 already owns replacement correctness. those Principles support separating conformance from append admission, **not** discarding identities, changing historical payloads, bypassing access controls, **or** reporting an unrun check as passed.

## Disposition

the active repair frontier covers source Atoms; Tool implementation changes are **not** silently included. the Atom conflict is corrected, while implementation **and** pending-event append remain deferred. preserve the exact pending evidence. the follow-up **must** demonstrate valid-envelope acceptance of legacy **and** malformed Project payload, unchanged-payload preservation, digest **and** authorization enforcement, idempotent replay, **and** independent replacement-conformance findings **before** appending the pending batches through the supported boundary. this Concern does **not** approve mutation of Journal history **or** assert that the Tool already conforms.
