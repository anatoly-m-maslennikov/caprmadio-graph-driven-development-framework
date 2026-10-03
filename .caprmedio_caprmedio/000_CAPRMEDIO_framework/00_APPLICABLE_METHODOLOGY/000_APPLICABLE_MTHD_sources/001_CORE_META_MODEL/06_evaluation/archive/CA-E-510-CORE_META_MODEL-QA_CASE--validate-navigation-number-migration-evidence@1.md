---
atom_id: CA-E-510
content_role: Evaluation
type: QA Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Reconcile Navigation Numbers"
  depends_on:
    - "Project Structure"
    - "Scope Unit"
    - "Scope Unit/Navigational Order Number"
    - "Scope Unit/Local Order"
    - "Scope Unit/Structural Level"
    - "Scope Unit/Type"
    - "Scope Unit/Label"
    - "Carrier"
    - "Directory Carrier/Numeric Prefix"
    - "Implementation Folder"
    - "Operator"
    - "Atom"
    - "Action"
    - "Evaluation"
    - "Atom/Revision"
    - "Concern"

version: 1
updated_at: "2026-09-23 15:59:19 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-O-078", "CA-R-1483", "CA-R-976", "CA-R-981", "CA-R-983", "CA-D-300", "CA-D-380", "CA-D-442", "CA-D-444", "CA-D-445"], "relates_to": ["CA-E-469"]}
---
# Summary

Validate Navigation Number Migration Evidence

## Claim

the Evaluation accepts a navigation-migration result **only** **if** it conforms **to** CA-O-078 **and** the identified Project Structure authority, preserves declared values **unless** an authorized change selects replacements, **and** distinguishes a ready candidate from unresolved **or** failed preparation.

### Inputs and evidence

- the exact checked authority Revisions, selected before-state, accepted Scope Unit inventory, source-layout rules, Carrier observations, creation-order evidence, **and** Operator selections.
- the Action result, candidate bytes, per-unit value evidence, mismatch dispositions, **and** before/after evidence for live TOML **and** Carriers. absent active declarations are represented explicitly as absent, **not** as an empty authoritative source.
- fixture inputs **and** expected outcomes derived from the checked authority; unavailable evidence leaves the affected check unresolved rather than silently passing.

### Test cases

1. an existing declaration **and** matching Carrier observations: retain the declared number.
2. an existing declaration **and** a conflicting folder prefix: preserve the declared value, report the mismatch, **and** block readiness **until** its disposition is explicit; do **not** silently adopt the folder number.
3. an explicit authorized replacement selection: propose the selected number **and** required Carrier/reference repairs, **without** changing parentage **or** structural Local Order.
4. a missing declaration with consistent numbered authority **and** Implementation Folder evidence: recover the number. use a generic `EXAMPLE` unit, **not** a concrete Project unit.
5. source names encoded with Structural Level width 1 **and** a candidate using width 2: decode the old `102_LAYER_2_EXAMPLE` as level 1, navigation 2, under the source rule. reject decoding it with candidate width 2. include multi-digit navigation values under CA-D-380.
6. an admitted unnumbered native layout: accept a supported creation-order value **or** explicit Operator selection **without** demanding a rename. missing selection **and** missing usable evidence produce a blocked result.
7. conflicting authority/Implementation Folder numbers **without** a settled disposition: report both paths **and** observed values; do **not** return ready.
8. a candidate number justified **only** by a parent's prefix, alphabetical order, **or** filesystem time: reject that unsupported justification.
9. valid duplicate navigation numbers on different units: do **not** reject them merely for equality. evaluate structural Local Order uniqueness separately under CA-E-469.
10. a result that rewrites unrelated declarations, emits duplicate structural Atoms, activates the candidate, **or** renames live folders: reject the out-of-bound effect.
11. changed source bytes, incomplete checks, **or** failed candidate output: report stale, unresolved, **or** failed evidence as applicable; do **not** claim successful preparation **or** activation.

### Acceptance and failure disposition

- **every** supported ready fixture passes **and** preserves its declared result boundary; **every** mismatched, unsupported, **or** out-of-bound fixture fails the corresponding check with the unit, path, expected/actual value, **and** evidence identified.
- a correctly reported blocked **or** failed Action result can pass its reporting check **without** making the candidate ready. an unknown observation cannot prove conformance.
- the check **must not** repair source Atoms, TOML, candidate values, **or** folders. report discrepancies as Concerns **and** request a decision **only** **when** governing authority does **not** settle the required selection.
- passing this Evaluation establishes navigation-reconciliation conformance **only**. Project Structure validation under CA-E-469 **and** cutover gates under CA-D-444 remain separate.
