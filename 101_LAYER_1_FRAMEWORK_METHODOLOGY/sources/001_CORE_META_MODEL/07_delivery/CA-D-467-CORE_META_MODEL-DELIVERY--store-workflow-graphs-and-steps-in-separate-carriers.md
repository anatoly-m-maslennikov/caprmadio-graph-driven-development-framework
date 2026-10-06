---
subjects:
  governs: "Workflow/Carrier"
  depends_on:
    - "Directory Carrier"
    - "Atom Collection"
    - "Artifact/Carrier"
    - "Atom/Content Role: Operations/Type: Workflow"
    - "Atom/Content Role: Operations/Type: Step"
version: 4
updated_at: "2026-10-01 21:24:33 +0400"
relations: {"delivery_for": ["CA-R-1570", "CA-R-1569"], "relates_to": ["CA-D-457", "CA-D-285"]}
atom_id: "CA-D-467"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Store Workflow graphs **and** Steps in separate carriers

## Scope

folder-backed Workflows.

## Claim

a folder-backed Workflow **must** use a Directory Carrier containing **`=1`** Workflow Atom Markdown Carrier **and** separate Markdown Carriers for its Step Atoms.

## Details

- the Workflow Atom's main content carries the graph scheme; a Step Atom's main content carries that Step's Action reference **and** parameter/input bindings.
- the Atom files retain the existing Atom filename, frontmatter, **and** main-content rules; the folder is a grouping Carrier, **not** another Workflow definition **or** owning Scope Unit.
- grouping is optional: separately placed Workflow **and** Step Carriers remain permitted **when** their references resolve unambiguously. moving them into a grouping folder does **not** redefine their graph.
