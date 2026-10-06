---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Compatible Lineage Impact Disposition"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 12
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define compatible Lineage Impact disposition

`compatible` **means** the child remains valid against the parent Revision required by the gate **and** traversal stops on that branch **without** a child update. **if** the gate requires the revised parent, **then** compatibility **must** be established against that new Revision; permission **to** consume a pinned earlier Revision **must not** establish compatibility for a gate that requires the new Revision.
