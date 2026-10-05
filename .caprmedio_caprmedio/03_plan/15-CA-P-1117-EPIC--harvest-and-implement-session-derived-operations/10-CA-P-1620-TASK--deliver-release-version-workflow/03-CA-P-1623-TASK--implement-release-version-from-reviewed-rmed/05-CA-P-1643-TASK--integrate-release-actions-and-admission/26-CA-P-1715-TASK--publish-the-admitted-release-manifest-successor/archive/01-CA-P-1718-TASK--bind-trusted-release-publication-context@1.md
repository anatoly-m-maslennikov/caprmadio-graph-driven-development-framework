---
atom_id: CA-P-1718
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 1
updated_at: "2026-10-05 15:30:49 +0000"
subjects:
  governs: "Release publication authorization"
  depends_on: [Implementation, Operator, Journal, Manifest, Evaluation]
relations:
  is_decomposition_of: [CA-P-1715]
  blocks: [CA-P-1624]
---
# Summary

Bind trusted Release publication context

## Objective

Deliver the private host-created context that authorizes only the exact current Release manifest publication.

## Details

1. implement `release_manifest_authorization.py` from current CA-R-1882@2, CA-M-339@2, CA-E-582@2 and CA-D-576@2. Validate the human Operator through the current Operators Registry and bind root, input bytes, accepted source frontier and candidate digest.
2. admit only a typed private host capability, not an incoming boolean, arbitrary callback or serialized grant. Preserve registered Operator identity separately from the existing generic Journal's author serialization; do not invent a new human identity.
3. test unregistered, altered, stale, wrong-root and caller-forged contexts. Share the narrow context/validation API with the parallel recorder and publisher owners.
4. root retains actual publication authority and Git. This leaf does not publish a manifest, append a canonical event or dispatch a Run.

The bounded next implementation/review leaf is estimated at <=15 minutes. Decompose before exceeding that bound. Independent API authoring may proceed in parallel; dependent tests and acceptance wait for the current helper implementations. Root owns integration, accepted authority and Git.

## Definition of Done

The private context and fresh validation are implemented, focused adversarial tests pass and the actual authority boundary receives independent bounded review. No fake callback grants or runtime proof substitute for these checks.

## Pre-execution review

Root accepts this bounded decomposition of the parent's existing source requirements. It adds no selected Workflow or execution permission, preserves the required full behavior, and does not execute the Operator-deferred final all-Workflow audit.
