---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Workflow/Carrier"
  depends_on:
    - "Directory Carrier"
    - "Atom Collection"
    - "Artifact/Carrier"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Step"
version: 1
updated_at: "2026-09-21 00:57:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1570", "CA-R-1569"], "relates_to": ["CA-D-457", "CA-D-285"]}
---
# Store Workflow graphs and Steps in separate carriers

a folder-backed Workflow **must** use a Directory Carrier containing **`=1`** Workflow Atom Markdown Carrier **and** separate Markdown Carriers for its Step Atoms.

- the Workflow Atom's main content carries the graph scheme; a Step Atom's main content carries that Step's Action reference **and** parameter/input bindings.
- the Atom files retain the existing Atom filename, frontmatter, **and** main-content rules; the folder is a grouping Carrier, **not** another Workflow definition **or** owning Scope Unit.
- grouping is optional: separately placed Workflow **and** Step Carriers remain permitted **when** their references resolve unambiguously. moving them into a grouping folder does **not** redefine their graph.
