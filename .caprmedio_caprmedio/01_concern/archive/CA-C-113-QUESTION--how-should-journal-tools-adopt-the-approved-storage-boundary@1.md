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
version: 1
updated_at: "2026-09-17 02:23:48 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should Journal Tools adopt the approved storage boundary?

which bounded Tool changes implement CA-R-1491, CA-D-340, CA-D-435, CA-E-462, CA-E-465, **and** CA-E-476 while retaining independent conformance checks **and** safe append integrity?

## Evidence

`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/work_journal.py` currently calls `_validate_replacement_payload` from `validate_sealed_event`. that path checks the current Atom-ID grammar, successor distinctness, archive placement, filename identity, **and** archive Version. the newer Core authority explicitly separates those Project checks from Journal admission.

two sealed batches remain pending because observed legacy predecessor identities fail that implementation:

- `.caprmedio_tmp/repairs/2026-09-16-release-readiness-journal-pending.json`: **14** events, including `CAPRMEDIO-GOV-REQU-301` retirement evidence.
- `.caprmedio_tmp/repairs/2026-09-17-project-boundary-retirement-journal-pending.json`: **2** events, including `CAPRMEDIO-REQU-008` retirement evidence.

## Principle check

CA-R-1490 requires preservation of valuable evidence. CA-M-002 rejects duplicate authority; the existing independent CA-E-462 already owns replacement correctness. those Principles support separating conformance from append admission, **not** discarding identities, changing historical payloads, bypassing access controls, **or** reporting an unrun check as passed.

## Disposition

the active repair frontier covers source Atoms; Tool implementation changes are **not** silently included. the Atom conflict is corrected, while implementation **and** pending-event append remain deferred. preserve the exact pending evidence. the follow-up **must** demonstrate valid-envelope acceptance of legacy **and** malformed Project payload, unchanged-payload preservation, digest **and** authorization enforcement, idempotent replay, **and** independent replacement-conformance findings **before** appending the pending batches through the supported boundary. this Concern does **not** approve mutation of Journal history **or** assert that the Tool already conforms.
