---
atom_id: CA-P-1779
content_role: Plan
type: Plan
label: Task
work_sequence_number: 28
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 1
updated_at: "2026-10-06 05:55:36 +0000"
subjects:
  governs: "Retained bootstrap proof metadata accounting"
  depends_on: [Implementation, Evaluation, Carrier, Manifest, Workflow Run]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1717, CA-P-1721]
---
# Summary

Repair retained bootstrap proof metadata accounting

## Objective

Restore exact persistent-inventory verification of the retained bootstrap image proof while preserving installed N and all proof bytes.

## Details

Use the existing inventory-defined ephemeral exclusion only after unsafe-carrier and secret-path refusal. Preserve exact persistent contents, modes and extra-file rejection in both context digest and package-context readers. Do not alter N, rewrite its evidence or replay N7. This bounded repair reuses current inventory authority and the Operator's instruction to ignore Finder metadata; it adds no Workflow or independent registry.

## Definition of Done

Metadata-only retained proof reopening succeeds without mutation; secret-shaped ephemeral files and arbitrary extra persistent files still refuse; focused regressions pass. Fresh actual Release gates remain separate.

## Results

N7 stopped before the Unit suite because five Finder files changed its raw retained proof-context digest. Excluding those files recovers the exact already-recorded digest. Both readers now share unsafe → secret refusal → ephemeral exclusion ordering. Thirteen bootstrap-image tests pass, including preserved metadata, `.env.pyc` refusal and arbitrary extra-file refusal. The actual retained N proof reopens as verified with the unchanged N manifest and immutable image. No N or proof files were modified.
