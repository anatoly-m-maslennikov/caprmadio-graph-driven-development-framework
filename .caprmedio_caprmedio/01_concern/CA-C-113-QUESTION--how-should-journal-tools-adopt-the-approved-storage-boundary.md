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
version: 18
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
priority: medium
---
# How should Journal Tools adopt the approved storage boundary?

which bounded Tool changes implement CA-R-1491, CA-D-340, CA-D-435, CA-E-462, CA-E-465, **and** CA-E-476 while retaining independent conformance checks **and** safe append integrity?

## Evidence

`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py` currently calls `_validate_replacement_payload` from `validate_sealed_event`. that path checks the current Atom-ID grammar, successor distinctness, archive placement, filename identity, **and** archive Version. the newer Core authority explicitly separates those Project checks from Journal admission.

twenty-two sealed batches remain pending because observed legacy predecessor identities fail that implementation:

- `.caprmedio_tmp/repairs/2026-09-16-release-readiness-journal-pending.json`: **14** events, including `CAPRMEDIO-GOV-REQU-301` retirement evidence.
- `.caprmedio_tmp/repairs/2026-09-17-project-boundary-retirement-journal-pending.json`: **2** events, including `CAPRMEDIO-REQU-008` retirement evidence.
- `.caprmedio_tmp/repairs/2026-09-17-projection-split-identity-journal-pending.json`: **2** events for the new `CA-R-1495` timestamp Requirement **and** retirement of `CAPRMEDIO-META-REQU-166` into `CA-R-1495`, `CA-R-1493`, **and** `CA-R-1494`. the source split **and** exact archives are present; neither event was appended because the current validator rejects the observed legacy predecessor ID.

- `.caprmedio_tmp/repairs/2026-09-17-authority-properties-split-journal-pending.json`: **7** events for the four new Property/separation Atoms `CA-R-1499` through `CA-R-1502`, the current dependent revision, **and** retirement of `CAPRMEDIO-META-REQU-129`. exact source **and** archive bytes are verified; the entire batch remains unappended because the observed legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-evaluation-mechanism-split-journal-pending.json`: **11** events for `CA-R-1503` through `CA-R-1506`, three dependent revisions, **and** retirement of `CAPRMEDIO-META-REQU-094`. the split sources **and** exact archives are present; the entire batch remains unappended because the observed legacy predecessor ID fails the same validator.

- `.caprmedio_tmp/repairs/2026-09-17-clarification-actor-journal-pending.json`: **2** events for replacement of `CAPRMEDIO-GOV-REQU-335` by `CA-R-1555/Actor`, preserving the four clarification gates **and** the authority boundary. the exact predecessor is archived; the batch remains unappended because the legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-analysis-optional-actor-journal-pending.json`: **2** events for replacement of `CAPRMEDIO-META-REQU-120` by `CA-R-1556/Actor`, preserving authorized direct Spec creation **and** optional Analysis. the exact predecessor is archived; the batch remains unappended because the legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-mutation-permission-dedupe-journal-pending.json`: **1** events for retirement of `CAPRMEDIO-META-REQU-146` into the existing `CA-R-1552/Actor`; the broader current delegation policy already covers Atom mutation. the exact predecessor is archived; the batch remains unappended because the legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-scope-type-encoding-dedupe-journal-pending.json`: **1** event for retirement of `CAPRMEDIO-GOV-REQU-718` into existing `CA-D-442` **and** `CA-R-1484`. the distinct parent **and** Type declarations preserve the retired encoding rule; its exact predecessor is archived. the original sealed event remains unappended because the legacy predecessor ID fails the same validator.

