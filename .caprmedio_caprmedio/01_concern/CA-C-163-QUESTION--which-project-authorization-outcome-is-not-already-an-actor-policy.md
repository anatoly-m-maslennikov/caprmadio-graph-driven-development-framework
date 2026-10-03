---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Operator"
    - "Project"
    - "Actor"
priority: medium
version: 1
updated_at: "2026-09-17 16:59:22 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Project authorization outcome is not already an Actor policy?

does CA-R-1058 retain a distinct required Framework capability, **or** should its governing-change authorization condition be absorbed into existing Actor policies with lossless dependent retargeting?

## Evidence

R-1058 permits establishing **or** changing governed Project meaning **only** through explicit per-action Operator acceptance **or** active delegation **to** the identified AI Agent. O-049 already restricts governed AI actions **without** per-action approval **to** active identified-Agent/action/target/constraint delegation. R-846 separately requires actual capabilities for creating, inspecting, limiting, changing, suspending, **and** revoking delegations. R-1058 is also a parent of META-REQU-689, O-048, METHODOLOGY-REQU-516, **and** FRAMEWORK-ENGINE-REQU-580, **and** is referenced by O-064. their Claims contain non-delegable Principle resolution, adaptation provenance, proposal approval, **and** raw-session consent conditions that **must not** be lost.

## Principle check

Operator authority, CA-M-002, CA-M-005, **and** CA-M-006 require one coherent authorization policy **without** erasing a distinct required capability. R-1282 classifies the primary contribution rather than the Actor named **in** the sentence. neither changing the role letter mechanically nor redirecting **every** parent link **to** O-049 proves that the authorization **and** hierarchy meanings remain unchanged.

## Disposition

preserve R-1058 **and** its dependents. determine the exact capability-versus-policy preservation map **before** retirement **or** replacement; reuse O-049 **and** R-846 **where** their actual Claims cover it. this Concern grants no new permission **and** does **not** certify the remaining role classification.

## Inspected source Revisions

- `CA-R-1058` Version **18**: `.caprmedio_caprmedio/04_requirement/CA-R-1058-CORE-REQUIREMENT--require-operator-authority-for-governed-change.md`; SHA-256 `68d0a933444129c61de3a38fffc3e2e0c49ce4cf262d46c47f183d44cbee8fb9`.
- `CA-R-846` Version **10**: `.caprmedio_caprmedio/04_requirement/CA-R-846-CORE-REQUIREMENT--let-the-operator-control-ai-permissions.md`; SHA-256 `246d5afbf348546a14d22d1ed62320ccde7cb3408124d45a76547c9d3b8543f3`.
- `CA-O-049` Version **1**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-049-CORE_META_MODEL-CORE-ACTOR--require-active-delegation-for-ai-agent-actions.md`; SHA-256 `fa39628eb68fb0f1b08c5f84b0d8fa8bb80817bc3425b714642992c4be7495be`.
- `CA-O-048` Version **1**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-048-CORE_META_MODEL-CORE-ACTOR--reserve-principle-conflict-resolution-to-the-operator.md`; SHA-256 `6fdb8ff1389e2e8e330afb495c69425607ceb1f57d04c45c236e55d139ee1b5b`.
- `CA-O-064` Version **1**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-064-CORE_META_MODEL-GENERAL-ACTOR--let-ai-agents-resolve-concerns-under-bounded-authority.md`; SHA-256 `67c1fb83582ffc5fd903128daa8fd91564af07c72f196b4c956196f29c4b47aa`.
- `CAPRMEDIO-META-REQU-689` Version **15**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-689-CORE_META_MODEL-GENERAL-REQUIREMENT--promote-project-adaptation-authority-to-an-extension.md`; SHA-256 `fd3296fd28ba5b739353333893e4488b18632e8705b03609ffb28bafc2c8f4e2`.
- `CAPRMEDIO-METHODOLOGY-REQU-516` Version **12**: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-516-FRAMEWORK_METHODOLOGY-REQUIREMENT--gate-upstream-framework-proposals.md`; SHA-256 `a145528b9377cd7fb289213ae63a89aac2e2a5535ba434ba27e73c42f4b92feb`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-580` Version **13**: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-580-SKILLS-REQUIREMENT--require-per-run-approval-for-raw-session-access.md`; SHA-256 `c958b1eff850714d4eb72779b03b603a0af7b9942db8cc15ae4b833c53b5bc90`.
