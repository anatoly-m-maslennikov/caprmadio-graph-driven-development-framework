---
atom_id: "CA-R-1802"
content_role: "Requirement"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: Archived
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-03 06:25:11 +0400"
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Atom"
    - "Evaluation"
    - "Prompt"
    - "Property"
    - "Implementation"
relations:
  relates_to:
    - CA-O-104
    - CA-O-111
    - CA-R-1801
---
# Summary

Keep review completion separate from applied edits

## Scope

completion results produced by the RMED review prompt Implementation for a selected Atom **or** selection.

## Claim

the Implementation **must** report completion **only** from complete initial check coverage **and** resolved findings, rather than from the existence of a report **or** an applied edit.

## Details

- an initial failed check is a completed check with a finding; a blocked **or** unperformed check is incomplete coverage.
- confirmed findings are resolved by an authorized correction **or** a recorded rejection supported by the supplied rules. partial correction does **not** resolve remaining findings **or** coverage.
- a completed selection requires completion evidence for **every** selected Atom. independent completed Atoms remain distinguishable from the unfinished selection.
- completion after fixes records completion of the admitted one-pass work, **not** a claim that saved output passed another Evaluation. this specification adds no recheck Step.

