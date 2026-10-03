---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Project/Implementation/refactoring verification"
  depends_on:
    - "Process"
    - "Action"
    - "Implementation Process"
    - "Spec"
    - "Atom/Content Role: Evaluation"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-17 14:56:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Actions compose refactoring verification?

which existing **or** necessary new Actions define the refactoring-verification flow currently held by M-270, **without** duplicating the Implementation Process?

## Evidence

M-270 prepares applicable regression **and** end-to-end checks, captures controlled baseline evidence, evaluates a refactored candidate, **and** applies release **and** conditional canary gates. its steps cross preparation **and** later candidate execution. O-016 already owns the implementation loop; O-017 prepares implementation work; O-020 executes applicable Evaluations; O-061 owns governing-change authorization. the existing baseline is comparison evidence, **not** missing specification **and** **not** a prerequisite for fresh reconstruction.

## Principle check

CA-M-002 requires reuse of existing Actions; CA-M-005 rejects invented intermediate nodes with no independent job; CA-M-006 requires the flow **to** preserve its before/after boundaries; CA-M-261 requires reconstruction from governing RMED rather than recovered code. R-1344 assigns operational behavior **to** O, R-1452 requires a justified Action boundary, **and** R-1453 requires explicitly bound Action nodes for a Process.

## Disposition

preserve M-270 until a lossless Action/Process mapping is established. do **not** merely relabel the numbered list as a Process with unbound nodes, duplicate O-016's loop, require canaries universally, convert existing defects into Requirements, **or** make baseline capture mandatory for fresh reconstruction. reusable process authority belongs with the methodology; this question does **not** preserve Project ownership as the desired final state.

## Inspected source Revisions

- `CA-M-270` Version 8: `.caprmedio_caprmedio/05_method/CA-M-270-CORE-METHOD--prepare-verification-before-refactoring.md`; SHA-256 `a0b732bb8686603d72f8a1f1914b297353b9c6510a9e50fe65404b41831e8070`.
- `CA-O-016` Version 4: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-016-CORE_META_MODEL-CORE-PROCESS--implement-evaluations-before-required-behavior.md`; SHA-256 `e4d669b3b67c501873a26a33c1bd9961edbf1445a62cb639ff2fd09facc75579`.
- `CA-O-017` Version 1: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-017-CORE_META_MODEL-ACTION--prepare-implementation-work.md`; SHA-256 `61d963bb2f34d2fe3cfb271ef6ba18b06493a6335655d9370020339e535c9e6f`.
- `CA-O-020` Version 1: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-020-CORE_META_MODEL-ACTION--run-implementation-evaluations.md`; SHA-256 `afd792da79983f52881e2c41d4822d3d4e636b1a9d81235fc05c88ff29edbb58`.
- `CA-O-061` Version 1: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-061-CORE_META_MODEL-GENERAL-ACTOR--gate-governing-atom-changes-during-implementation.md`; SHA-256 `5f20f7f0fa0d96addd88dc4011b6ffdb8ab094e8d2d1a0eab6c1ec972683585a`.
- `CA-E-442` Version 5: `.caprmedio_caprmedio/06_evaluation/CA-E-442-CORE-EVAL_APPROACH--evaluate-refactoring-verification-readiness.md`; SHA-256 `91d0725932973d32d3b1b4967eb9e7a2d5c6e57ca32cc4f977defa447f4fcea6`.
