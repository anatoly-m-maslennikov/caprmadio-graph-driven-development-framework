---
atom_id: CA-C-455
content_role: Concern
type: Problem
current_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 04:21:12 +0000"
subjects:
  governs: "Draft promotion source conformance"
  depends_on: [Atom, Carrier, Tool, Evaluation]
relations:
  concern_about: [CA-P-1662, CA-D-569, CA-D-570]
---
# Summary

Record retired Draft identity evidence shape

## Concern

The first P1662 implementation accepted the retired request shape `{kind, prior, prior_revision}` instead of current D569@2's exact `{draft_digest, revision_lineage}`. The mismatch was found by reading the accepted source, not inferred from a passing test count. The saved repair rejects the retired shape, requires the actual Draft digest and value-identical carried lineage, and retains D570 as the sole identity basis. Root reran five promotion, fourteen status and four demotion tests successfully. Current lifecycle_intents.py SHA-256 is 497b31578cbc4cad87d3fa3130f8c45076572490fa3d8924863442e22789d680. This Problem is resolved for the bounded native path; it is not immutable-image or MCP proof.

## Evidences

The directly affected Task preserves the exact resulting files, source pins, actual focused test outputs and remaining coverage.

## Blast radius

The narrow implementation slice named above. No broader source audit, runtime promotion or denied-operation workaround is authorized by this record.
