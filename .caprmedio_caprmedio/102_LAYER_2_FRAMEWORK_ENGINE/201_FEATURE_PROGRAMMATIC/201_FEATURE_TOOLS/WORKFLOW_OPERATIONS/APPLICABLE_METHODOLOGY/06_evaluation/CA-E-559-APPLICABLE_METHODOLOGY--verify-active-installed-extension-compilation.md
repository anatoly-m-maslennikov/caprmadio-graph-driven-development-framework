---
atom_id: CA-E-559
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:50 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY"
  depends_on: [Tool, Extension, Project Configuration, Methodology Source, Projection, Journal]
relations:
  evaluation_for: [CA-R-1839, CA-R-1842, CA-M-226]
---
# Summary

Plan functional proof that an activated installed Extension contributes without source mutation.

## Scope

Functional Project/MCP-ready case for a conflict-free active Core, installed Extension, and Project Configuration frontier.

## Claim

An implementation **must** prove that an activated installed Extension Revision contributes to the selected and published Applicable Methodology without source mutation or loss of its original-source relation.

## Details

Prepare a Project fixture with one Active Core source, one active installed Extension at a settings-selected Revision, and one Active Project Configuration source. Snapshot the source, prior output, and Journal/Run evidence before dry run. The dry run must enumerate all three layers, retain their exact source paths/IDs/Revisions/digests and original Relations, report no hidden Extension exclusion, return one deterministic digest, and leave every source and output byte plus Journal/Run evidence unchanged. Apply must publish a complete derived output with source bindings, unchanged source bytes, a stable output digest on repeat, and shared Journal/Run receipt references. Every published Carrier must be an Active RMEDO Carrier in a governed role directory: no non-RMEDO, Draft, archived, monolithic, persistent-index, or placeholder Carrier may be emitted. For every published Carrier, compare the selected source frontmatter, body, Relations, path/ID/Revision/digest binding, and bytes with its derived counterpart.

The same fixture with no activated Extension must succeed without a placeholder collection Carrier. An inactive or unselected Extension must be reported as excluded and must not appear in output. Delete the full generated output, then apply the unchanged current resolved frontier again: it must regenerate the complete role tree byte-for-byte with the same deterministic output digest. This is planned functional assurance, not a runtime pass.

### Strict request rejection matrix

Exercise an otherwise valid request with an unknown field, mixed operations or fields, a caller-supplied mutable source or output path, `edit_source`, a raw source patch, an arbitrary selected candidate, raw approval text or a TOML-only approval, and a caller-authored Journal or Run event payload. Each request must be rejected at the strict boundary without source authority, output, or Journal/Run effects; canonical shared Run/Journal handles remain references only.

### Sources

- CA-R-1839; CA-R-1842; CA-D-541 v1; CA-O-152 v2; CA-O-157 v2.
