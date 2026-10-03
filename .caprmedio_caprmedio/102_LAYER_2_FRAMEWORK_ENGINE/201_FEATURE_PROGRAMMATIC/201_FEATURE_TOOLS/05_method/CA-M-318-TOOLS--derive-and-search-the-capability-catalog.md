---
atom_id: CA-M-318
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Capability Catalog"
  depends_on:
    - "Tool"
    - "Action"
    - "Workflow"
    - "Atom"
    - "Scope Unit"
    - "Implementation"
    - "Workflow Run"
    - "Journal"
relations:
  relates_to: [CA-R-1810, CA-D-520]
---
# Summary

Derive and search the capability catalog

## Scope

the TOOLS capability for Capability Catalog.

## Claim

**to** derive **and** search the Capability Catalog, the Implementation **must** apply the following method.

## Details

1. read authoritative Project Structure **and** current source Atoms within the configured Project boundary; omit delivered methodology copies **and** historical or draft Carriers.
2. reuse the safe Atom parser; read identity, Content Role, Type, Status **and** Scope Unit from carried Properties.
3. resolve D-owned Tool Binding tables **and** observe admitted entrypoint files without executing them. bind implemented Action Prompts from their existing source manifests.
4. keep duplicate identities **and** unresolved bindings explicit; an observed script with no declaration remains an Implementation candidate.
5. rank matching query words deterministically, apply the requested filters **and** paginate compact results. load full source content only for a selected context.
