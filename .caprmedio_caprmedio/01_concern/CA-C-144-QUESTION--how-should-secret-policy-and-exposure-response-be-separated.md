---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Actor"
  depends_on:
    - "Atom/Content Role"
    - "Action"
    - "Process"
    - "Carrier"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-17 14:22:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should secret policy and exposure response be separated?

which existing **or** replacement Claims preserve the complete secret-protection boundary while separating permitted credential use, personal-identifier handling, **and** exposure response?

## Evidence

GOV-REQU-290 combines secret classification **and** excluded surfaces, Operator-authorized authentication, transport **and** resource limits, required redaction, personal-identifier minimization, **and** an exposure-response sequence. the response stops propagation, revokes **or** rotates the secret, cleans affected Carriers, **and** records the incident **without** reproducing it. deleting a current file alone is explicitly insufficient for history **or** replicas. D-452 separately owns permitted storage **and** local injection Carriers.

## Principle check

CA-M-001 **and** CA-M-006 require coherent responsibility boundaries; CA-M-002 requires reuse of D-452 **and** Actor permission authority; CA-R-1490 protects **every** unique condition. R-1452 does **not** admit an arbitrary large procedure as **`=1`** atomic Action. R-1453 requires explicit Action references for a Process. moving the complete response into O **without** those boundaries would leave the modeling issue unresolved.

## Disposition

preserve the source pending a complete policy **and** Action mapping. do **not** infer new authorization **to** revoke credentials, disclose secret values, broaden permitted storage, omit a protected surface, **or** replace the response with a vague instruction. no secret, vault, environment file, **or** external account is inspected **or** changed by this Concern.

## Source snapshot

- `CAPRMEDIO-GOV-REQU-290@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-290-CORE_META_MODEL-REQUIREMENT--requirement-exclude-secrets-from-caprmedio.md`; SHA-256 `59a3bc70d3f374731e7c598f197752708103d3abf850ec7693ebc9983bb18489`.
- `CA-D-452@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-452-CORE_META_MODEL-DELIVERY--place-local-environment-injection-carriers.md`; SHA-256 `16d4a512cdc89a4854d6e62d603f9b0f383ed06c97ffc537928fa4cd456ce61f`.
- `CA-R-1452@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1452-CORE_META_MODEL-CORE-REQUIREMENT--define-action.md`; SHA-256 `f6bf25fa0e9868bb29311aebc9dde8a7f42fa3b7ab8bd9a7359f3546de931ea1`.
- `CA-R-1453@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1453-CORE_META_MODEL-CORE-REQUIREMENT--define-process.md`; SHA-256 `ef8aef1fb7a2193b3647e4de316069b2dfa2f0fd4009178421fd61d886356db4`.
- `CA-R-1496@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1496-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-action-process-and-actor-types-for-operations-atoms.md`; SHA-256 `92e63c5a218b970cef139e16aa22a71db14f621acf1cc33035fe833a39ae8049`.
