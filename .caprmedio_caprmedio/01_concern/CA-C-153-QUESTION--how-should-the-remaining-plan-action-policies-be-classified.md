---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Actor"
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Operations"
    - "Atom/Local Tier: Principle"
    - "Operator"
    - "AI Agent"
priority: medium
version: 1
updated_at: "2026-09-17 15:13:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the remaining Plan Action Policies be classified?

which exact role mapping preserves the three remaining Actor policies **before** retiring the Plan Action Policy registration?

## Evidence

GOV-REQU-753 still admits `Plan/Type: Action Policy`. P-032, P-033, **and** P-034 still use `ACTION_POLICY`; P-032 classifies Actors, P-033 reserves original Operator authority, **and** P-034 limits AI Agent authority. newer R-1496 admits O/Actor for participation **and** authorization policies, while R-1282 classifies by the Claim's contribution rather than merely its mentioned Actor. D-386 **and** GOV-EVAL-009 also name Action Policy among priority-field exclusions, **and** METHODOLOGY-REQU-491 references the old registration.

## Principle check

the Operator-authority **and** Actor-distinction Principles must remain intact. CA-M-002 rejects parallel admission owners, CA-M-006 requires policy **and** role agreement, **and** CA-R-1490 protects their unique authority boundaries. deleting the registry first would strand live Carriers; moving all three mechanically into O would overlook the classification-versus-authorization distinction.

## Disposition

preserve the registration **and** policies until their exact replacement mapping **and** incoming references are reconciled. keep the policies distinct where they make independently replaceable Claims; preserve Principle/Core placement **and** delegated-authority limits. the current RMEDO source repair does **not** silently rewrite these P Carriers **or** remove their admission while they remain active.

## Inspected source Revisions

- `CAPRMEDIO-GOV-REQU-753` Version 19: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-753-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--register-plan-role-types.md`; SHA-256 `6fa063d7869634e5822192a5a6f5a4a96ac4dcca5307b62b30e0d881e189d366`.
- `CA-P-032` Version 5: `.caprmedio_caprmedio/03_plan/CA-P-032-PRINCIPLE-ACTION_POLICY--distinguish-human-operators-from-ai-agents.md`; SHA-256 `7f5b6b5ea4469ac6d2c25046850ef2b1128038f533ac7741f4c156b61e8767c3`.
- `CA-P-033` Version 9: `.caprmedio_caprmedio/03_plan/CA-P-033-PRINCIPLE-ACTION_POLICY--the-operator-holds-authority.md`; SHA-256 `687cd7b7b001f7a86eb687930b3cb14bd340179a531d627be8fe15469894d4f4`.
- `CA-P-034` Version 6: `.caprmedio_caprmedio/03_plan/CA-P-034-CORE-ACTION_POLICY--ai-agents-act-within-permission.md`; SHA-256 `22f827e76b5ffc5191b23b9bddafa84d626b7e9c40128c54372b7b2ebead307e`.
- `CA-R-1282` Version 7: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1282-CORE_META_MODEL-CORE-REQUIREMENT--define-content-role-as-an-atom-property.md`; SHA-256 `555838efe33f1ee23c0f81b01afa034f8e81d1a5bc215ab1650b453f9dac4282`.
- `CA-R-1496` Version 1: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1496-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-action-process-and-actor-types-for-operations-atoms.md`; SHA-256 `92e63c5a218b970cef139e16aa22a71db14f621acf1cc33035fe833a39ae8049`.
- `CA-D-386` Version 4: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-386-CORE_META_MODEL-DELIVERY--serialize-concern-priority.md`; SHA-256 `4bf7952b78ff67becb9fe2e44b590ccdeb99a7e7eba9dcb75ba2dbf406d363d4`.