- `.caprmedio_tmp/repairs/2026-09-17-tier-validation-ownership-journal-pending.json`: **3** events for absorption of `CAPRMEDIO-GOV-REQU-685` into `CA-E-456` **and** `CA-D-285`, preserving Goal/Type restrictions **and** tierless external Goal interpretation. the current sources **and** exact archives are verified; the complete sealed batch remains unappended because its legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-relation-status-validation-ownership-journal-pending.json`: **3** events for absorption of `CAPRMEDIO-GOV-REQU-768` into `CAPRMEDIO-GOV-EVAL-005` **and** `CA-D-295`, preserving the Active-source RMED-to-RMED boundary **and** canonical lifecycle placement. the current sources **and** exact archives are verified; the complete sealed batch remains unappended because its legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-extension-nonstructural-duplicate-journal-pending.json`: **1** events for retirement of the incompatible Structural Unit exclusion **in** `CAPRMEDIO-REQU-713`; reusable packaging remains governed by `CAPRMEDIO-META-REQU-160` **and** classification by `CA-R-1217` **and** `CA-R-1219`. exact source transitions **and** archives are preserved; validation rejects the legacy predecessor ID, so the complete sealed bundle remains unappended.

- `.caprmedio_tmp/repairs/2026-09-17-lineage-impact-action-journal-pending.json`: **8** events for replacement of `CAPRMEDIO-META-REQU-090` by `CA-O-058` **and** retargeting of its three active incoming references. exact source transitions **and** archives are preserved; validation rejects the legacy predecessor ID, so the complete sealed bundle remains unappended.

- `.caprmedio_tmp/repairs/2026-09-17-scope-change-identity-dedupe-journal-pending.json`: **2** events for retirement of the unconditional identity-preservation duplicate `CAPRMEDIO-META-REQU-730` into `CA-R-1432`, `CA-R-1464`, **and** `CA-O-058`. exact source transitions **and** archives are preserved; validation rejects the legacy predecessor ID, so the complete sealed bundle remains unappended.

- `.caprmedio_tmp/repairs/2026-09-17-obsolete-operations-record-registration-journal-pending.json`: **2** events for retirement of the obsolete factual Operations Atom Type registry `CAPRMEDIO-GOV-REQU-752` **and** its Carrier-token rule `CA-D-403`. the five factual families remain covered by `CAPRMEDIO-META-REQU-143`; no recorded fact was deleted. the complete sealed batch remains unappended because validation rejects its actual legacy predecessor ID.

- `.caprmedio_tmp/repairs/2026-09-17-conflict-exploration-actor-journal-pending.json`: **2** events for the preserved exploratory-input Actor policy replacement. the exact source transitions **and** archives are present; the whole sealed batch remains unappended because the validator rejects its actual legacy predecessor ID.

- `.caprmedio_tmp/repairs/2026-09-17-exploration-policy-boundaries-journal-pending.json`: **5** events for the preserved exploratory-input Actor policy replacement. the exact source transitions **and** archives are present; the whole sealed batch remains unappended because the validator rejects its actual legacy predecessor ID.

- `.caprmedio_tmp/repairs/2026-09-17-routing-tree-evaluation-journal-pending.json`: **2** events for replacement of `CAPRMEDIO-GOV-REQU-334` by `CA-E-483`. the five routing-tree rejection conditions, exact predecessor archive, **and** current successor are preserved. validation rejects the actual legacy predecessor ID; the complete sealed batch remains unappended.

- `.caprmedio_tmp/repairs/2026-09-17-project-mode-alias-deduplication-journal-pending.json`: **2** events for absorption of `CAPRMEDIO-REQU-710` **and** `CAPRMEDIO-REQU-711` into corrected `CAPRMEDIO-REQU-029` **and** `CA-R-1430`. exact predecessor archives remain available; the validator rejects their actual legacy IDs.

- `.caprmedio_tmp/repairs/2026-09-17-casual-fallback-rule-deduplication-journal-pending.json`: **3** events for absorption of `CAPRMEDIO-REQU-041` into `CAPRMEDIO-GOV-REQU-377` **and** replacement of the surviving rule's duplicate parent with `CA-R-1430`. the exact archives **and** current successor are present; the complete bundle remains unappended because its legacy predecessor ID is rejected.

