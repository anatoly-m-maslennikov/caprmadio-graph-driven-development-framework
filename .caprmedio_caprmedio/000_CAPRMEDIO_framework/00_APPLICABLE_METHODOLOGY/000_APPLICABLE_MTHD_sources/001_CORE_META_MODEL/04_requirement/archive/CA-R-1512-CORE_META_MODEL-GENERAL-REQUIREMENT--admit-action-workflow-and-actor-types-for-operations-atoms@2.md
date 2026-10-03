---
cce_version: cce_1
cce_form: classification
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    - "Atom/Content Role: Operations"
    - "Type"
    - "Action"
    - "Workflow"
    - "Actor"
    - "Atom/Claim"
version: 2
updated_at: "2026-09-20 23:33:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-O-068", "CA-O-069"]}
---
# Admit Action, Workflow, and Actor Types for Operations Atoms

the admitted internal Type values under `Atom/Content Role: Operations/Type` **must** include (Action, Workflow, Actor), with the following classification:

- Action: an Operations Atom whose Claim defines reusable Action behavior.
- Workflow: an Operations Atom whose Claim defines reusable Workflow behavior, including a context-specific binding of a reused flow.
- Actor: an Operations Atom whose Claim defines an Actor participation **or** authorization policy.

these values classify definition Atoms, **not** their governed Actions, Workflows, **or** Actors, particular executions, **or** execution records. the Atom **and** its governed target retain distinct identities. this admission keeps the qualified Type domain open **and** does **not** change other admitted values. the additional Foundation **and** Rule Types are admitted by CA-O-068; the methodology Operations tier mapping is governed by CA-O-069.
