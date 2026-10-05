---
atom_id: CA-O-119
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 01:12:38 +0400"
subjects:
  governs: "RMED Atom Review Workflow/coverage/Step: 119"
  depends_on: [Workflow, Step, Action, Atom, Operator, Journal]
relations:
  relates_to: [CA-O-104, CA-O-118]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/RMED_ATOM_REVIEW/CA-O-119-CORE_META_MODEL-STEP--gate-gather-result-coverage.md
  source_atom_id: CA-O-119
  source_atom_revision: 1
  source_sha256: 4f9f072eb47d4c3536a86d6edbf634a18c177136a3c9e560c944d642c0543a67
  original_relations_sha256: bf71386ada6c23487fc05e9498120de59784b00f41060c7bbc43ad9070f682e0
---
# Summary

Gate gather result coverage

## Operation

the gather Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=gather **after** the main gather Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
