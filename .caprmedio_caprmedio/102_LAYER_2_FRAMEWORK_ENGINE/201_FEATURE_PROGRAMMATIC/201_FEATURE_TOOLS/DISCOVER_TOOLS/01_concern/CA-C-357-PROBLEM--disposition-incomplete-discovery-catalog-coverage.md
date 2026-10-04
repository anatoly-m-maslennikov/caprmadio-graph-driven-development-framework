---
atom_id: CA-C-357
content_role: Concern
type: Problem
current_scope_unit: DISCOVER_TOOLS
local_tier: Standard
global_tier: 14
author: Anatoly Maslennikov
status: active
subjects:
  governs: "Tool/DISCOVER_TOOLS/catalog coverage"
  depends_on: [Tool, Atom, Operations, Implementation]
version: 1
updated_at: "2026-10-04 12:42:25 +0000"
relations:
  concern_about: [CA-R-1804, CA-P-1123]
---
# Summary

Disposition incomplete discovery catalog coverage

## Concern

The current discovery result cannot establish complete runtime capability coverage while its catalog diagnostics remain undispositioned. This is a coverage limitation, not a proved implementation defect or permission to repair unrelated historical files.

## Evidences

- Read-only MCP DISCOVER_TOOLS query `reconcil`, limit 20: zero matches and 50 coverage diagnostics.
- Read-only Operations discovery query `completed work`, limit 20: 21 total matches, next offset 20, and the same 50 diagnostics. Its broad text matches do not establish an exact completed-work Action.
- Representative diagnostics: `ambiguous Atom ID: CA-D-388`; legacy execution-evidence Markdown and a programmatic Method Projection reported as `CarrierError`.
- The actual schema distinguishes coverage diagnostics from success; a zero-match result with these diagnostics is not proof that a capability is absent. No Action or Workflow was dispatched.

## Blast radius

Nonblocking for current saved-evidence reconciliation and source authoring. The later PROGRAMMATIC/runtime inventory must classify the diagnostics against registered authoritative inputs, distinguish harmless non-Atom evidence from real identity/reader failures, and prove the complete implemented capability inventory independently where needed. Repair only a confirmed governed implementation gap; do not broaden this Epic into a legacy-document cleanup. Keep CA-P-1123's full image-based runtime coverage gate intact.
