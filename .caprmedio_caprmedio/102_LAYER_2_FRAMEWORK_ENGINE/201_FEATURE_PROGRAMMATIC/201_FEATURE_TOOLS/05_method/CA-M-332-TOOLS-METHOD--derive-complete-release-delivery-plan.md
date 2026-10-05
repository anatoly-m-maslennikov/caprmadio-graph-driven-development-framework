---
atom_id: CA-M-332
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Delivery-plan construction"
  depends_on: [Tool, Manifest, Methodology, Projection, Skill, Image]
relations:
  method_for: [CA-R-1877, CA-R-1878, CA-R-1879]
---
# Summary

Derive one complete release delivery plan

## Scope

Pure derivation of the candidate's source, compilation, runtime, Skill, test, image, and rollback bindings.

## Claim

The Tool derives one ordered delivery plan from the sealed manifest: derived source copy and compilation, package preparation, full-suite gate, separately retained N+1 installation, actual candidate-image build/execution, then promotion and delayed exact retirement. It preserves N as active rollback selection and reports any absent reviewed path or unsupported existing interface as a blocker rather than synthesizing a destination or fallback.

## Details

The plan binds existing compiler and installer interfaces only where their actual declared surface fits and keeps active runtime/Skill exposure at N until every promotion gate passes. It does not execute a compiler, installer, Docker command, Skill copy, test suite, or image operation.
