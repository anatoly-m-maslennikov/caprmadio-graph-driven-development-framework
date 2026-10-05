---
atom_id: CA-P-1619
content_role: Plan
type: Plan
label: Task
work_sequence_number: 30
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Current Artifact query source admission rebind"
  depends_on: [Workflow, Action, Tool, Projection, Evaluation]
version: 1
updated_at: "2026-10-05 01:38:40 +0000"
relations:
  is_decomposition_of: [CA-P-1520]
  blocks: [CA-P-1527, CA-P-1528]
---
# Summary

Rebind current Artifact query source admission

## Objective

Within <=15 minutes, bind the existing W14 selected route to the independently accepted current source frontier without changing unrelated routes or bypassing source admission.

## Details

Inputs are CA-P-1618@1 and CA-O-158@4, accepted source-only in commit 88405e40e. Own selected_routes.py, the one selected_workflow_bindings.json Projection, and necessary admission regression tests only. Preserve W15, the other thirteen routes, the accepted registry, and closed manifest schema. Recompute canonical route-binding and manifest self-digests. Reject the old CA-P-1532 frontier even when its carrier is present and a candidate manifest is rehashed.

## Definition of Done

Independent source review accepts exact updated pins and canonical digests; focused development tests prove current frontier admission and stale-frontier rejection. This does not claim immutable-image, actual queue, current client cache, or full runtime acceptance.

## Result

Completed by /root/integrate_selected_native_providers; independently ACCEPTED read-only by /root/review_combined_query_tools.

W14 now pins CA-P-1618@1, SHA-256 bdf10c928c10c102dc489c8e3e526ffe73e8a33d492f4dabc8b5d0129c453b1f, and CA-O-158@4, SHA-256 d7fdaebdd1d0c6ca7dac9aced25552c487336f2a51f18c0f03ef65d16ff4618a. The route graph, W15 admission, other fourteen route objects, route order, and registry reference are unchanged. Exact expected-frontier equality, live byte pins, and closed admission schema remain enforced.

Saved implementation hashes:
- 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py: 272534ffcc46143ddd4b3073d76ee0f0b16d072d1cff181389c7f296cd893fd2.
- 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_selected_routes_mcp.py: 2cdbcb5939c154c53a199358883d5a1a196b04d2bb9def03f87c72fc42b8eb88.
- .caprmedio_caprmedio/_projection/selected_workflow_bindings.json raw carrier: 87b575d1c6b6f608fe5718f6922e79943f6deaff8e823fd827fe6d01be51b14d.
- selected_binding_digest: f945372d498c4b79f5d97466096a9b9fa1ae6b6a3791cc243203d9150e9271d9.
- canonical_manifest_sha256: 84491cf5372d6441b2d5bda50fde95587c12105a4e2c02c02d74fb17f7ba6106.

Eight focused existing-development-worker tests passed in 14.8 seconds combined: four MCP current-manifest/admission/preview/stale-frontier tests, two fifteen-route definition/freeze tests, and two GoldenRequests digest-bound/closed-query tests. The old-P1532 regression copies the actual historical receipt, retains current O158@4, recomputes the manifest self-digest, and fails with accepted-frontier mismatch rather than incidental stale bytes. The independent reviewer did not rerun tests; it independently verified source changes and canonical digests.

No new containers, host provisioning, queue execution, image functional proof, client schema refresh, or permission bypass occurred. C449 and C447 remain separate unfinished gates. Unrelated lifecycle candidate changes are not admitted by this review.
