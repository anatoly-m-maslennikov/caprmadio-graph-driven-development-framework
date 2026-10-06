---
atom_id: CA-C-495
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 05:55:36 +0000"
subjects:
  governs: "Bootstrap proof metadata accounting"
  depends_on: [Carrier, Manifest, Implementation, Evaluation, Workflow Run]
relations:
  concern_about: [CA-P-1779]
---
# Summary

Align bootstrap proof metadata accounting

## Concern

The retained bootstrap context readers count ephemeral Finder metadata as persistent proof content, unlike the governing inventory selection.

## Evidences

N7 completed delivery and compilation, then stopped at `closed_unit_gate` with `release-suite-executor-n-unproven`. Direct read-only reopening reports changed canonical bootstrap proof bytes. Excluding the five `.DS_Store` files restores the exact retained context digest; the actual immutable image and labels still match N. No Unit tests or promotion occurred in N7.

## Blast radius

Frozen N authentication and every later Release gate using that retained image proof.

## Resolution

CA-P-1779 aligns both readers with existing ephemeral selection after unsafe and secret refusal. Thirteen focused tests pass and actual retained-N proof reopening succeeds without mutation. N7 remains recorded interruption evidence with no pending events; fresh Release execution is still required.
