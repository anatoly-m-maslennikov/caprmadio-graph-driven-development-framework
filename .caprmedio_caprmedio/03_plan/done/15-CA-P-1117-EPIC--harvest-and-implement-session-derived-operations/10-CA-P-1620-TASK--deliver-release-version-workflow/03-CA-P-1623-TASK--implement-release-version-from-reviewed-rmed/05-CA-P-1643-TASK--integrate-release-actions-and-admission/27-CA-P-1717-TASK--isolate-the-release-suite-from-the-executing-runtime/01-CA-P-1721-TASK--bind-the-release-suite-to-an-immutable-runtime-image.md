---
atom_id: CA-P-1721
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-05 16:49:29 +0000"
subjects:
  governs: "Release suite sandbox executor"
  depends_on: [Implementation, Operator, Journal, Manifest, Evaluation]
relations:
  is_decomposition_of: [CA-P-1717]
  blocks: [CA-P-1624]
---
# Summary

Bind the Release suite to an immutable runtime image

## Objective

Connect the complete sealed Release suite to a governed isolated executor using the already installed immutable runtime N.

## Details

1. implement the narrow sandbox executor in `release_suite_execution.py` using current CA-R-1879, CA-E-574 and the private selected Release image-executor boundary.
2. verify the installed N image and package binding. Mount only sealed candidate workspace read-only and a separate writable output carrier; canonical sources, selector, public ca, settings, Journal, host credentials and Docker socket are not suite inputs.
3. execute the exact sealed argv and working directory with truthful process, timeout and report observations. Preserve the full declared suite and coverage, not a smaller fixture-only substitute.
4. wire the executor into the private `run_tests` phase without global fallback or caller-selected images. Test exact immutable binding, unsafe mounts and unavailable evidence with bounded mocks; actual Docker proof remains required and may be blocked.

The bounded next implementation/review leaf is estimated at <=15 minutes. Decompose before exceeding that bound. Independent API authoring may proceed in parallel; dependent tests and acceptance wait for the current helper implementations. Root owns integration, accepted authority and Git.

## Current frontier

`release_suite_execution.py` passed **9** focused adapter cases, including the sealed command, image-entrypoint override, mount escape rejection, path ancestry rejection, and truthful timeout handling. The immutable-image bootstrap passed **2** checks and the generic suite boundary passed **2** checks.

The real retained-suite path remains blocked before executor invocation: `release_compilation.py:313` raises `EPERM` at `os.replace`. An earlier Action O174 `deliver_sources` rename also received `EPERM`. No installed-N Docker execution or complete declared-suite result is claimed until those gates allow the real run.

## Definition of Done

The production executor and private phase wiring are independently accepted, focused boundary tests pass, and the complete suite has actual installed-N execution evidence before the parent Release gate closes. Mock-only or unavailable execution is not Done.

## Pre-execution review

Root accepts this bounded decomposition of the parent's existing source requirements. It adds no selected Workflow or execution permission, preserves the required full behavior, and does not execute the Operator-deferred final all-Workflow audit.
