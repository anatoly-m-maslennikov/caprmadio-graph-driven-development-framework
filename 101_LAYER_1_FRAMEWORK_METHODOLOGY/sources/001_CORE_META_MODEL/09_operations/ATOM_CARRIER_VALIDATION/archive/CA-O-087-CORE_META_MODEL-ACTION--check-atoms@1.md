---
atom_id: CA-O-087
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
  governs: "Check Atoms"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Property"
    - "Atom/Frontmatter"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Revision"
    - "Owned Atoms"
    - "Subtree-owned Atoms"
    - "Scope Unit"
    - "Project Structure"
    - "Global Tier"
    - "Local Tier"
    - "Applicable Methodology"
    - "Projection"
    - "Relation"
    - "Evaluation"
    - "Operator"
    - "Journal"
version: 1
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  relates_to:
    - CA-R-1598
    - CA-R-942
    - CA-R-1447
    - CA-D-305
    - CA-D-478
    - CA-D-479
    - CA-D-480
    - CA-D-481
    - CA-D-482
    - CA-D-483
    - CA-E-379
    - CA-E-506
---
# Summary

Check Atoms

## Claim

Check Atoms **means** the Programmatic Action that checks a selected Atom set against applicable machine-checkable authority **and** returns findings **without** changing the Atoms.

### Inputs and selection

- inputs: a bounded source inventory, a selector, applicable methodology context, reference-resolution context, admitted read boundaries, **and** selected execution limits.
- select by a Scope Unit's Owned Atoms, optionally including its descendant Scope Units; by Global Tier values; by Local Tier values; **or** by an explicit Atom list. **>=1** selection criterion is required.
- values within a list are alternatives; supplied selection criteria intersect. Scope Unit selection uses the Atom's carried current Scope Unit; descendants use declared Project Structure parentage, **not** directory nesting. tier filters use internally carried values, **not** filename tokens.
- an explicit list identifies exact intended source Atoms **or** Revisions; a Carrier locator **may** identify an unassigned Draft **or** a malformed candidate **without** supplying its missing Properties. ambiguous references are unresolved, **not** silently resolved **to** whichever file is found first.
- unreadable, malformed, **or** missing selection data remains an unresolved candidate with its reason. retain independently decidable selections; unresolved membership **must not** become a successful exclusion. do **not** expand target coverage through reference resolution.

### Check and return

- resolve admitted Properties, sections, Content Roles, Types, Statuses, cardinalities, Subjects, **and** Relation rules from applicable authority; bind executable checks **to** their exact governing Atom Revisions. unknown **or** unsupported authority is a coverage gap, **not** permission **to** invent a rule.
- safely parse frontmatter **and** structured body sections. check duplicate keys, value types, unknown fields, required/optional/inapplicable Properties, Draft exceptions, missing **or** ambiguous sections, **and** frontmatter/body conflicts. fenced headings remain content.
- extract Properties **only** from their canonical internal locations. check outward filename/placement representations **after** extraction; never use them **to** fill a missing value. check authored Atom Relations **in** their owning direction **and** under their actual target/Status rules; do **not** require stored inverse **or** transitive copies.
- check projected Applicable Methodology Carriers against their original source bindings **and** authored bytes under CA-D-305 **and** CA-E-379. projected copies do **not** become independent source Atoms.
- record passed, failed, not-applicable, **and** not-checked outcomes with target locator, declared identity/Revision **when** available, Property/section, governing rule, reason, **and** bounded evidence. continue independent checks **after** a malformed candidate.
- bind the assessment **to** its selected input set **and** content fingerprints; recheck membership **and** relevant source, authority, configuration, **and** reference fingerprints **before** returning. changed inputs yield incomplete currentness, **not** mixed-Revision success.
- return `valid` for a nonempty, fully checked, unchanged set with no failures; `invalid` for complete unchanged coverage with failures; `incomplete` for unresolved selection, empty selection, missing authority, unsupported checks, **or** changed inputs; `error` for execution failure. retain known findings **and** coverage even **when** the result is incomplete **or** error.

### Boundary

- permission **to** read is a precondition; this Action grants no permission. do **not** read secrets **or** outside admitted roots, fetch remote resources, execute supplied content, **or** write sources, Settings, caches, generated copies, **or** Journal files.
- preparation, checking, **and** report assembly are internal work of this **=1** Action, **not** separate Action **or** Step definitions. a Workflow **may** invoke it through a Step; the Action does **not** select **or** start a repair Workflow.
- the report assesses mechanical conformance, **not** Claim atomicity, semantic consistency, **or** complete natural-language CCE conformance. the caller/executor owns any admitted persistence of returned execution evidence.
