---
atom_id: CA-P-943
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - SKILLS-to-MCP Demand Authority
    occurrent:
      - SKILLS-to-MCP Demand Authority Establishment
version: 1
updated_at: 2026-09-02 00:43:03 +0400
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-939
---
# Establish SKILLS Demands on Admitted MCP Service

**when** CA-P-939 is Done, **then** the Assignee **must** establish the accepted SKILLS Job dependency and Consumer-owned Demand authority for the admitted Project-local Provider-neutral MCP Service Implementation result.

## Scope

`((the exact current MCP Implementation result admitted by CA-P-939) union (the accepted SKILLS Job CA-R-1189) union (current Demand, Claim-boundary, replacement, and Journal authority) union (the seven independently governed SKILLS acceptance Claims for MCP consumption) union (legacy CNTR-002 and its complete incoming-reference frontier))`

## Definition of Done

the Task is **not done if** (CA-P-939 has not admitted **`=1`** current Project-local Provider-neutral MCP Service Implementation result **or** CA-R-1189 does not authorize an exact dependency on that identified result **or** SKILLS does not own **`=7`** separately validated Demands on that same result for current capability discovery, stable callable identity, complete accepted-input contract, canonical invocation, Tool meaning and authority preservation, asynchronous handoff and lifecycle addressability, and stable result interpretation **or** any Demand copies or fully defines MCP producer authority, assigns lifecycle semantics to MCP, constrains more than one Implementation result, lacks an independent accept-replace-retire lifecycle, or serializes another Demand-direction relation **or** CNTR-002 remains active after its true successor Demands are active **or** its replacement lineage includes the new asynchronous-handoff Demand, omits a preserved predecessor component, names a nonexistent successor, or loses an incoming reference **or** CA-E-243, Claim-boundary, lineage-impact, CCE, filename, relation, and project-graph validations fail).

## Details

revise the existing CA-R-1189 Job rather than creating another Job. create seven `SKILLS-DEMANDS_FROM-MCP` Requirement Atoms only after binding them to the admitted result. keep lifecycle behavior in canonical Tools and let MCP expose and transport those Tool capabilities. treat the discovery, callable-identity, accepted-input, invocation, meaning-preservation, and result-interpretation Demands as the six true successors of CNTR-002; treat asynchronous handoff and lifecycle addressability as new authority with no predecessor. activate and commit all Demands before archiving CNTR-002 through a separate governed move.
