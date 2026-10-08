---
atom_id: CA-P-1568
content_role: Plan
type: Plan
label: Task
work_sequence_number: 30
current_scope_unit: caprmedio
claim_target_scope_unit: REVERT_CHANGES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Native Revert current evidence validation"
  depends_on: [Workflow, Action, Operator, Journal, Implementation, Evaluation]
version: 3
updated_at: "2026-10-04 23:52:49 +0000"
relations:
  is_decomposition_of: [CA-P-1513]
  blocks: [CA-P-1513, CA-P-1567, CA-P-1519]
---
# Summary

Revalidate native Revert evidence before effects

## Objective

Within <=15 minutes, repair P1566's confirmed evidence-currentness defect against existing R1833/D536/E553/E554.

## Details

- Own native_revert_provider.py and its focused tests under WORKFLOW_OPERATIONS/REVERT_CHANGES; add a narrow evidence reader if necessary. Update only directly affected selected-native-provider tests in coordination with root. Own no fixture, shared executor, backend, MCP, source, Journal or Plan files.
- Resolve the admitted references against actual bounded, safe Project authority/evidence. At admission, before execution and before each effect, verify current permission, exact Operator decision, selected-change/history and affected-reference/governing-definition bindings. A frozen packet, valid hash shape or arbitrary approval-shaped string is not current evidence.
- Reuse the canonical Journal reader for Event references and existing declared artifact carriers where applicable. No arbitrary URLs, code, generic file mutations, second Journal, fallback authority, synthesized evidence or caller-supplied executable resolver. Reject unsupported, missing, unsafe, changed or revoked bindings precisely before effects.
- Preserve the existing complete request and capability boundaries. If accepted source cannot represent a required reference/hash, report that exact source gap to root; do not invent an ungoverned schema or weaken validation to make a fixture pass.
- Functional disposable regressions prove post-admission revocation/change blocks before Action start/effects; valid current evidence still admits the exact supported native capability. Coordinate the actual accepted evidence input interface with P1567's fixture worker.
- Use apply_patch, preserve everyone, no commits/Plan/Journal changes. Inherit 90% confidence, no FPF, harvesting or live Project mutation. Root records the result and any explicit source remainder.

## Saved result

P1574 completed independently accepted D536@2 actual evidence protocol; P1581 native provider review ACCEPT and 24/24 Revert tests plus registered selected native Revert proof passed. The earlier source gaps are closed for this bounded provider slice. Full W10 route, queue/MCP and immutable image proof remain separate gates.

The confirmed currentness defect is repaired with saved evidence and bounded regressions, or the precise source prerequisite is retained unfinished without unauthorized effects.

## Saved partial result

## Definition of Done

Actual capability permission JSON, raw-byte hashes and affected member/canonical Event evidence are now re-observed at admission/pre-execution/per-effect. Unsafe, symlink, secret, missing, oversized and duplicate-JSON records are refused. The native provider suite passed 8/8, selected-provider suite 6/6 and underlying Revert service 11/11; compile/diff checks passed. Former synthetic happy cases now correctly assert blocked. Full native admission remains unfinished until P1574 implements independently accepted D536@2's governing-definition, Operator-decision and executor-permission pins. No queue, image, new authority or real Project effect is claimed.
