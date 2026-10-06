---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Action"
  depends_on:
    - "Actor"
    - "Tool"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Journal/Record"
    - "Carrier"
    - "Action/Execution Kind"
    - "Step"
version: 6
updated_at: "2026-09-22 14:41:44 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Action

an Action **means** one reusable operational building block with an explicit operational contribution **and** a justified boundary at the modeled responsibility **and** granularity **where** further division has no useful independently governed meaning. this atomic boundary is **not** a count of machine instructions **or** Tool calls; an arbitrary large procedure **without** that justified boundary is **not** an Action. the Action is distinct from an Actor, a Tool, a Task, a particular execution, a Journal Record, **and** a Carrier. its execution kind is defined under CA-R-1526; an Agentic Action **may** use Tools **without** making **every** call another Action **or** Step.
