---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand"
  depends_on:
    - "Consumer"
    - "Producer"
    - "Scope Unit"
    - "Atom/Claim"
    - "Atom/Claim/Scope Unit"
priority: medium
version: 1
updated_at: "2026-09-17 16:59:23 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the legacy MCP-to-SKILLS interface contract be represented?

which current Atom-owned Claims preserve the MCP-to-SKILLS interface requirements **without** retaining a Scope-Unit dependency graph **or** a common-ancestor Contract owner?

## Evidence

FRAMEWORK-ENGINE-CNTR-002 resides **in** FRAMEWORK_ENGINE but declares SKILLS as controller, MCP as follower, **and** `realization_input: ./PROGRAMMATIC/MCP`. its body combines supplying the generated discovery/invocation interface, Skill consumption **without** redefining behavior, **and** preservation of Tool identity, inputs, outputs, **and** failure meaning. its parent R-881 still describes cross-unit relation ownership, although current Demand authority concerns an Atom owned by the Consumer **and** targeting a permitted Producer result. C-160 separately preserves the unresolved earlier-to-later Layer rule.

## Principle check

CA-M-002 rejects a duplicate Scope Unit relation model; CA-M-001 requires distinct Claim responsibilities; CA-M-006 requires Consumer ownership **and** current relation vocabularies; CA-R-1490 protects the interface guarantees. a mechanical Contract-to-Demand rename does **not** establish the exact demanded result, ownership, **or** independently required Producer behavior. C-117 **and** C-118 retain unresolved structural **and** targeting authority.

## Disposition

preserve R-881 **and** CNTR-002 until a complete split **and** reference map establish which Claim is an actual Consumer Demand **and** which are ordinary capability constraints. remove obsolete endpoints **and** Scope Unit dependency fields as part of that gap-free replacement, **not** by dropping their sole remaining information.

## Inspected source Revisions

- `CA-R-881` Version **8**: `.caprmedio_caprmedio/04_requirement/CA-R-881-CORE-REQUIREMENT--use-relation-specific-cross-unit-ownership.md`; SHA-256 `5eb488dee69229278fc5b5156b708975e62fa02ef01b2929b462580dc518d4eb`.
- `CAPRMEDIO-FRAMEWORK-ENGINE-CNTR-002` Version **8**: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-CNTR-002-FRAMEWORK_ENGINE-REQUIREMENT--supply-the-mcp-tool-interface-to-skills.md`; SHA-256 `2b224e53c3f1119a46f54ef318d94976c1bf635e0218473629616fb6f97eb9ff`.
- `CA-R-932` Version **16**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-932-CORE_META_MODEL-CORE-REQUIREMENT--define-demand-atom.md`; SHA-256 `e3245718eece3cd2833db2dcd4292a2e44f9674d1ab7316ec628909a3d9abf2d`.
- `CA-R-934` Version **11**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-934-CORE_META_MODEL-CORE-REQUIREMENT--preserve-producer-authority-outside-demanded-result.md`; SHA-256 `4552dfd23d26c336a98e1479b30653ba1a6ad4f477ebbef568c180ccf6d025fd`.
- `CA-R-935` Version **14**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-935-CORE_META_MODEL-GENERAL-REQUIREMENT--prohibit-demands-between-ancestors-and-descendants.md`; SHA-256 `6e1ae7e3bd55ed0f0036875649210a000727bddb1101f5f6fce83134d0629bcc`.
- `CA-C-117` Version **1**: `.caprmedio_caprmedio/01_concern/CA-C-117-QUESTION--which-declarations-complete-the-authoritative-project-structure.md`; SHA-256 `18c58f8ab5fb4afaffe39137e0e0a54006d68bd45993b09d714e1cefea2a7846`.
- `CA-C-118` Version **1**: `.caprmedio_caprmedio/01_concern/CA-C-118-QUESTION--how-should-plan-targeting-follow-the-goal-and-demand-boundary.md`; SHA-256 `803d2eb754ee55684fe4ff08c1e61591ee0b11e271ed391d1e9981672815adda`.
- `CA-C-160` Version **1**: `.caprmedio_caprmedio/01_concern/CA-C-160-QUESTION--how-should-the-backward-coupling-rule-use-atom-owned-demands.md`; SHA-256 `cc1c92528baa637624cd399457b900040d37423fb8c0a557d9c0cf4c12b797eb`.
