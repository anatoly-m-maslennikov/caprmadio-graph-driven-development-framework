---
atom_id: CA-P-1683
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
status: Done
subjects:
  governs: "Implement Draft history primitives"
  depends_on: [Atom, Carrier, History, Runtime, Tool, Evaluation]
version: 1
updated_at: "2026-10-05 06:14:04 +0000"
relations:
  is_decomposition_of: [CA-P-1677]
  blocks: [CA-P-1684]
---
# Summary

Implement Draft history primitives

## Objective

Within <=15 minutes, implement Draft history primitives.

## Details

Own only new draft_history.py and tests/test_draft_history.py. Golden first. Implement safe pre-addressable retained-history references, immutable append-only Draft entries, exact output path/digest validation, unique live-head enumeration, acyclic direct parents, inherited original origin, and finalized promotion successor publication after exact output observation. Reuse existing archive/Project-control bindings, not an identity registry or second Journal. No native lifecycle wiring or source edits. Return the small explicit API before dependent integration.

Inputs: accepted D568@5 64d2e60303d9dceeaee694263ebd888daf4bd217a794830896b1c5837517559d, D570@4 462ff2638fdba7050c83c27c9a8f974c1008c431cb46b4d8d81212d207ea1f37 and D569@5 ada92dcacfcf906878e3c3e3964281abd8e9c8b99336042564d565d2a79dd523. One Task, one Agent; preserve others. No source/Plans/Git/runtime/image writes or permission workaround. Existing development worker focused tests only, not immutable-image proof. Choose best authorized options; record C/Question and continue. If work cannot fit fifteen minutes, save exact partial frontier and bounded remainder.

## Definition of Done

Save exact code/test hashes, concrete API, genuine focused evidence and remaining coverage. Partial results do not close the parent or mandatory runtime gates.

## Result

Implemented draft_history.py SHA-256 c4aa0a9b2bae88a9e80fefae44472bf3af9c2c533e95d28b3e6e5ad25d1a02d3 and tests/test_draft_history.py 359ab00de57c733e79b296191c3474d80809eeafce7b8053f7b88669cc5c9ecf. Existing development worker passed7 focused cases. The initial five-case result missed inherited demoted-update schema, actual predecessor metadata/digest verification, unsafe reservation parents and identified-output checks; those precise defects are repaired and actual positive/refusal cases added. Public API: reserve_history_entry, append_draft_entry, validate_current_draft_head, append_promotion_successor. Trusted retained entries bind the exact current Draft, direct origin/parents and unique head; observed identified output alone permits a consuming successor. Private pending recovery and native lifecycle wiring remain P1684/P1685, not completed by this helper corpus.

### Current review disposition

Reopened after independent helper review REJECT at98%. Concurrent finalizers created two consuming successors; terminal-receipt recovery failed after old-Draft removal. Initial focused passes remain historical, not current acceptance. C462 and P1690 bind the repair and regression proof before native integration can close.

### Current completed result

Eight history cases now pass, including forced forked consumption. Current draft_history.py `b6cda4302807a1ac7c1cbc79aecc12878559a2d65745d4e83e7fcd17491cb6d2` and tests `a83dce6c09ee30e1a68d19222a64651aa561b3a522cba5e711c3e527efc01a0d` are independently ACCEPT at97% through P1690. Per-head process locking makes exact successor match, head validation and publication one consuming critical section. Native integration remains separate.
