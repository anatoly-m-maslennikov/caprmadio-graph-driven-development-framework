---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Project Configuration"
    - "Methodology"
    - "Core Meta-Model"
priority: medium
version: 1
updated_at: "2026-09-17 18:10:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Is the software-development default an instance choice or a product promise?

does METHODOLOGY-REQU-492 select the current Framework Instance's discipline, declare a configurable product default, **or** preserve an obsolete restriction that should be retired?

## Evidence

REQU-492 says CAPRMEDIO defaults **to** software application development while Extensions **and** Project Adaptations permit other disciplines. CA-R-1425 requires a project-independent Core usable **in** **any** Project. CA-R-1207 separates expansion rules/defaults from current Settings selections; the old adaptation family remains unresolved **in** C-142. moving REQU-492 into Settings would select a value, whereas moving it into Project Configuration would preserve it as a rule. those are different changes.

## Principle check

CA-R-1421 requires configurability **and** extensibility; CA-M-002 requires one owner per fact; CA-M-006 requires neutral Core definitions **and** coherent selected behavior. these do **not** decide whether the software default is still intended. CA-R-1490 requires preserving a valid product promise rather than silently deleting it.

## Disposition

preserve the Claim while resolving its intended default-versus-selection contribution. do **not** invent a Settings parameter, write a selected discipline, impose a software-only Core, **or** remove the expansion permission as a shortcut.

## Inspected source Revisions

- `CAPRMEDIO-METHODOLOGY-REQU-492@6`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-492-FRAMEWORK_METHODOLOGY-REQUIREMENT--default-to-software-application-development.md`; SHA-256 `f41c4ba045e8c6266182f099308b5ad68445a316a349875fd15403bbe2296797`.
- `CA-R-1425@3`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CA-R-1425-FRAMEWORK_METHODOLOGY-REQUIREMENT--provide-modular-methodology-with-a-reusable-core.md`; SHA-256 `ef954cbbc6d7545e17b1cf056cc55c362c76958f816dce231a55230308cb8f46`.
- `CA-R-1207@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1207-CORE_META_MODEL-CORE-REQUIREMENT--separate-project-configuration-rules-from-current-settings.md`; SHA-256 `39bc32faff60c2d7f18982eea2e00a855892d9b04efdfbbd1f96c055a9cbd700`.
- `CA-C-142@1`: `.caprmedio_caprmedio/01_concern/CA-C-142-QUESTION--which-legacy-adaptation-claims-belong-to-project-configuration.md`; SHA-256 `48eb165af2a9f105916f8a99a8782618dc9c09eff6c6649100ff7b40f8c8c1d3`.
- `CA-R-1421@4`: `.caprmedio_caprmedio/04_requirement/CA-R-1421-PRINCIPLE-REQUIREMENT--keep-the-framework-configurable-and-extensible.md`; SHA-256 `01fe8927295fd8ed5b539b2dc7781ba1803a33dbd409f49b07031ac542752473`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
