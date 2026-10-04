---
atom_id: CA-A-1085
content_role: Analysis
type: Analysis Report
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Calibration and legacy preparation gap acceptance"
  depends_on: [Operations, Evaluation, Implementation, Spec, Operator]
version: 1
updated_at: "2026-10-04 14:48:57 +0000"
relations:
  analysis_for: [CA-P-1370]
  relates_to: [CA-A-1077, CA-A-1079, CA-O-017, CA-O-018, CA-O-020, CA-O-104, CA-O-105, CA-O-106, CA-O-111, CA-O-118, CA-O-006, CA-O-007, CA-O-008, CA-O-019]
---
# Summary

Review calibration and legacy preparation gaps

## Question

Do the two proposed contributions duplicate current Operations, exceed their admitted purpose, or justify minimal separate capabilities?

## Scope

The completed A1077 and A1079 proposals only. Root independently read both complete reports, their saved candidate sections in A953/A989/A1010/A1013/A1029/A1047 and A933, and the current source boundaries named below. No native harvesting, source authoring, runtime test, activation or implementation was performed. The full unchanged Project Goal/Principles and P1117v2/P1119v2/P1130v5 remain governing; threshold90%.

## Approach

Compare the promised output and admission boundary with actual current clauses, not similar titles. Apply Operator authority, checkability, DRY, necessary complexity and evidence preservation. Reuse established sub-capabilities; retain a separate Action only for a distinct outcome that existing definitions do not supply. Historical requests and reports clarify intent but do not prove current implementation.

## Results

### Evaluator calibration: accepted, narrowly

A1077's optional evaluator-calibration contribution is distinct from test preparation, check execution and accounting.

- O018v6 prepares tests from admitted R/E/D; it does not review proposed evaluator judgments as an oracle.
- O020v5 runs selected checks and preserves candidate/input/baseline evidence; it does not define expected-versus-actual semantic calibration.
- O105v5 freezes local Atom selection; O106v8 performs atom-local review and rejects unsupported diagnoses.
- O118v1 expressly checks accounting, not semantic correctness. O104v9 and O111v5 expressly exclude an automatic saved-Atom recheck.

Accept one CORE_META_MODEL Action that, for an admitted calibration request, compares fresh evaluator judgments with independently reviewed expected judgments on exact frozen cases. Retain original/corrected input and output evidence, exact defect occurrences, misses, false positives, duplicates, withdrawn findings, incomplete coverage and authority/setup blockers. Distinguish mechanical/schema test passes from semantic results. Reuse O018/O020 and separately requested O105/O106 work; do not copy their behavior or add a Step to Base Revise.

Narrow the proposal: no fixed sample size, mandatory recheck, automatic broad rollout, new source of truth, or universal gate for every review. A calibration result supports only its bound evaluator/configuration/input universe. Oracle disagreement remains blocked until an admitted decision resolves it; an unreviewed expected result cannot certify the evaluator.

Counterexample boundary for later Evaluation: a schema-valid judgment that misses a seeded defect or invents one must not be reported as calibrated; missing oracle/actual evidence yields incomplete or blocked. A complete matched comparison is evidence, not authorization to repair or expand the scope.

### Legacy evidence preparation: accepted, narrowly

A933W2 and A1079 correctly distinguish initial legacy reconstruction from implementing already accepted authority.

- O017v6 consumes active R/D, separate E and a complete M Projection; absent authority blocks implementation.
- O019v4 realizes selected ready work without changing expected behavior or authority to obtain a pass.
- O006v6 prepares corrections for an identified conflict in an exact source frontier. It does not prepare first-time RMED from legacy observations.
- O007v6/O008v11 obtain/revalidate actual decisions for their correction domain. They are not blanket permission to activate observed behavior.

Accept one CORE_META_MODEL Action that prepares a bounded legacy-evidence and provisional-RMED packet: exact source/window, existing or explicitly absent authority, observable behavior and provenance, inferred interpretations, unknowns, and candidate preserve/change decisions. Proposed RMED is reviewable input, never automatically accepted authority. The Action returns ready-for-review or blocked, with missing contracts explicit; it does not refactor, mutate source Claims or fabricate Journal history.

Reuse admitted authoring/decision routes and O017/O019 after accepted sources are available. Concrete legacy paths, extraction adapters and any graph output format belong to the selected project/Engine bindings, not this generic Action. The proposal's mandatory graph faces/value schemas are not adopted.

Counterexample boundary for later Evaluation: an isolated legacy fixture with no initial RMED/Journal returns traceable provisional observations and unknowns rather than invented active authority/history. Refactoring remains blocked until the governing inputs are actually admitted. Downstream behavior equivalence must be tested separately from preparation.

### Destination, gates and actual evidence

Both accepted contributions belong in authoritative CORE_META_MODEL/09_operations, not Applicable Methodology. Exact Atom IDs/carriers, source authoring and independent source review remain unperformed and separately bound. No source activation or runtime conformance is claimed by this Analysis.

Current source root:
.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/

The actual full reads were O017v6, O018v6, O020v5, O105v5, O106v8, O111v5, O118v1, O104v9, O006v6, O007v6, O008v11 and O019v4. The reports' legacy body-heading defects remain in their existing Concerns; semantic reuse is not carrier-conformance proof. No additional C382 adoption blocker remains. Other family gaps must still be coalesced before P1130 closes.

## TLDR

Accept two optional, narrowly bounded CORE capabilities: evaluator calibration and legacy-evidence preparation. Reuse existing test/implementation/change mechanisms; add no automatic Base Revise recheck, activation or refactoring.
