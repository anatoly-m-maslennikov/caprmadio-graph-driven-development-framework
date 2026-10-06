---
cce_version: cce_1
cce_form: classification
subjects:
  governs: "Atom/Content Role: Operations/Local Tier"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Atom/Local Tier"
    - "Atom/Claim"
    - "Type"
    - "Scope Unit"
    - "Action"
    - "Workflow"
    - "Step"
    - "Workflow Run"
    - "Step Run"
    - "Actor"
    - "Journal"
version: 1
updated_at: "2026-09-20 23:33:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-O-068", "CA-R-1442", "CA-R-659", "CA-R-1431", "CA-R-660", "CA-R-1443"]}
---
# Organize Operations into Core, General, and Standard

**within** a non-Project methodology Scope Unit, classify **every** Operations Atom by its complete Claim using Core above General above Standard:

| Local Tier | Contribution | Type |
|---|---|---|
| Core | operational concepts, their fundamental boundaries, **or** the tier system itself; for example, what a Workflow, Step, Action, Workflow Run, **or** Step Run is | Foundation |
| General | reusable rules governing the use, combination, **or** execution of those concepts; for example, admitted invocation contexts, handoff behavior, **or** nested Tool-call treatment | Rule |
| Standard | a particular reusable Action, Workflow, **or** specific Actor participation/authorization policy | the applicable specific Type, including Action, Workflow, **or** Actor |

- this Atom classifies its own contribution as Core/Foundation. the Type admissions **in** CA-O-068 establish the vocabulary; this Atom owns the tier mapping rather than repeating those definitions.
- a reusable **or** widely applicable Workflow remains a particular Workflow definition at Standard; its importance, breadth, **or** reuse alone does **not** make it a Foundation **or** General Rule.
- Standard remains the default lowest Local Tier. omitting its filename token does **not** turn a foundational Claim **or** General Rule into Standard.
- classify fundamental Actor concepts **and** authority boundaries as Foundations, reusable operational constraints as Rules, **and** specific participation policies by their actual contribution. mentioning an Actor does **not** determine the tier.
- the Standard definitions are reusable authority, **not** execution instances. actual Runs **and** their outcomes are recorded **in** the Journal rather than introduced as another local tier.
- this classification does **not** create a methodology Principle tier, alter Project Principle eligibility, **or** classify RMED implementation Spec as the upper tiers of Operations. Operations has its own model **and** rules; RMED remains Spec for Implementation.
