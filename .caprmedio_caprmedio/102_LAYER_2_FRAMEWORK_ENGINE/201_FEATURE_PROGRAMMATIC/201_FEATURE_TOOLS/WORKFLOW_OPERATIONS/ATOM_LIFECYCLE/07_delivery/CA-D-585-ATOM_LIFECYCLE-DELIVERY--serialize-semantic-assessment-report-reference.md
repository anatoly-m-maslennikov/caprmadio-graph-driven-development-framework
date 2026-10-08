---
atom_id: CA-D-585
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Semantic Assessment Report Reference"
  depends_on: ["CA-R-1892", "CA-D-531", "CA-D-532"]
version: 1
updated_at: "2026-10-06 05:33:09 +0000"
relations:
  delivery_for: [CA-R-1892]
---
# Summary

Serialize semantic assessment report reference

## Scope

The optional external evidence field of one lifecycle Update request and its retained O145/O129 result evidence.

## Claim

The request representation of external semantic evidence **must** be `semantic_assessment_report: {path, digest}`, with `path` a canonical Project-relative path and `digest` its lowercase SHA-256, bound to the report representation below.

## Details

The referenced report stores exactly one canonical JSON object at `## Results` / `### Update assessment evidence`, with no aliases. The object contains exact target and proposal pins, CA-R-1432 and CA-R-1464 authority pins, the admitted class, `primaryClaimIdentityPreserved: true`, a nonempty declared delta and nonempty lineage-evidence pins. Every pin is `{path, digest}` except the Atom target, which additionally contains `atom_id`.

The request reference accepts no identifier alias, inline assessment, caller-supplied class, Status, authority pin or approval field. O145 returns normalized verified report observations; O129 returns the verified evidence with the actual lifecycle outcome. The shared Run result retains those Action facts under its existing Journal contract; this Delivery adds no Event schema or authorization grant.
