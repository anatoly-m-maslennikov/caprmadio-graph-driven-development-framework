---
atom_id: CA-C-426
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 2
updated_at: "2026-10-04 18:15:44 +0000"
subjects:
  governs: "Selected Workflow Step/Agentic invocation context binding"
  depends_on: [Step, Action, Workflow Run, Step Run, "Step/Agentic Execution Context"]
relations:
  concern_about: [CA-O-139, CA-O-140, CA-O-141, CA-O-142, CA-O-143, CA-O-144, CA-O-146, CA-O-147, CA-O-148, CA-O-149, CA-O-150, CA-O-151, CA-O-152, CA-O-153, CA-O-154, CA-O-155, CA-O-156, CA-O-157, CA-P-1459, CA-P-1470]
---
# Summary

Bind Agentic context for selected Workflow Steps

## Concern

The selected v1 Steps do not bind the admitted Agentic invocation's supplied execution-context runtime parameter before dispatch: O139–144 and O146–151 default to Integrated; O152–157 omit this binding. R1527v4 requires exactly one admitted Integrated/Isolated context through the declared invocation binding, blocking missing or unsupported context rather than substituting.

## Evidences

P1459 identified the missing binding in O152–154. P1470 directly read all eighteen complete v1 Step carriers and R1527v4, confirming the same bounded defect across the selected structural/reconciliation/compilation Steps. No runtime failure or executed Run is inferred from these source definitions.

## Blast radius

### Resolution

P1470 saved all eighteen Steps as v2. Independent P1473–P1477 accepted every changed Step against R1527v4 and whole archived v1: exactly one supplied Integrated/Isolated context before actual Agentic dispatch, missing/unsupported/unavailable context blocks, Programmatic behavior unchanged, all other bindings preserved. Source context binding is resolved. This does not claim dispatched Runs or implemented context enforcement.

### Original impact

P1470 saved all eighteen sources as v2 with a conditional actual-Agentic-Action binding to supplied `agentic_execution_context`, fail-closed values/capabilities and no default. Complete v1 bodies are explicitly Archived. One exact saved comparison and functional clause walkthrough passed; all other inputs, Action identities and graph guards are preserved. C426 remains Active pending separately bound independent reviews of <=4 changed Steps; authoring completion is not source or runtime acceptance.
