---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "CCE"
    - "Operator"
    - "Artifact"
    - "Projection"
priority: medium
version: 1
updated_at: "2026-09-17 18:10:40 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Artifact language permissions exclude authoritative CCE Claims?

does METHODOLOGY-REQU-494's permission for prose **in** **any** human language cover authoritative Claims, **or** **only** Operator-facing interaction **and** non-authoritative presentation?

## Evidence

REQU-494 combines Operator interaction, Artifact prose, **and** optional language-pack presentation while preserving canonical identities **and** meanings. M-112 requires English as the base language; M-113 governs CCE Claims. M-139 governs understandable language **when** addressing the Operator, but does **not** by itself define multilingual authoritative Claims. replacing Artifact prose with Projection prose would narrow the existing promise **and** could omit other legitimate Artifact kinds.

## Principle check

CA-R-1420 requires information sufficient for informed Operator decisions; CA-M-006 requires coherent Claim language; CA-M-002 rejects independently maintained equivalent authority; CA-R-1490 preserves useful multilingual input **and** presentation. these rules distinguish communication from authority but do **not** identify the complete admitted Artifact-language boundary.

## Disposition

preserve REQU-494 **and** the English/CCE authoring rules pending an explicit boundary. do **not** treat multilingual interaction as permission **to** bypass CCE **or** create a second authoritative translation. retain canonical identity preservation **and** optional language-pack behavior when the Claim is narrowed **or** split.

## Inspected source Revisions

- `CAPRMEDIO-METHODOLOGY-REQU-494@5`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-494-FRAMEWORK_METHODOLOGY-REQUIREMENT--support-any-operator-language.md`; SHA-256 `7d3c3dd9980d9a756263597d801a4f39dd75b9478915025ae0d5e874f1b2438d`.
- `CA-M-112@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-112-CORE_META_MODEL-METHOD--use-english-as-the-project-language.md`; SHA-256 `d59bf20a9ccdc033fb973afe4fd99990ccfd109571ea1d8bc9ec550296804525`.
- `CA-M-113@12`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-113-CORE_META_MODEL-METHOD--write-claims-in-caprmedio-controlled-english.md`; SHA-256 `4177f606f3e2f647e8654569c735d2039c2904735b9f0a615144bf9892b0850d`.
- `CA-M-139@9`: `.caprmedio_caprmedio/05_method/CA-M-139-CORE-IMPL_METHOD--translate-framework-language-for-the-operator.md`; SHA-256 `26898aa85844e508d3e2f799322756212af1ac5742335ffc18f720f396dcd831`.
- `CA-R-1420@5`: `.caprmedio_caprmedio/04_requirement/CA-R-1420-PRINCIPLE-REQUIREMENT--support-informed-operator-decisions.md`; SHA-256 `816a03918b1b0198138dc44a33277bb41b08084da2b8fa38823bef2367ea7b6b`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
