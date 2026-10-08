---
atom_id: CA-P-1672
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Review actual Release child compiler"
  depends_on: [Atom, Workflow, Action, Tool, Manifest, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 04:42:52 +0000"
relations:
  is_decomposition_of: [CA-P-1623]
  blocks: [CA-P-1643]
---
# Summary

Review actual Release child compiler

## Objective

Within <=15 minutes, review actual Release child compiler.

## Details

Independent read-only review of P1650's actual release_compilation.py and its four real-compiler golden cases against D561/D566/D567/D571@2 and E572@2. Verify effect-free expected-byte prediction before sealing; actual executing compiler identity; immutable source/currentness and child-only safe output; equality before trusted handoff; source-conflict/stale/compiler-mismatch/symlink-parent refusal. Inspect actual code/source, not only test counts. No full Release, new environment/image, C447 workaround, source/code/Plan/Git edits or broad audit.

Choose the best authorized in-scope option when uncertain; record C/Question and continue. Preserve other agents' work. C447/C449 and actual permission/evidence boundaries remain unchanged.

## Definition of Done

Save the bounded result with exact current source/code hashes, actual evidence and remaining coverage. This leaf never completes full runtime/image gates or the Epic.

## Result

Independent review REJECT: actual compile_report frontier 77096bedd879cecc4a0f37e4271cfb946ed3d3afd9b7b64036ffcd16a49b47a7 differs from canonical source/tree digest 46433c1ab8aaa4fe5192b2a62f74db23f5debb8fc92b5846c930f0600c89ab3a in the disposable fixture. D571 child payload records the former; typed evidence/seal currently require the latter under the compiler frontier name. Actual compiler identity, expected-output prediction, unsafe-parent refusals and source/Projection preservation are otherwise aligned; four real-render cases pass. P1650 reopens for precise frontier alignment and actual equality/refusal tests. This rejected review does not authorize downstream Release integration.

### Current review

Independent review of the repaired exact bytes ACCEPTS the narrow compiler lane. release_handoff.py SHA-256 3866a58049fea78a473fcd7d8e577f6335757910ca5182e27228638253b0da82, release_compilation.py 3943af4a3b344d68b1dc9d61b2b07d0db38038e7b3e1e6e3101908567fa5caab and test_release_compilation.py 376d95ea3ac2bdeafd5edaa96d9a4adf0e887608b13805065a8c9f326d90e844 now bind the report frontier consistently while retaining separate canonical-tree currentness. Five actual compiler and thirteen handoff tests pass, including forged-frontier refusal before child creation. This supersedes the prior rejected bytes only; full Release integration, source admission, image and Journal gates remain required.
