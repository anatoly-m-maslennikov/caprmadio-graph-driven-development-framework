---
atom_id: CA-P-1470
content_role: Plan
type: Plan
label: Task
work_sequence_number: 37
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on: [Workflow, Step, Action]
version: 1
updated_at: "2026-10-04 17:44:59 +0000"
relations:
  is_decomposition_of: [CA-P-1132]
  blocks: [CA-P-1132, CA-P-1158, CA-P-1160]
---
# Summary

Bind Agentic context for selected Workflow Steps

## Objective

Repair the admitted Agentic execution-context input binding under R1527v4 for only O139–144, O146–151 and O152–157. These eighteen selected structural/reconciliation/compilation Step Atoms reuse shared Actions whose actual execution may require judgment. Read each actual binding before changes. Preserve Action identity, inputs, effects and all graph behavior. Explicitly bind an Agentic invocation's Integrated/Isolated context to the admitted invocation's supplied runtime parameter before dispatch; missing/unsupported context blocks that Agentic dispatch. It does not apply to Programmatic Actions or invent a default/context-dependent duplicate Action.

Own only these eighteen Step carriers, whole prior semantic revisions, this Plan and narrow C426. Keep Summaries/IDs fixed; increment meaningful Versions and actual timestamps. Graph Workflows are independently reviewed elsewhere; do not edit them or shared Actions. Record exact changed clauses and one saved comparison/scenario gate; <=15-minute estimate. You are not alone: preserve other work. No code, Git, Journal, FPF or harvest. Independent review slices of <=4 changed Steps are required afterward.

## Details

### Authoring completion

First actual clock: 2026-10-04 17:36:51 UTC. Whole selected carriers and R1527v4 were read before editing. Source save: 2026-10-04 17:42:12 UTC; saved comparison and functional clause walkthrough passed at 17:42:53 UTC. This leaf closes authoring only; C426 remains Active for the required independent source reviews of <=4 changed Steps per slice.

All eighteen selected sources are Active v2, with unchanged IDs, Summaries, Action bindings, input clauses, results, authority/approval/retry guards and graph behavior outside the context clauses below. Source paths remain in the CORE_META_MODEL `09_operations` tree: O139–144 directly there; O146–151 in `SOURCE_RECONCILIATION`; O152–157 in `APPLICABLE_METHODOLOGY_COMPILATION`. Each exact prior source is saved beside its current carrier as `archive/<same-stem>@1.md`: Version 1, full prior body/meaning/identity retained, status explicitly Archived, and actual Updated At 17:42:12 UTC. The prior lifecycle fields are intentionally not an original-byte claim.

Exact changed clauses:

- O139–144 replace the paragraph beginning “An Agentic invocation uses Integrated context under CA-R-1527” with:

> For an invocation whose actual bound Action is Agentic, bind **=1** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. Missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. A Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

- O146–151 replace the bullet beginning “for an Agentic invocation, use Integrated context” with:

> for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under `CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context` from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, return a blocked Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. this does **not** grant additional authority. a Programmatic invocation does **not** acquire an Agent context.

- O152–157 add only the supporting `### Agentic invocation binding` subsection before Details, with this exact paragraph:

> for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

One bounded saved gate compared all eighteen current carriers against their captured pre-edit texts and all eighteen complete prior revisions. PASS: exact planned deltas; unchanged Summary, identity and other metadata; strict duplicate-free Operations/Step carriers with explicit CORE target, required heading order, no trailing whitespace and one EOF newline. The current input source is the admitted invocation's supplied `agentic_execution_context`; no Action or Workflow was rewritten.

Clause cases: an actual Agentic bound Action with one supplied Integrated value or one supplied Isolated value resolves that value before dispatch when its required context/capability is available. Missing, ambiguous, unsupported or unavailable context/capability blocks that Agentic invocation, without default/substitution. Programmatic Actions gain no Agent context and retain their existing input/dispatch behavior. Selected Agentic context is retained with the Step Run; this is no permission/approval grant, duplicate Action, runtime execution or runtime acceptance. P1132/P1158/P1160 gates remain unchanged.

### Definition of Done

The selected Step-owned runtime parameter is explicit and fail-closed without changing Programmatic behavior, Action definitions or graph control flow. Required histories and exact deltas are saved. Own Plan may become Done after authoring; source acceptance waits for independent review.
