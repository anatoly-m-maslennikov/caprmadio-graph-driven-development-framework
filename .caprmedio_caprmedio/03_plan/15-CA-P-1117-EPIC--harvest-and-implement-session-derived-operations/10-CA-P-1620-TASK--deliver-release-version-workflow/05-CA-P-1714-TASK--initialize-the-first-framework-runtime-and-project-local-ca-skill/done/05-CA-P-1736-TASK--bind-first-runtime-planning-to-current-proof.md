---
atom_id: CA-P-1736
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-05 20:58:40 +0000"
subjects:
  governs: "First Framework runtime delivery/Bind first runtime planning to current proof"
  depends_on: [Implementation, Evaluation, Framework Package, Methodology, Docker Image, Journal, Skill]
relations:
  is_decomposition_of: [CA-P-1714]
---
# Summary

Bind first runtime planning to current proof

## Objective

Integrate read-only canonical compilation proof and actual bootstrap image admission into first-runtime planning and installation.

## Details

Own framework_initialization.py and, if required, one private compiler-currentness module. Use exact deterministic output comparison for a complete conflict-free frontier. Recheck proof before package/Skill/selector effects; planning/startup never compile or build. Expected bounded effort: <=15 minutes; decompose further if necessary.

## Definition of Done

The owned source or implementation is independently accepted and its real verification result is saved. Source or mock proof alone does not close actual first-install or Release gates.

## Result

Initializer binds current canonical compilation and complete-package image proof, refuses caller-controlled fresh inspectors and retained test-double authorization, and reopens inputs before package, Skill and selector effects.

Saved implementation: b790a3fd0. This is scoped source and fixture verification, not an actual complete Release or Framework installation. P1739 remains Active.
