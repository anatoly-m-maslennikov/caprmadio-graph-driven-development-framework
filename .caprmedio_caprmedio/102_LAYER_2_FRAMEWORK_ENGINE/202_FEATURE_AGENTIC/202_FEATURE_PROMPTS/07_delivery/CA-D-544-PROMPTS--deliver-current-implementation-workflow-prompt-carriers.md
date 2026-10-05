---
atom_id: "CA-D-544"
content_role: "Delivery"
type: "Delivery"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 2
updated_at: "2026-10-05 03:37:42 +0400"
subjects:
  governs: "Implementation Workflow prompt carriers"
  depends_on: ["Prompt", "Carrier", "Step", "Action"]
relations:
  relates_to: [CA-R-1843, CA-M-326]
---
# Summary

Deliver current Implementation Workflow prompt carriers

## Scope

the future reviewed prompt package at `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/`.

## Claim

the package **must** contain only `CA-O-091`, `CA-O-092`, `CA-O-093`, `CA-O-094`, `CA-O-095`, `CA-O-096`, and `CA-O-099` `.prompt.md` carriers, plus `README.md`, `source_bindings.json`, and `tests/`.

## Details

Each prompt header carries exact Step, Action, and context. This Delivery specifies future reviewed carriers and does not authorize changes to current prompt files.

Every invocation packet additionally carries exactly one `selected_project`
binding before a prompt can verify its governed sources or call an Agent:

| Field | Required value | Boundary |
| --- | --- | --- |
| `selected_project.kind` | `selected_project` | identifies the Project frozen by the selected Workflow; it is not an absolute host path, current directory, code-root copy, or mount grant |
| `selected_project.source_root` | `.caprmedio_caprmedio` | the only authority root for prompt-source resolution |
| `selected_project.source_references` | the exact current `source_bindings` rows, each with Atom ID, Version, project-relative `path`, and SHA-256 | every path is nonempty, relative, has no `..` segment, begins under `source_root`, and resolves only beneath the frozen selected Project |
| `method_projection` | the existing full active-M Projection with source identity, revision, path, digest, and content | its Method source rows must be current members of the same selected-Project source binding; it remains derived input, not Method authority |
| `workspace` | the existing absolute, non-symlink disposable workspace supplied to the Agent | no source binding infers or substitutes this path |
| `permissions.implementation_workspace` | the existing exact `{kind: disposable_workspace, path: workspace, allow_write: true}` capability | it must match `workspace`; this Delivery adds no write grant |

The selected Workflow runtime resolves `selected_project` only from its frozen
Project context. Absent, stale, duplicate, mismatched, escaping, or
partially-readable source references, an incomplete Method Projection, or a
missing/mismatched workspace capability blocks before Agent launch or effects.
This binding exposes neither credentials nor an Agent endpoint and does not
authorize a hidden mount, arbitrary writer, or live-model execution. An
explicit executable mock remains `mock-not-live-llm` evidence only.
