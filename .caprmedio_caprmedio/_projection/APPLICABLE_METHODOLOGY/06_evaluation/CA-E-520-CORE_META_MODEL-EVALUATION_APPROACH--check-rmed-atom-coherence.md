---
atom_id: CA-E-520
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-03 06:11:33 +0400"
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Subjects"
    - "Atom/Claim"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Details"
    - "Atom/Summary"
    - "Atom/Content Role"
    - "Property"
    - "Entity"
    - "CCE"
    - "Atom/Local Tier: Principle"
    - "Operator"
    - "CAPRMEDIO Framework Instance"
    - "Workflow"
relations: {"evaluation_for":["CA-D-269","CA-D-478","CA-D-479","CA-D-495","CA-M-113","CA-M-125","CA-R-1269","CA-R-1270","CA-R-1271","CA-R-1273","CA-R-1465","CA-R-1624","CA-R-1799"]}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-520-CORE_META_MODEL-EVALUATION_APPROACH--check-rmed-atom-coherence.md
  source_atom_id: CA-E-520
  source_atom_revision: 5
  source_sha256: 9e3cdee5027c3e24cb91e1ce9fe009dc281b499a49a45aaacea38f3ff59fcada
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Check RMED Atom coherence

## Scope

individual active RMED Atoms reviewed locally against their exact carried text **and** applicable local authoring rules.

## Claim

an RMED Atom passes this local Evaluation **only** **when** **all** of these checks pass with source evidence:

| Check | Passing condition |
|---|---|
| properties | frontmatter is valid; required local Properties are present, admitted, correctly typed, **and** consistent with the body; body Properties occupy their required sections; values are **not** inferred from filenames **or** folders |
| scope | **`=1`** coherent applicability description applies throughout the contribution **and** supporting text; a composite boundary **may** describe **`=1`** Scope |
| claim | Claim expresses **`=1`** independently replaceable contribution **and** distinguishes capability requirements from authorization **to** execute; multiple clauses, conditions, **or** allowed values alone do **not** imply multiple Claims |
| details | Details explain the scoped Claim **without** adding an independent obligation, permission, exception, **or** applicability change |
| summary | Summary faithfully shortens the scoped Claim **without** changing its contribution **or** decisive boundary |
| cce | the complete Markdown follows the supplied current CCE rules, including syntax, capitalization, structure, **and** understandability |

a failed check **must** identify its local source evidence, rule, **and** proposed correction. unresolved required local evidence **must** remain a coverage gap. a pass **must** include a concrete source observation **and** the rule it satisfies. mechanical evidence does **not** prove Claim meaning.

## Details

missing, duplicate, **or** misplaced headings fail Properties; they do **not** automatically block content checks. assess the complete readable text **and** cite actual passages that establish applicability, contribution, supporting detail, **and** Summary. this interpretation is review evidence, **not** a declaration that missing Property sections exist. keep the Carrier defect visible; do **not** invent headings **or** values from filenames **or** folders. **if** the content itself is absent **or** ambiguous, identify the precise unavailable evidence **or** unresolved meaning for the affected check. empty supporting content **may** satisfy Details; missing Details heading still fails Properties.

this checklist has **`=3`** disjoint parts: CCE for `cce`, Properties for `properties`, **and** coherence for `scope`, `claim`, `details`, **and** `summary`. **every** part uses the same source binding **and** compact local rule pack.

the Claim check applies the supplied Operator-authority rule **to** the candidate's own text:

- a capability Requirement states what the Framework provides. its existence alone does **not** authorize execution.
- direct Operator instruction **or** explicit prior authorization **may** cover a Workflow **or** automation. required behavior during that authorized execution remains binding.
- report an authority violation **only** with evidence that the text forces execution independently of Operator authorization. `must`, an event condition, **or** omitted repeated approval wording alone is insufficient evidence.
- an unresolved distinction is a coverage gap, **not** an assumed violation. identify unspecified operation targets from the local text **without** inventing a Projection **or** another target.

the profile is `atom_local`. Subject **and** relation fields are checked for local shape **only**. Entity-model correctness, Subject completeness **or** similarity, relation-target existence/status, cross-Atom conflicts, duplicate Claims, role reclassification, tier hierarchy, **and** general Principle alignment are excluded. the explicit local execution-authority check above is included; it does **not** require a wider Principle audit. excluded checks are **not** failures, passes, **or** coverage gaps of this profile.

the result is failed **if** **any** local check fails, **otherwise** blocked **if** **any** local check is unresolved, **otherwise** passed. findings **and** coverage gaps remain distinct even **when** present together. a passed result asserts local quality **only**, **not** complete methodology conformance.
