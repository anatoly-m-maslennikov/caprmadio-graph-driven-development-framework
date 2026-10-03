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
version: 3
updated_at: 2026-09-07 19:43:08 +0000
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-943
---
# Create CA Main Skill and Host Adapters

**when** CA-P-943 is Done, **then** the Assignee **must** create the canonical `ca` Skill and a thin Codex host adapter that invokes it as `$ca`.

## Scope

`((accepted CA Main Skill Authority Bundle) union (accepted SKILLS-to-MCP Demand Authority established by CA-P-943) union (canonical ca Skill package) union (Codex $ca adapter) union (Skill validation and Codex adapter contract tests))`

## Definition of Done

the Task is **not done if** (CA-P-943 is not Done **or** the Skill identity is not exactly `ca` **or** Codex does not serialize that Skill as `$ca` **or** the Codex host adapter owns provider-neutral routing, Tool, MCP, lifecycle, or approval behavior **or** any non-main Skill can load the CAPRMEDIO General System Prompt **or** the Main Skill bypasses the canonical Routing Tree or accepted SKILLS-to-MCP Demand Authority **or** an unregistered branch or leaf is accepted **or** direct-route Skills are confused with the Main Skill **or** Skill validation and Codex adapter contract tests fail).

## Details

keep `ca` as one Skill with provider-neutral behavior and a Codex invocation adapter. preserve the host-support boundary established by CA-P-936; Claude compatibility is outside this Task. load only the bounded authority and prompt context required by the selected route, consume the admitted MCP service through the accepted SKILLS Demands, and keep long-running execution asynchronous through MCP-exposed lifecycle Tools.
