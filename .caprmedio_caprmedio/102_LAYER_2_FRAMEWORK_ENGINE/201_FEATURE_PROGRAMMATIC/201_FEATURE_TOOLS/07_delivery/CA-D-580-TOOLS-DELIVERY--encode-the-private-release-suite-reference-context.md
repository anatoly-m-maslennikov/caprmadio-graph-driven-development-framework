---
atom_id: CA-D-580
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 7
updated_at: "2026-10-06 20:32:22 +0000"
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

`reference_rows` are source-path sorted with no duplicate path. `control_context_digest` is the SHA-256 of canonical JSON over exactly the schema version, trusted binding values, and ordered rows, excluding itself. The closure includes the exact `project_structure.toml` carrier beneath the control root declared by Project Settings. The closure begins only at the named roots in CA-R-1887 and expands only through the selected-manifest source registry, CA-D-572 pin declarations, the following closed Prompt binding frontier and the separate registered selected-source refresh authority frontier. It contains no caller fields, credentials, secrets, runtime carriers, Journal files, output files, symlinks, directories, or arbitrary transitive discovery.

### Prompt binding frontier

| Package | Binding carrier | SHA-256 |
| --- | --- | --- |
| IMPLEMENTATION_WORKFLOW | `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/source_bindings.json` | `9c79de6ac6f022c3d4361d460729b3c9c7af0e8473aa972181dc844a93a0a4a3` |
| RMED_ATOM_REVIEW | `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW/source_bindings.json` | `6da38387e1d8633e1901bb06e649d27550f4fe656220c7bdb91648aea3c04dc2` |

Include each exact binding carrier and every member of its existing `sources` array. A source pin has exactly `atom_id`, positive integer `version`, safe Project-relative `path` and lowercase SHA-256 `sha256`; validate those values against the current active Atom. Keep each binding's existing schema-1 package metadata unchanged. Duplicate declarations within one binding and conflicting shared pins are invalid; identical shared pins across the closed frontiers are unioned once. The resulting carriers are ordinary `reference_rows`, not a new context field, public request, inventory field or Journal schema. Obsolete Plan carriers and folder-wide discovery are not members of this frontier.

The Suite Owner retains this object only as internal sealed suite evidence, verifies it before copy and after execution, and supplies its digest to the schema-2 suite envelope defined by CA-D-579. It creates no new public Tool, Workflow, Action, Run, or Journal schema.

### Selected-source refresh authority frontier

The closed `reference_rows` set also includes **only** the following source-path-sorted Active Atom pins for the registered selected-source refresh. These are a separate authority frontier, not Prompt bindings or new context fields. CA-R-1041 is the exact Requirement dependency validated by the CA-D-588 registered refresh.

| Atom ID | Version | Source path | SHA-256 | Mode |
| --- | --- | --- | --- | --- |
| `CA-R-1041` | 8 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REPLACE_ATOM/04_requirement/CA-R-1041-TOOLS--coordinate-atom-replacement-intent.md` | `45a87fc9dbb416111b66b22875c844abcce0cd362f0a421190406897413bd9bc` | `0644` |
| `CA-R-1894` | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1894-MCP-REQUIREMENT--refresh-only-accepted-selected-source-pins.md` | `8c757293510088685fa539e22eedb8cea2a4d3cdd14ccc7fadf3f20d0e7ece4b` | `0644` |
| `CA-M-350` | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/05_method/CA-M-350-MCP-METHOD--derive-the-registered-selected-pin-refresh.md` | `611f47a31ec786a8ec927e5fcd33a41cff39bf5e0832803220ed4194f3799744` | `0644` |
| `CA-E-593` | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/06_evaluation/CA-E-593-MCP-QA_CASE--verify-the-registered-selected-pin-refresh.md` | `562e5840644c75916218a223a4a07b986131f8979501ca73e51ca1e1611119e3` | `0644` |
| `CA-D-588` | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/07_delivery/CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh.md` | `2bab8cafd97e810ea73d36b5ee5ece8b7e47dadec9fc1f07097205ce5eafdce7` | `0644` |

Descriptor-capture each exact regular Carrier and validate its Atom ID, Version, Active Status, observed mode and SHA-256 before copy. Union identical shared paths once; missing, conflicting, changed or unsafe Carriers fail closed. Historical input manifests and test controls remain declared test fixtures, not current project-control sources. No folder discovery or additional transitive frontier is admitted.

### Unit deadline source carriers

The closed `reference_rows` set also includes exactly these two explicit settings carriers, without changing the context JSON member set: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml`. The Suite Owner reads only their captured bytes and resolves `[release_suite].unit_timeout_seconds` by instance-over-default fallback. The value is finite, non-boolean, positive, and at most `7200` seconds. The rows are source fingerprints for the private deadline snapshot, not a new public context member; missing or changed carriers fail closed.
