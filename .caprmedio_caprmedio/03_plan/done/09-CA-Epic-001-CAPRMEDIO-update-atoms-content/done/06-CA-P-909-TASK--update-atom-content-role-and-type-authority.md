---
atom_id: CA-P-909
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Atom Content Role and Type Authority
    occurrent:
      - Atom Classification Authority Update
  depends_on:
    occurrent:
      - CA-P-907
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Atom Content Role and Type Authority

**when** CA-P-907 is Done, **then** the Assignee **must** make Atom Content Role and local Type authority use bearer-qualified Properties and distinct allowed values.

## Scope

`((every CA-P-905 frontier entry assigned to ATOM_CONTENT_ROLE_AND_TYPE) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (Content Role is not a Property borne by Atom **or** Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, and Operations are not distinct allowed Content Role values **or** Type is borne directly by Atom rather than by a value-qualified Content Role **or** Task is treated as a Content Role **or** the qualified Type domains under Plan and Requirement cannot be distinguished **or** Epic is registered in any Atom Type domain **or** the Core default Concern Type registry differs from (Question, Conflict, Problem) **or** the Core default Analysis Type registry differs from (Analysis Report, Rationale) **or** Local Tier is collapsed into Atom Type **or** Local Tier is not a separate Atom Property with allowed values (Principle, Core, Standard) **or** Standard is not the default Local Tier **or** any replaced conflicting authority remains active).

## Details

keep local Property name `Type` reusable because its canonical identity and allowed-value domain come from its complete bearer-qualified path. keep additional and Project-specific Type registries open through Extension and Local Configuration authority. leave Content Role tokens and Local Tier filename tokens to CA-P-913. leave the registration and semantics of Job and Demand to CA-P-910 and Task to CA-P-911.
