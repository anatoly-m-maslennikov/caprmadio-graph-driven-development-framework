---
content_role: Delivery
type: Delivery
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Skill/package Carrier"
  depends_on:
    - "Action"
    - "Artifact/Revision"
    - "CAPRMEDIO Main Skill"
    - "Carrier"
    - "Methodology"
    - "Skill"
    - "Step"
    - "Tool"
    - "Workflow"
version: 1
updated_at: "2026-09-23 19:41:33 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CAPRMEDIO-FRAMEWORK-ENGINE-REQU-559"], "relates_to": ["CA-D-024", "CA-R-1522", "CA-R-1529", "CA-R-1601", "CAPRMEDIO-FRAMEWORK-ENGINE-REQU-564"]}
---
# Summary

Package Skills as bootstrap and response-handler instructions

## Claim

a delivered Skill package **must** carry its discovery metadata **and** very thin bootstrap/response-handler body separately from task-specific Action instructions supplied through MCP.

- place canonical Skill packages at the SKILLS Delivery binding under CA-D-024. identify the entry purpose **and** **any** registered direct-route reference **in** the host-admitted metadata representation.
- carry the standing instruction body **and** **only** references, templates, **or** assets necessary for that bootstrap **and** generic response handling. references identify the canonical shared runtime **and** capabilities rather than copy their executable contents.
- do **not** bundle deterministic scripts, executable helpers, copies of the Methodology, independent Workflow transitions, **or** a task-prompt library as Skill-owned procedure. ACTION_PROMPTS retains prompt Implementation ownership under CA-R-1601; the current Step invocation remains delivered through MCP under CA-R-1522.
- keep discovery metadata, standing body, **and** optional bootstrap resources distinguishable so the host can load the applicable part. portable content is shared; host-specific package encoding follows its declared host boundary rather than assuming **every** host has identical fields **or** loading behavior.

this Delivery specifies the package Carrier, **not** a new Workflow, permission policy, response schema, installer, Hook, host-support promise, **or** Tool implementation.
