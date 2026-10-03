---
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
    - "Atom"
    - "Atom/Content Role: Operations/Type: Action"
    - "Atom/Claim"
version: 8
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
---
# Define Action

an Action **means** an Atom with Content Role Operations **and** Type Action whose Claim specifies one reusable operational building block with an explicit operational contribution **and** a justified boundary at the modeled responsibility **and** granularity **where** further division has no useful independently governed meaning. this atomic boundary is **not** a count of machine instructions **or** Tool calls; an arbitrary large procedure **without** that justified boundary is **not** an Action. the Action is distinct from an Actor, a Tool, a Task, a particular execution, a Journal Record, **and** a Carrier. its execution kind is defined under CA-R-1526; an Agentic Action **may** use Tools **without** making **every** call another Action **or** Step.
