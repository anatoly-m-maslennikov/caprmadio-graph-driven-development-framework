---
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/installed release manifest"
  depends_on:
    - "Artifact/Revision"
    - "Carrier"
    - "Project"
    - "Tool"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1065"], "relates_to": ["CA-D-011", "CA-D-025", "CA-M-103", "CA-M-166", "CA-M-221", "CA-M-281"]}
---
# Summary

Declare installed Tool release contents and prerequisites

## Claim

the selected installed Tool release **must** carry **`=1`** release manifest that represents its complete executable **and** static-resource contents **and** its admitted host prerequisites.

- use the content-addressed release identity, relative paths, digests, **and** executable-mode bindings owned by CA-M-103; extend that manifest rather than maintain a competing inventory.
- identify the supported Python **and** platform boundaries from their accepted authority. identify **any** admitted host interpreter **or** Git prerequisite separately from bundled FRAMEWORK_ENGINE Implementation under CA-R-1065; unknown compatibility **must not** be represented as supported.
- keep this manifest **with** the release selected through CA-D-011. it describes the selected release, **not** a live import from canonical source **or** a project virtual environment.

runtime isolation, installation verification, selection, **and** rollback remain governed by CA-R-1065, CA-M-103, **and** CA-M-221. this manifest does **not** add an installer procedure, host Hook, dependency, **or** platform-support promise.
