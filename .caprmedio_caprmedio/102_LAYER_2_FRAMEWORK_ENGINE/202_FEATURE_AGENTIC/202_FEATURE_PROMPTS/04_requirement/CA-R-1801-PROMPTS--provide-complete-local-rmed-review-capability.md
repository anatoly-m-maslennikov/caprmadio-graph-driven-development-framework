---
atom_id: "CA-R-1801"
content_role: "Requirement"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-03 06:25:11 +0400"
subjects:
  governs: "Prompt"
  depends_on:
    - "Atom"
    - "Property"
    - "Scope"
    - "Atom/Claim"
    - "Atom/Details"
    - "Atom/Summary"
    - "CCE"
    - "Action"
    - "Step"
    - "Workflow"
    - "Implementation"
relations:
  relates_to:
    - CA-E-520
    - CA-O-104
    - CA-O-105
    - CA-O-106
    - CA-O-111
---
# Summary

Provide complete local RMED review capability

## Scope

the prompt Implementation of RMED Atoms Base Revise delivered by PROMPTS.

## Claim

the prompt Implementation **must** provide complete local RMED review capability under the admitted methodology checklist **and** Action definitions, including assessment of readable content whose Carrier layout is defective.

## Details

- the supported checklist is defined by CA-E-520-CORE_META_MODEL-EVALUATION_APPROACH--check-rmed-atom-coherence; the Implementation preserves its **`=6`** local check boundaries.
- malformed headings remain Properties defects. readable applicability, contribution, supporting text, **and** Summary remain assessable using their actual source passages.
- this is implementation authority for the capability, **not** another definition of the Workflow. CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch owns the Workflow; its referenced Actions own selection, checking, **and** correction.
- the capability preserves the admitted local-review boundary. it does **not** require cross-Atom comparison **or** an Entity-graph audit.
