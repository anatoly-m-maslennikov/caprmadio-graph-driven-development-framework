---
atom_id: CA-P-940
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - CAPRMEDIO Main Skill
    occurrent:
      - CA Main Skill and Host Adapter Creation
version: 2
updated_at: 2026-09-02 00:43:03 +0400
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-943
---
# Create CA Main Skill and Host Adapters

**when** CA-P-943 is Done, **then** the Assignee **must** create the canonical `ca` Skill and thin Codex and Claude host adapters that invoke it as `$ca` and `/ca` respectively.

## Scope

`((accepted CA Main Skill Authority Bundle) union (accepted SKILLS-to-MCP Demand Authority established by CA-P-943) union (canonical ca Skill package) union (Codex $ca adapter) union (Claude /ca adapter) union (Skill validation and cross-host contract tests))`

## Definition of Done

the Task is **not done if** (CA-P-943 is not Done **or** the Skill identity is not exactly `ca` **or** Codex and Claude do not serialize that same Skill as `$ca` and `/ca` **or** either host adapter owns provider-neutral routing, Tool, MCP, lifecycle, or approval behavior **or** any non-main Skill can load the CAPRMEDIO General System Prompt **or** the Main Skill bypasses the canonical Routing Tree or accepted SKILLS-to-MCP Demand Authority **or** an unregistered branch or leaf is accepted **or** direct-route Skills are confused with the Main Skill **or** validation and cross-host behavioral-equivalence tests fail).

## Details

keep `ca` as one Skill with host-specific invocation syntax, not two Skills. load only the bounded authority and prompt context required by the selected route, consume the admitted MCP service through the accepted SKILLS Demands, and keep long-running execution asynchronous through MCP-exposed lifecycle Tools.
