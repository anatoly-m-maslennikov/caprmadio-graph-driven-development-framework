---
atom_id: CA-E-597
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 22:25:26 +0000"
subjects:
  governs: "Tool/Validation/Finder metadata acceptance"
  depends_on: [Tool, Carrier, Framework Package, Runtime, Skill, Projection, Journal]
relations:
  evaluation_for: [CA-R-1898]
---
# Summary

Verify metadata-independent Tool validation

## Scope

The persistent inventories and runtime message directories checked under CA-R-1898.

## Claim

The QA case **must** obtain the same validation result for otherwise identical fixtures with **and** without `.DS_Store`, while preserving failures for real invalid files.

## Details

1. Add Finder metadata at the root and nested paths of source, compiled output, retained package, public Skill, image context and runtime nonce-message fixtures. Compare selection, digests, currentness and validation results before and after.
2. Execute the fixed image canary's actual inventory checks against real fixture bytes. Metadata must not alter its result; a missing, changed, wrong-mode or other unexpected package file must still fail.
3. Preserve and reopen original legacy image proofs and the fixed metadata-aware proofs. Reject arbitrary canary code or changed isolation arguments.
4. Check that metadata bytes are not read, modified or deleted by validation. Distinct names such as `.ds_store` and `.DS_Store.bak` remain subject to ordinary admission.
5. Keep fixture results separate from actual Docker and Release acceptance. Historical failed attempts are not relabeled as successful.