- `.caprmedio_tmp/repairs/2026-09-17-scope-name-reservation-deduplication-journal-pending.json`: **1** event for retirement of `CAPRMEDIO-REQU-614` into existing Name uniqueness, CCE reservation, Scope Unit rendering, **and** graph-dimension authority. no actual Scope Unit Name changes; the exact predecessor archive is preserved. validation rejects its actual legacy predecessor ID, so the sealed event remains unappended.

- `.caprmedio_tmp/repairs/2026-09-17-obsolete-derived-project-structure-journal-pending.json`: **1** event for retirement of obsolete derived-structure rule `CAPRMEDIO-REQU-646` into R-1483, R-1070, **and** REQU-622. the exact source is archived, its sole active incoming Skill requirement is repaired, **and** the sealed record is preserved. validation rejects the actual legacy predecessor ID; this event is **not** appended.

## Principle check

CA-R-1490 requires preservation of valuable evidence. CA-M-002 rejects duplicate authority; the existing independent CA-E-462 already owns replacement correctness. those Principles support separating conformance from append admission, **not** discarding identities, changing historical payloads, bypassing access controls, **or** reporting an unrun check as passed.

## Disposition

the active repair frontier covers source Atoms; Tool implementation changes are **not** silently included. the Atom conflict is corrected, while implementation **and** pending-event append remain deferred. preserve the exact pending evidence. the follow-up **must** demonstrate valid-envelope acceptance of legacy **and** malformed Project payload, unchanged-payload preservation, digest **and** authorization enforcement, idempotent replay, **and** independent replacement-conformance findings **before** appending the pending batches through the supported boundary. this Concern does **not** approve mutation of Journal history **or** assert that the Tool already conforms.

## Shared append capability authority

R-1126 combines the required append/idempotence outcome, shared non-executable implementation selection, exact receipt/segment encoding, the 100-event bound, **and** serialization/rollover behavior. retain sealed identity/context, digest checks inside the serialization boundary, duplicate replay **without** another append, identity-collision rejection, **and** the ban on complete-Journal rereads. separate R/M/D/O ownership **without** expanding append admission into Project conformance.

R-1127 is a capability requiring sufficient recovery evidence; it does **not** supply the recovery procedure **or** permit invented events. no validator implementation, partition policy, historical payload, **or** pending bundle is changed by this review.

## Additional inspected source Revisions

- `CA-R-1126@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1126-TOOLS-CORE-REQUIREMENT--append-work-journal-events.md`; SHA-256 `ef2aa674ebfbb481fea5a2d61c48759d8606814dcc576d4d8996401e4e212f4d`.
- `CA-R-1127@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1127-TOOLS-REQUIREMENT--reconcile-work-journal-coverage.md`; SHA-256 `0c422dc3a1e96e726e35a7981745077bcdd35668803dc3b611323b10d3530cf0`.

## Coverage recovery consumer

M-205 preserves exact action binding, an explicit coverage state **and** recovery **only** **when** durable evidence supplies **every** required field unambiguously. retain append-**only** history **and** no second recovered event on unchanged input. extraction into Operations **must** preserve these admission checks **without** turning them into Project-conformance validation **or** inventing a prior action. this review appends no recovery event for the existing pending legacy bundles.

## Additional inspected source Revisions

- `CA-M-205@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-205-TOOLS-METHOD--reconcile-work-journal-coverage-from-sealed-evidence.md`; SHA-256 `5d7a3b367420d76bfa3833ce6ee0d33738851e5e1a69cf94275d0cdbf720fe8b`.
- `CA-R-1127@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1127-TOOLS-REQUIREMENT--reconcile-work-journal-coverage.md`; SHA-256 `0c422dc3a1e96e726e35a7981745077bcdd35668803dc3b611323b10d3530cf0`.
- `CA-R-1491@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1491-CORE_META_MODEL-CORE-REQUIREMENT--keep-project-validation-out-of-journal-admission.md`; SHA-256 `8c8b7fcbe12d2ebc1e02e26229f528a5539953f88261d411a5950d7f84e97052`.
