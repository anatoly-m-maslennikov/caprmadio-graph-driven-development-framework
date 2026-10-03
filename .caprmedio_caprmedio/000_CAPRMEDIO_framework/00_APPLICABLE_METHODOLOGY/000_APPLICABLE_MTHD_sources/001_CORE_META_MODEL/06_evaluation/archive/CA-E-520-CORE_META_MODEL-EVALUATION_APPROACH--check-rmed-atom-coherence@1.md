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
version: 1
updated_at: "2026-09-25 21:01:05 +0000"
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
relations: {"evaluation_for":["CA-D-269","CA-D-478","CA-D-479","CA-D-495","CA-M-113","CA-M-125","CA-R-1269","CA-R-1270","CA-R-1271","CA-R-1273","CA-R-1465","CA-R-1624"]}
---
# Summary

Check RMED Atom coherence

## Scope

individual active RMED Atoms evaluated against their exact current Revision, applicable authority, **and** Project Principles.

## Claim

an RMED Atom passes this Evaluation **only** **when** **all** of these checks pass with current source evidence:

| Check | Passing condition |
|---|---|
| properties | the Carrier contains the required, admitted, correctly typed Properties **in** their registered single locations; references **and** representations agree; no required value is inferred from a filename **or** folder |
| subjects | **=1** canonical GOVERNS Entity **and** the necessary distinct DEPENDS_ON Entities match the complete scoped Claim **and** supporting Details |
| scope | **=1** explicit applicability description under Scope, possibly composite, is coherent **and** distinct from the carried structural ownership **and** Claim Target Scope Unit |
| claim | **=1** independently replaceable contribution occurs under Claim; multiple clauses alone do **not** imply multiple Claims |
| details | Details **only** explain the Claim within Scope, with no added obligation, exception, independently replaceable Claim, **or** applicability change |
| governed_entity | Scope, Claim, **and** Details together govern **only** the Entity identified by GOVERNS; using a prerequisite Entity through DEPENDS_ON does **not** govern it |
| cce | the complete body follows applicable current CCE **and** understandability rules |
| content_role | the contribution matches its carried Requirement, Method, Evaluation, **or** Delivery role |
| alignment | the Atom agrees with applicable higher-tier authority **and** current Project Principles; unresolved conflicts remain visible |
| summary | Summary faithfully shortens the Claim within Scope; it does **not** replace authoritative content **or** conceal a scope change |

a failed check **must** identify source evidence, the governing authority, **and** the violated condition. an unresolved check **must** identify the missing evidence **or** decision; it is **not** a pass. mechanical findings do **not** prove Claim meaning, **and** a prompt judgment does **not** prove an unperformed mechanical check. the overall result is failed **if** **any** check fails, otherwise blocked **if** **any** check is unresolved, otherwise passed; coverage gaps remain reported even alongside a failure.

## Details

the evaluation concerns this checklist, **not** an unsupported claim of complete Project conformance. independently replaceable obligations fail even **when** joined by a logical operator. a coherent composite condition over **=1** governed Entity **may** pass. harmless examples **and** prerequisite references are **not** automatically additional Claims. a narrower Property target is required **when** that is the actual governed Entity; broadening GOVERNS **to** hide unrelated obligations is **not** a fix.
