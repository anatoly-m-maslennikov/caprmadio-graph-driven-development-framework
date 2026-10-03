---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Action"
  depends_on:
    - "Actor"
    - "Journal/Record"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role"
priority: medium
version: 2
updated_at: "2026-09-17 22:54:28 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# What is the canonical Initiative boundary for programmatic mutation?

which existing definition **and** carrier binding govern the sealed Initiative required for programmatic mutation, **and** which parts of its propagation belong **to** the operational Action?

## Evidence

R-1094 requires a sealed human-origin Initiative, a stable action identity, instruction-derived summary/context, **and** preservation across handoffs. M-191 resolves **or** creates that Initiative, assigns identities, propagates them, **and** blocks invalid mutation. its complete flow has an O contribution. the inspected Claims do **not** settle whether Initiative is an independent Entity, a qualified instruction grouping, **or** an existing action-context representation. widespread use of the name is **not** itself a definition.

## Principle check

DRY **and** minimum necessary complexity require reusing an existing representation **when** it preserves attribution. coherence **and** information preservation require retaining the human instruction, exact action identity, handoff continuity, **and** no-substitution rules. these Principles do **not** justify inventing an Initiative Entity **or** replacing it with Task, execution, **or** Journal Event identity.

## Disposition

preserve the attribution **and** mutation-admission requirements. resolve the canonical Initiative target **before** moving its identity fields into D **or** replacing M-191 with a typed O Action. ephemeral Tasks remain permitted; no persisted Plan Atom is invented. this Concern does **not** establish global absence of an Initiative definition.

## Inspected source Revisions

- `CA-R-1094@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-1094-PROGRAMMATIC-REQUIREMENT--bind-each-programmatic-mutation-to-one-initiative.md`; SHA-256 `b30685352da96ed54dee8e983a3731898c6d9d4aff0743a47d3f02eafc3f2320`.
- `CA-M-191@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-191-PROGRAMMATIC-METHOD--bind-one-programmatic-mutation-to-its-initiative.md`; SHA-256 `f7e29a5142f5287e6040dfea0e8c5310c7ac42ada472f6257da63f748c416b04`.
- `CA-R-1344@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1344-CORE_META_MODEL-CORE-REQUIREMENT--define-operations-content-role.md`; SHA-256 `300b0d772013aad37e26ec465f6b59279fe1f756d45643b5b91434d0d7020401`.
- `CA-R-1452@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1452-CORE_META_MODEL-CORE-REQUIREMENT--define-action.md`; SHA-256 `f6bf25fa0e9868bb29311aebc9dde8a7f42fa3b7ab8bd9a7359f3546de931ea1`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

## Commit-message consumer

D-417 carries the exact real-change **and** Journal-batch message forms. its real-change summary now follows R-1094's human instruction retained by the sealed Initiative instead of requiring a human-created Task Carrier. this correction preserves origin, deterministic navigation **and** the ban on substituting process/thread/queue parents. it does **not** define a new Initiative Entity, authorize an action **or** settle the remaining canonical Initiative carrier question.

## Additional inspected source Revisions

- `CA-D-417@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-417-TOOLS-DELIVERY--project-initiative-into-real-change-commit-messages.md`; SHA-256 `d57fb190e2c270696258cb7f530c51c6af71a1f873cc8bf9c02d3fe33dabd408`.
- `CA-R-1094@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-1094-PROGRAMMATIC-REQUIREMENT--bind-each-programmatic-mutation-to-one-initiative.md`; SHA-256 `b83d759f0554f7322fb756384b39719dbfde0d6fb5773b31aabf2addcd810527`.
