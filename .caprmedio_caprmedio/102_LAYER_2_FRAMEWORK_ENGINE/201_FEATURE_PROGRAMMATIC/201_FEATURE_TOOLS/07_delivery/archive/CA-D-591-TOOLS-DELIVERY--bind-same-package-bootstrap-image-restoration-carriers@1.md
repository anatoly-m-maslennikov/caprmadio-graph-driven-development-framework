---
atom_id: CA-D-591
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 22:31:14 +0000"
subjects:
  governs: "Tool/FRAMEWORK_IMAGE_RESTORATION/Intent and proof carriers"
  depends_on: [Tool, Operator, Framework Package, Runtime, Skill, Manifest, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1897, CA-M-353]
---
# Summary

Bind same-package bootstrap image restoration carriers

## Scope

The closed private intent, retained build proof, selector replacement and actual result of CA-O-187, outside the selected Release Version request and route.

## Claim

FRAMEWORK_IMAGE_RESTORATION **must** retain a frozen same-package intent, the applicable authentic canonical bootstrap proof and fresh attempt observations, and the actual image-binding restoration result while preserving existing package, selector, proof and canonical Journal schemas.

## Details

The admitted source API is restore_framework_image(project_root, *, journal, requested_run_id, expected_selector_sha256, image_executor). Its only caller input seal is the exact selector SHA-256; it derives the retained package, original proof and context internally. The frozen intent contains exactly action_id = FRAMEWORK_IMAGE_RESTORATION, kind = retained_selected_framework_image_restoration, manifest_sha256, source_context_sha256, selected_selector_sha256, old_image_digest, retained_proof_receipt_sha256 and retained_context_sha256. Digest values are actual lowercase SHA-256 observations; old_image_digest is an immutable sha256 image ID. requested_run_id binds that closed intent and source authority through the existing direct Session, rather than adding an intent member. The registered Operator and authorization reference remain the direct Session's explicit authorization boundary. The replacement image digest is not prefilled in the started intent: it is an actual build result. No caller supplies a context path, proof path, Dockerfile, dependency, label, command, tag, network or replacement image override.

The intent digest is SHA-256 of canonical UTF-8 JSON excluding itself. Private restoration evidence occupies only the internally derived .caprmedio_runtime/framework_image_restoration/<intent_sha256>/ location and retains intent.json, the exact prior-selector.toml, the verified replacement-selector.toml when a different image digest is published, fresh actual build/inspect/canary attempt observations at derived private paths, and actual result.json. The complete persistent package and public Skill inventories bind ordered paths, file digests and observed modes, including their directory structure, under the existing Release inventory exclusions. These carriers support one Action's observation and recovery; they are not another Journal or authority registry.

The disposable build context and canonical image proof retain CA-D-575's existing bootstrap evidence shape and derived bootstrap_proof_key. Every actual build retains fresh immutable build/inspect/canary attempt records and outputs. For a different observed image digest, retain a new canonical proof containing those actual command records at the corresponding new key. For the original observed digest, reopen and preserve the existing canonical proof/key unchanged and retain the fresh attempt observations in restoration evidence instead of overwriting historical proof. The applicable canonical proof and fresh attempt bind the original package/source-context identity, authenticated persistent context digest and actual observed immutable image digest. The retained-package reader and installed-N executor receive no bypass or additional selector field.

For a different observed image digest, the replacement selector has exactly CA-D-575's existing bootstrap fields and retains every frozen value except image_digest. For the original observed digest, all exact selector bytes remain unchanged. Both branches use one new fixed Project-wide selector lock shared with normal promotion plus an immediate exact frozen-input recheck; they do not reuse the distinct first-install lock as a substitute.

The actual result binds the frozen intent and Action Run, outcome and reason, observed image digest and applicable canonical proof key/receipt when available, fresh attempt references, prior and observed selector hashes, publication state, and retained effect references. Its closed outcomes are restored, no_op, blocked, partial, effect_uncertain, recording_pending and recovery_required. Both successful build branches are restored, including reproduction of the original image digest; no_op requires the exact image already available and freshly verified before building. An unavailable observation is absent or null, never an expected value presented as actual proof. The canonical Journal retains only its existing completed, no_op, failed, cancelled and partial outcomes: restored requires an observed canonical completed terminal, and no_op uses its existing no_op outcome when an Action was started. Uncertainty retains the started Run or original pending canonical recording without inventing a terminal outcome. The existing result/effect references record actual digests without new Journal fields. A terminal recording failure retains the actual selected or unselected state and any original pending event for exact recording recovery; no carrier authorizes replay or rewrites a historical receipt.
