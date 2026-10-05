---
atom_id: CA-C-461
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 05:49:29 +0000"
subjects:
  governs: "Which evidence proves declared full-suite coverage"
  depends_on: [Tool, Manifest, Evaluation, Runtime]
relations:
  concern_about: [CA-P-1688]
---
# Summary

Which evidence proves declared full-suite coverage

## Concern

Current Release authority requires an actual complete suite but does not define a machine-readable coverage result. Consider exit-code-only proof, parsing runner console prose, or retained standard JUnit XML from the actual declared command. Choose JUnit plus source-bound component coverage and exact suite-command/currentness evidence at88% design confidence. It avoids caller success flags and brittle console inference; missing or unsupported reports remain incomplete. Do not infer that one test file or passing Engine-only suite proves full Framework coverage. This chosen implementation format remains subordinate to E572 and is not actual Project full-suite evidence.

## Evidences

The sealed suite command/environment and accepted E572@2 require completeness; actual runtime proof remains separate.

## Blast radius

Release suite evidence only; no new independent source or runner provisioning.
