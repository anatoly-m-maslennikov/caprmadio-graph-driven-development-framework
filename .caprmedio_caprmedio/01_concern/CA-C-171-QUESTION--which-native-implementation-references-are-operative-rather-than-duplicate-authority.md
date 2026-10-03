---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Implementation"
  depends_on:
    - "Artifact/Carrier"
    - "Atom/Content Role"
    - "Journal"
    - "Projection"
priority: medium
version: 1
updated_at: "2026-09-17 18:10:35 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which native Implementation references are operative rather than duplicate authority?

which Claims from METHODOLOGY-REQU-510/511/512 preserve the boundary between operative Implementation **and** normative authority, **without** banning references required **to** implement CAPRMEDIO itself?

## Evidence

REQU-510 excludes normative intent, rationale, **and** traceability from native Implementation. REQU-511 is a writing convention for comments **and** docstrings, which belongs **in** M. REQU-512 specifies Carrier content, which belongs **in** D, but literally bans **all** embedded Artifact identities, filenames, paths, **and** Relation metadata. a Tool that reads, resolves, **or** returns such values uses them operatively; that use is **not** necessarily a second source of authority. simply changing role letters would preserve this ambiguous blanket prohibition. the parent **and** both children also need a lossless ownership map.

## Principle check

CA-M-002 prohibits independent duplicate authority, **not** **every** reference **to** it. CA-M-006 requires Implementation **and** its rules **to** agree; CA-R-1490 protects useful rationale **and** traceability rather than discarding them. these Principles establish the distinction but do **not** identify the complete intended exclusion boundary **or** all affected native interfaces.

## Disposition

preserve the three Claims; do **not** move an overbroad prohibition unchanged into D. resolve normative restatement versus operative reference, retain Journal-owned history **and** derived traceability, map the remaining outcome, writing Method, **and** Carrier specification **to** their owners, **and** use replacement identities for role changes. no Implementation rewrite is authorized by this Concern.

## Inspected source Revisions

- `CAPRMEDIO-METHODOLOGY-REQU-510@6`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-510-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--keep-native-implementation-semantically-clean.md`; SHA-256 `b896678224ab371b38a8630ad5f540cf69382bc739f4b88e4c4b923134ba56ec`.
- `CAPRMEDIO-METHODOLOGY-REQU-511@6`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-511-FRAMEWORK_METHODOLOGY-REQUIREMENT--keep-normative-prose-outside-native-implementation.md`; SHA-256 `95cab0a1d5c6cfb90491afa5c95c6db3a4ebc03ab086af154e8f0000752eeba1`.
- `CAPRMEDIO-METHODOLOGY-REQU-512@6`: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CAPRMEDIO-METHODOLOGY-REQU-512-FRAMEWORK_METHODOLOGY-REQUIREMENT--keep-caprmedio-references-outside-native-implementation.md`; SHA-256 `ed48970307686733b2e08f696c5b62cfe09488ff7b9324a6e6bbdb08f3a15a17`.
- `CA-C-123@2`: `.caprmedio_caprmedio/01_concern/CA-C-123-QUESTION--which-required-information-belongs-to-semantic-or-carrier-authority.md`; SHA-256 `d6e0d2d2af7a16fc1745114a2ac8910faf2b122cd30d8a68e60aec296f11e385`.
- `CA-C-119@1`: `.caprmedio_caprmedio/01_concern/CA-C-119-QUESTION--how-should-atom-moves-preserve-owner-dependent-meaning.md`; SHA-256 `a86e0db234bdf6b485c421897fd282f5a765d9b67593b195f8aa0a93aec186fc`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
