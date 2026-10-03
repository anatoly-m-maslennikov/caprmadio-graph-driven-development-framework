---
content_role: Delivery
type: Delivery
current_scope_unit: GRAPH_SERVER
claim_target_scope_unit: GRAPH_SERVER
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "GRAPH_SERVER/runtime Carriers"
  depends_on:
    - "Atom"
    - "Carrier"
    - "Journal"
    - "Project Temporary State"
    - "Projection"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1077"], "relates_to": ["CA-D-046", "CA-D-437", "CA-M-154", "CA-R-1100", "CA-R-1603"]}
---
# Summary

Separate graph service carriers from governed sources

## Claim

GRAPH_SERVER **must** keep its delivered service Carriers **and** runtime read-model Carriers separate from the governed source Artifacts.

- source-indexer **and** backend Implementation use the GRAPH_SERVER Delivery binding under CA-D-046.
- retained derived indexes, rebuildable database state, service logs, **and** owned service state use its declared project-local `.caprmedio_runtime/` location under CA-M-154.
- disposable indexing scratch, caches, **and** build intermediates use the component-owned Project Temporary State boundary under CA-D-437, **not** the retained database **or** governed-source location.
- read-model metadata records its non-authoritative nature **and** source-frontier references required by CA-R-1077. storage does **not** grant source-mutation capability **or** make the read model another source of truth.
