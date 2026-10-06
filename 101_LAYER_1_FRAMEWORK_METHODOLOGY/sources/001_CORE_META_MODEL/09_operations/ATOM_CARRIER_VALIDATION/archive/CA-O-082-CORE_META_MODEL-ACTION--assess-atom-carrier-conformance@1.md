---
atom_id: CA-O-082
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
  governs: "Assess Atom Carrier Conformance"
  depends_on:
    - "Action"
    - "Action/Execution Kind"
    - "Atom"
    - "Atom/Property"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Frontmatter"
    - "Relation"
    - "Projection"
    - "Evaluation"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  relates_to:
    - CA-D-305
    - CA-D-478
    - CA-D-479
    - CA-D-480
    - CA-D-481
    - CA-D-482
    - CA-D-483
    - CA-E-379
    - CA-E-506
    - CA-R-1598
---
# Summary

Assess Atom Carrier conformance

## Claim

Assess Atom Carrier Conformance **means** the Programmatic Action that returns machine-checkable findings for one prepared validation input set **without** repairing its Carriers.

- input: the prepared targets, applicable check definitions, source fingerprints, selection evidence, **and** reference-resolution context.
- safely parse frontmatter **and** named Markdown sections; report malformed YAML, duplicate keys, unsafe tags, invalid value types, ambiguous section boundaries, **and** missing required sections. fenced examples **must not** become body Property headings.
- apply the admitted required, optional, **and** inapplicable Property rules, including role/type/status-specific exceptions; reject unknown fields **unless** admitted by the applicable methodology. retain unassigned Draft identity exceptions.
- extract **every** carried Atom value from its canonical internal location. identify duplicate internal authority **and** frontmatter/body conflicts. compare filename **and** placement **only** as outward representations **after** extraction; do **not** recover missing values from them.
- validate Subjects **and** explicitly owned Atom Relations, target resolution, applicable Status constraints, **and** duplicate inverse declarations under the selected Relation authority. do **not** impose an Active-only target rule on Relations that permit historical targets.
- for an Applicable Methodology projected Carrier, check the one-way source binding **and** source fidelity under CA-D-305 **and** CA-E-379. reject generated Projection metadata on an authoritative source Atom.
- record each check as passed, failed, not applicable, **or** not checked, with Carrier locator, declared identity/Revision **when** present, Property/section, rule identity/Revision, **and** finding reason. continue independent checks **after** a malformed candidate; unavailable prerequisites remain not checked, **not** passed.
- return assessed **when** **all** applicable machine-checkable obligations were assessed, including failed obligations; return incomplete **when** a rule, prerequisite, target, **or** input is unresolved; return error for an execution failure, retaining available partial findings.

this Action does **not** prove Claim atomicity, semantic consistency, **or** complete natural-language CCE conformance. those semantic checks remain explicitly outside its result. it does **not** execute Atom content **or** modify sources, generated copies, Settings, **or** history.
