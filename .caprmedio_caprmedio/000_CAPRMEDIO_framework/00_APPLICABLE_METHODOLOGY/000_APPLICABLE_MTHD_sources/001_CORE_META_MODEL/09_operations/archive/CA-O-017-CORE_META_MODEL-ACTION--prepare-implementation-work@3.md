---
atom_id: CA-O-017
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Implementation Preparation"
  depends_on:
    - "Action"
    - "Spec"
    - "Projection"
    - "Atom"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "AI Agent"
    - "Operator"
    - "Dependency Order Derivation"
    - "Scope Unit"
version: 3
updated_at: "2026-09-24 17:18:07 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-M-239
    - CA-M-266
    - CA-M-306
    - CA-R-1589
    - CA-R-1592
    - CA-R-1599
    - CA-R-1591
    - CA-D-481
    - CA-R-1525
---
# Summary

Prepare implementation work

## Claim

Implementation Preparation **means** the Agentic Action that resolves an implementation request into persistent Plan work **and** the next prerequisite-ready item.

### Inputs

- receive the bounded implementation request, an existing P/Plan Atom **when** supplied, a source-bound Projection of **all** active Method Atoms **in** the declared input universe, the selected active Requirement, Evaluation, **and** Delivery Atoms **to** realize, the selected implementation mode, complete execution inputs, retained work, candidate-specific evidence, **and** applicable permissions.
- bind exact source identities/Revisions **and** check Projection completeness **and** freshness. the Projection is input context, **not** a second source of Method authority; apply **all** Methods governing the selected work **without** treating unrelated Methods as applicable merely because they are present.
- include applicable higher-tier authority, current Project Principles, concrete input/output boundaries, **and** test commands **or** enough admitted information **to** establish them. incomplete **or** conflicting authority returns blocked, **not** guessed scope.

### Plan preparation and selection

- reuse the supplied Plan **and** existing suitable decomposition. **when** no Plan was supplied, create the admitted P/Plan for the bounded request **before** code work starts. Tasks **and** subtasks are P/Plan Atoms with their own Claims, Assignees, **and** Definitions of Done, **not** Workflow Steps **or** an ephemeral checklist.
- **when** practical, decompose work into independently verifiable P Atoms with an ETA **<15** minutes for one assigned AI Agent. record the estimate **and** its assumptions **in** Plan Details; it is an estimate, **not** an automatic time limit. **if** safe decomposition cannot meet the applicable leaf-work bound, return the specific blocker rather than inventing small estimates **or** weakening the Definition of Done.
- store `IS_DECOMPOSITION_OF` **only** on the child Plan **and** actual start prerequisites through `BLOCKS`, following CA-M-306 **and** CA-D-481. preserve an acyclic combined completion graph under CA-R-1592. navigation order is **not** a dependency.
- select **=1** ready bounded Plan item **and** its assigned subagent context for test, implementation, diagnosis, **and** repair work. provide source-bound inputs, owned files/work boundary, expected outputs, verification, relevant prior results, **and** effective confidence/retry gates; preserve unrelated work.
- derive prerequisite-first work order under CA-M-239. prepare tests **before** the behavior they check wherever actual prerequisites permit; execute the prepared baseline tests **before** implementing that behavior **when** runnable. minimum execution prerequisites are explicit, **not** permission **to** implement the entire feature first. use Atom ID **only** **to** break remaining ties between ready work items.
- unchanged implementation mode, governing RMED, **and** complete execution inputs **must** yield the same applicable work **and** prerequisite-respecting order. retained results determine residual work, **not** a different normative interpretation.
- retain completed work **and** candidate-specific evidence. a new Method activation **or** other authorized authority change requires refreshed Projection inputs **and** renewed work/Evaluation resolution; it does **not** erase prior effects **or** reset retry accounting.

### Results and execution boundary

- return `evaluation_ready`, `requirement_ready`, **or** `evaluation_runnable` with the selected Plan, exact work, prerequisites, assigned context, **and** current baseline.
- return `complete` **only** after **all** selected implementation Plan work, required child Plans, Definitions of Done, **and** applicable Evaluations are satisfied, with no failed, blocked, stale, **or** unevaluated implementation obligations. return retained issue/diagnosis/fix evidence for separate Method learning; creating **or** accepting a Method is **not** a completion condition **or** a next Step **in** this Run.
- return `blocked` for unmet authority, capability, confidence, permission, prerequisite, **or** Plan admission, including nonempty residual work with no ready next item.
- current execution uses the host's native subagent, file, **and** command capabilities. MCP **or** a running Workflow server is **not** required. missing subagent capability blocks delegated work rather than silently executing it **in** the main session. Step bindings own the Integrated/Isolated choice; do **not** introduce a Workflow-wide context Property.
