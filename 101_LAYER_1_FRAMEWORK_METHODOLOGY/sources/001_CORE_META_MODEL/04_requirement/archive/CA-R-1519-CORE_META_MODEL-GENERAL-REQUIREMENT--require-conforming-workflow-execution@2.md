---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Workflow"
  depends_on:
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Step Run"
    - "Workflow/Relation Kind: On Result"
    - "Artifact/Revision"
    - "Operator"
    - "Methodology"
version: 2
updated_at: "2026-09-18 21:51:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1508", "CA-R-1509", "CA-R-1510", "CA-R-1511", "CA-R-1513", "CA-R-1525"]}
---
# Require conforming Workflow execution

an executor of a Workflow **must** conform **to** the applicable methodology execution rules rather than inventing behavior that is absent from its governing definitions.

- resolve the Workflow, referenced Actions, Step bindings, typed transitions, terminal outcomes, **and** applicable execution rules **before** their use. bind definition Revisions **and** revalidate definition changes under CA-R-1525 rather than silently resolving a different Revision during the same Run.
- preserve supplied inputs, returned results, **and** actual Run identities under CA-R-1509, CA-R-1510, **and** CA-R-1511.
- admit work **only** within the applicable authorization, Operator-approval, retry, waiting, **and** recovery conditions. a missing capability **or** unresolved rule blocks the affected execution rather than granting permission. a well-formed definition remains valid **when** a selected executor lacks a required capability; definition validation **and** execution admission are distinct checks.
- a Workflow **may** assume these declared capabilities; it **must not** require a particular executor product merely **to** define its behavior.

this conformance boundary does **not** select a server, programming language, storage technology, **or** a Workflow for building the executor itself.
