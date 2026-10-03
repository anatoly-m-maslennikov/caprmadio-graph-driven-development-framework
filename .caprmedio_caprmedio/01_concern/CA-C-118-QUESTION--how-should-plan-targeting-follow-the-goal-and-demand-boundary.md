---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Relational Atom"
  depends_on:
    - "Atom/Claim"
    - "Scope Unit"
    - "Atom Collection/Type: Epic"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Plan/Type: Objective"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Atom/Content Role: Requirement/Type: Demand"
priority: medium
version: 1
updated_at: "2026-09-17 02:47:51 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should Plan targeting follow the Goal and Demand boundary?

how should existing Task **and** Objective targets be represented under the Operator's latest rule that explicit Claim Scope Unit is for Relational Goal **and** Demand Atoms, **without** inventing a Plan exception **or** losing the target of an Epic Objective?

## Evidence

the older active authority uses Claim Structural Entity, permits Objective as a Relational Type, requires one structural target for every Claim, **and** defaults a Task target **to** its enclosing Scope Unit. an Objective specifically targets an Epic, which is **not** a Scope Unit. a textual rename from Claim Structural Entity **to** Claim Scope Unit would therefore change its admitted target domain, **not** merely its spelling. existing P Carriers are outside this active RMEDO repair frontier.

## Principle check

CA-M-002 rejects duplicate target representations; CA-M-006 requires one coherent interpretation; CA-R-1490 protects still-needed Task **and** Objective information. latest Operator input prevails, but the Principles do **not** justify quietly retaining a forbidden P exception, treating an Epic as a Scope Unit, removing an Objective target, **or** inventing another Property **to** bypass the restriction.

## Disposition

defer the unsupported Plan-targeting decision **and** coordinated migration. resolve whether **and** how the existing Epic reference survives **without** becoming Claim Scope Unit, **and** how narrower Task applicability is expressed under the current Scope Unit. update the single owning R/M/E/D authority coherently **before** target-sensitive rewrites; obtain scope authorization for P Carrier changes rather than silently mutating them. do **not** report the current competing target definitions as reconciled.

## Current authority inspected

- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-919-CORE_META_MODEL-CORE-REQUIREMENT--give-every-claim-one-structural-entity.md` at Version **15**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-923-CORE_META_MODEL-CORE-REQUIREMENT--define-relational-atom.md` at Version **18**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-924-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-relational-atom-classifications.md` at Version **16**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1365-CORE_META_MODEL-CORE-REQUIREMENT--define-objective-atom.md` at Version **9**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1445-CORE_META_MODEL-GENERAL-REQUIREMENT--default-task-target-to-the-enclosing-scope-unit.md` at Version **4**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1446-CORE_META_MODEL-CORE-REQUIREMENT--define-claim-structural-entity.md` at Version **4**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-367-CORE_META_MODEL-DELIVERY--serialize-claim-structural-entity-only-for-relational-atoms.md` at Version **7**.
