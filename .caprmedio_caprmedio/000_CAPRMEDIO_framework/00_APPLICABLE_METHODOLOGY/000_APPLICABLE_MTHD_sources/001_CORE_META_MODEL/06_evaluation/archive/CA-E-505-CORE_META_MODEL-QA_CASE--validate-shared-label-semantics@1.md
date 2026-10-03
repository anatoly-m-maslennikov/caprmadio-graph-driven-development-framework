---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Label"
  depends_on:
    - "Scope Unit/Label"
    - "Scope Unit/Type"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Entity"
    - "Property"
    - "Operator"
version: 1
updated_at: "2026-09-22 14:53:19 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1594", "CA-R-972", "CA-R-1576", "CA-R-1577", "CA-R-982"]}
---
# Validate shared Label semantics

the Label Evaluation **must** reject a qualified use of Label that changes the shared meaning under CA-R-1594.

## cases

- change **only** a Scope Unit Label among Layer, Feature, **and** Superlayer; retain its identity, declared Type, parentage, Local Order, authority, **and** Relation semantics.
- change **only** a Plan Label among Version, Objective, Epic, Task, **and** Subtask; retain its identity, Type, authoring Subtype, completion conditions, decomposition, **and** blocking.
- resolve `Scope Unit/Label` **and** `Atom/Content Role: Plan/Type: Plan/Label` as distinct bearer-qualified Properties using **=1** shared Label definition, **not** incompatible meanings of the same Term.
- reject inferring an authoring Subtype, required workflow, Status, **or** execution dependency from Label spelling alone.
- accept a Label value that matches a Type **or** Subtype name **only** as a navigation value; any classification still requires its separately governed source.
- retain bearer-specific cardinality, defaults, **and** Carrier encoding under their own authority; the shared definition **must not** require a Label on **every** Entity **or** create a new field **in** existing Carriers.

report the bearer, Label value, **and** wrongly inferred fact **without** silently changing the source Entity.
