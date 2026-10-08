---
atom_id: CA-D-580
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 18:54:35 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Private suite reference-context encoding"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest]
relations:
  delivery_for: [CA-R-1887, CA-M-344]
---
# Summary

Encode the private Release-suite reference context

## Scope

The exact internal schema for the Suite Owner's sealed reference closure and currentness digest.

## Claim

The Suite Owner **must** encode the reference context as canonical JSON containing only trusted internal binding values, typed allowlisted `reference_rows`, and `control_context_digest`; it is private evidence, not a candidate manifest or caller contract.

## Details

```json
{
  "schema_version": 1,
  "candidate_snapshot_manifest_sha256": "<trusted candidate sha256>",
  "compiled_candidate_root": "<trusted project-relative compiled root>",
  "selected_n_identity": "<trusted frozen selected-N identity>",
  "selected_n_image_context": "<trusted selected-N image-context identity>",
  "reference_rows": [
    {"source_path": "<allowlisted project-relative regular file>", "sha256": "<lowercase sha256>", "mode": 420}
  ],
  "control_context_digest": "<lowercase sha256>"
}
```

`reference_rows` are source-path sorted with no duplicate path. `control_context_digest` is the SHA-256 of canonical JSON over exactly the schema version, trusted binding values, and ordered rows, excluding itself. The closure begins only at the named roots in CA-R-1887 and expands only through the selected-manifest source registry and CA-D-572 pin declarations. It contains no caller fields, credentials, secrets, runtime carriers, Journal files, output files, symlinks, directories, or arbitrary transitive discovery.

The Suite Owner retains this object only as internal sealed suite evidence, verifies it before copy and after execution, and supplies its digest to the schema-2 suite envelope defined by CA-D-579. It creates no new public Tool, Workflow, Action, Run, or Journal schema.

