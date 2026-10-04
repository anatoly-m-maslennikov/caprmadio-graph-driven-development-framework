---
atom_id: CA-P-1504
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Selected capability RMED review correction"
  depends_on: [Implementation, Evaluation, Workflow, Journal]
version: 4
updated_at: "2026-10-04 19:24:56 +0000"
relations:
  is_decomposition_of: [CA-P-1134]
  blocks: [CA-P-1499, CA-P-1122, CA-P-1162, CA-P-1163]
---
# Summary

complete selected mcp mode and source manifest

## Objective

Correct only the exact independent RMED findings before implementation. Estimate <=15 minutes; inherited threshold 90%. No harvesting, FPF, code or broader audit. Root retains review findings in C430 and review Plans; actual independent re-acceptance is required.

### Inputs and ownership

Current P1499 review, current exact native carriers R1847/R1848, E567/E568, D547, their accepted source Operations and shared D527/528/529. Preserve other workers' edits; use apply_patch. Archive prior meaningful native-carrier revisions, bump semantic Version, and use actual Updated At.

### Required correction

Use canonical `preview`/`execute`, one derived immutable per-route binding manifest, D521v3's existing `enqueue_selected` APP, eight helpers, and hot reload. No code, new executor, source campaign, or broader audit. Every incomplete/stale/shadow manifest case must reject before Run/effect.

## Details

### Prior saved result

P1504 v2 completed the first MCP correction: R1847/R1848/E567/E568/D547 v2 adopted `preview`/`execute`, the full thirteen-route manifest contract derived from A1142v2, no duplicate executor, and no-Run incomplete/stale cases. Each v1 predecessor was archived. No runtime proof was claimed.

### Actual reopened correction and result

P1504 was physically reopened v3 at 2026-10-04 19:24:08 +0000 after focused re-acceptance found two bounded residual issues. Saved at 2026-10-04 19:21:30 +0000: CA-R-1847 v3, CA-R-1848 v3, CA-E-567 v3, CA-E-568 v3, and CA-D-547 v3; every meaningful v2 predecessor is now physically archived in its native role-local `archive/` folder with `status: Archived`.

- All five source citations now pin the current CA-D-527 v3 contract.
- The only canonical manifest reference/digest is the outer `definition_manifest` (`manifest_ref`, `manifest_digest`). `source_freshness` retains selected-source registry/binding evidence only; manifest fields there or anywhere else are unknown shadow fields and reject before a Run/effect, including matching or different digests.
- E567/E568 add both matching-shadow and different-digest rejection cases with no shared-support invocation, Run, Action Run, worker, effect, Event, or Journal creation.
- D547 still reuses D521v3's existing DBOS `enqueue_selected` APP, preserves the eight helpers/hot reload, and introduces no executor.

The focused static gate passed after reopening: all five v3 headers/timestamps/source pins, five archived v2 carriers marked Archived, exact canonical-outer/shadow-rejection semantics, E567/E568 matching-and-different shadow cases, no D527v1 citation, no obsolete `binding_manifest_canonical_sha256`, no trailing whitespace, and clean `git diff --check`. This is specification evidence only; no code, MCP runtime, Docker, or independent re-acceptance is claimed. Root must independently re-accept this packet before implementation starts.

### Definition of Done

All named correction obligations are saved and locally verified, ready for independent focused re-acceptance. Runtime/code remains gated.
