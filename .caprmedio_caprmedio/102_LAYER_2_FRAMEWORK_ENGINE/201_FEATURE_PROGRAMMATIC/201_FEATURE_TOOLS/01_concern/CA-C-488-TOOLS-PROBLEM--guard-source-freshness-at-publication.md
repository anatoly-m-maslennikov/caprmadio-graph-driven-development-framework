---
atom_id: CA-C-488
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Guard source freshness at publication"
  depends_on: [Tool, Implementation, Evaluation, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1761]
---
# Summary

Guard source freshness at publication

## Concern

The compiler's staging check precedes live output replacement; changed sources can be detected only after the replacement.

## Evidences

At commit `c011b68fa`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py:1202-1204` replaces before its final freshness check. Regression: `COMPILE_APPLICABLE_METHODOLOGY/tests/test_selected_compilation.py`; CA-O-009 supplies the publication boundary.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Revalidate at the publication boundary and prove a detected pre-publication change leaves output unchanged. Report any actual post-effect state truthfully.

CA-P-1761 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
