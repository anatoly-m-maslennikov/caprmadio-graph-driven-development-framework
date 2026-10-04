---
atom_id: CA-O-123
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Evaluator Evidence Calibration"
  depends_on: [Action, Evaluation, Operator, Atom/Revision, Artifact/Revision, Implementation]
version: 1
updated_at: "2026-10-04 15:12:43 +0000"
relations:
  relates_to: [CA-O-018, CA-O-020, CA-O-104, CA-O-105, CA-O-106, CA-O-111, CA-O-118]
---
# Summary

Calibrate evaluator evidence

## Operation

Evaluator Evidence Calibration **means** the optional Agentic Action that, for an admitted calibration request, compares fresh, independently produced evaluator judgments with independently reviewed expected judgments on an exact frozen case universe **and** returns the bounded comparison evidence.

1. bind the caller's admitted purpose, Actor, permissions, evidence location **and** comparison criteria; the exact evaluator implementation/revision **and** configuration; the ordered cases with stable case/occurrence references, complete inputs **and** their revisions; applicable R/E/D **and** test bindings; **and** the expected judgments with their independent review evidence. a proposed **or** unreviewed expectation is **not** an accepted oracle. missing authority, unresolved oracle disagreement **or** unavailable setup blocks the affected comparison.
2. freeze these bindings before obtaining the actual judgments. retain original inputs/outputs **and** supplied, authorized corrected inputs/outputs as separate identified evidence; a correction does **not** silently replace the original case, output **or** expected judgment. reuse CA-O-018 for admitted test preparation **and** CA-O-020 for actual selected check execution. retain fresh evaluator output from the bound execution, independently of the expected judgments; do **not** substitute the oracle, corrected output **or** the calibration assessment for what the evaluator actually produced.
3. compare **every** bound case **and** exact defect occurrence with the independently reviewed expectation. account for expected findings, actual findings **and** their dispositions, including misses, false positives, duplicates **and** withdrawn findings. preserve evidence references **and** reasons rather than hiding a difference by changing the oracle, dropping a case, merging distinct occurrences **or** discarding an initial finding. report mechanical/schema results separately from semantic comparison.
4. return the case-level comparison, expected/actual evidence, complete/missing coverage, observed differences, setup/authority/currentness blockers **and** the outcome below. a complete matched comparison supports **only** its bound evaluator/configuration, inputs, oracle **and** criteria. retain partial evidence **and** the exact unresolved case, binding **or** decision for a caller handoff; do **not** claim the unfinished portion passed.

## Details

### Outcomes and currentness

| Condition | Returned outcome and evidence |
| --- | --- |
| complete, current actual evidence agrees with the independently reviewed expectations under the admitted criteria, with every case/occurrence and finding disposition accounted for | `matched`, with the exact bindings and case-level comparison; bounded semantic calibration evidence, not a universal evaluator pass |
| complete current evidence differs from the reviewed expectations under the admitted comparison criteria, including a seeded defect missed despite schema-valid output, an invented finding, an unsupported duplicate or an incorrectly withdrawn finding | `mismatch`, retaining the exact expected/actual occurrences and dispositions; explaining a difference or obtaining mechanical success does not make this calibrated |
| actual evidence or required case/occurrence coverage is missing, pending or unknown | `incomplete`, with completed comparisons and the exact missing evidence; no certification of the missing portion |
| the independent oracle is missing, unreviewed or disputed; applicable authority, permission, setup or trustworthy execution evidence is unavailable | `blocked`, retaining available evidence and the required admitted resolution; the executor does not settle truth or invent permission to obtain a pass |
| evaluator, configuration, case inputs, oracle, criteria or applicable authority no longer matches the frozen execution/comparison binding | `blocked` for current calibration, with the binding mismatch; earlier evidence remains historical evidence for its original binding, not a current result |

An execution failure retains its actual failure evidence **and** incomplete coverage, **without** diagnosing an evaluator defect from a failed command alone. a changed binding requires a separately admitted continuation **or** new request; this Action does **not** automatically rerun, repair **or** certify the changed candidate. unresolved oracle disagreement remains blocked **until** an admitted decision resolves the affected expectation; preserve the earlier judgment **and** the decision rather than silently rewriting it.

### Actor, reuse and authority boundary

The caller supplies the authorized executor, independently reviewed oracle **and** evidence handoff location. the executor records actual comparisons **and** blockers; unresolved authority **or** oracle decisions return **to** the caller/Operator through the admitted decision route. neither the tested evaluator's assertion **nor** the comparison report replaces governing authority. any supplied corrected case remains distinguishable from its original **and** must have its own expected/actual binding.

Separately requested local Atom selection/review reuses CA-O-105/CA-O-106. CA-O-118 checks accounting, **not** semantic correctness; its coverage result **and** an implementation/schema test pass are **not** substitutes for this comparison. CA-O-104/CA-O-111 retain their existing no-automatic-saved-Atom-recheck boundaries. this Action adds no Workflow **or** Step **to** Base Revise **and** does **not** invoke local review merely because calibration was requested.

No fixed sample size, twenty-case rule, default discrepancy threshold **or** universal calibration gate is imposed. the admitted request determines the exact case universe **and** criteria; a complete result over that universe makes no unperformed wider-coverage claim. matched **or** mismatched evidence grants no source correction, automatic repair, rollout, adoption, new source of truth, mandatory post-fix recheck **or** expansion beyond the admitted request.
