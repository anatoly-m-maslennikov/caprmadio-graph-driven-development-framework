---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    - "Action"
    - "Step"
    - "Workflow"
    - "AI Agent"
    - "Operator"
    - "Tool"
    - "Artifact/Revision"
version: 1
updated_at: "2026-09-20 15:47:25 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"method_for": ["CA-R-1529"], "relates_to": ["CA-M-301", "CA-M-294", "CA-R-1452", "CA-R-1528"]}
---
# Write self-contained agentic Action instructions

**to** present an Agentic Action for execution, organize its derived instruction around the declared responsibility rather than assumed session memory.

- state the requested outcome, relevant context, exact targets, inputs, available evidence, **and** governing references.
- distinguish already performed effects from proposed changes, **and** existing permissions from decisions still needed.
- state the expected result **and** how **to** report uncertainty, failures, partial effects, **or** a request for Operator input. do **not** treat a suggested correction as permission **to** apply it.
- keep the instruction limited **to** the bound Action. leave next-Step selection **and** cross-Workflow handoff coordination **to** the executor using the governing Workflow.
- use understandable wording **and** structured points under CA-M-301 **and** CA-M-294; reference governing definitions rather than copying another authoritative procedure into the prompt.
- keep internal Tool calls as execution detail under CA-R-1528. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.
