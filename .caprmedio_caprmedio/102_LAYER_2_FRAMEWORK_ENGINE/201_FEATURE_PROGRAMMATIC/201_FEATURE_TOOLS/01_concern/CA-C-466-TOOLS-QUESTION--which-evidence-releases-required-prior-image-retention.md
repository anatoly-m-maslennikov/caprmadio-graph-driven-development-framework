---
atom_id: CA-C-466
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 07:05:54 +0000"
subjects:
  governs: "Prior-image rollback retention"
  depends_on: [Image, Manifest, Action, Framework Instance Settings, Evaluation]
relations:
  concern_about: [CA-P-1697, CA-O-169, CA-R-1880]
---
# Summary

Which evidence releases required prior-image retention

## Concern

O169 requires an approved rollback-retention condition before exact prior-image removal, but the current implementation has no admitted producer for that condition. Successful promotion and a retained historical selector alone do not prove whether an old image remains required for rollback.

## Evidences

R1879 retains N as the runnable rollback point until promotion; R1880 and O169 additionally require proof that no container or required rollback reference retains the old image before removal. P1693 retains the exact prior selector and Skill evidence, not an approved release-of-retention record.

## Blast radius

Only P1697's retirement decision and later Release provider integration. Candidate preparation, delivery, compilation, testing, staging, image verification and promotion remain independently implementable.

## Decision

P1704's first source review REJECTS D573@1 at94% because completed verification can be failed or partial and same-candidate successful terminal records were not explicit. P1705 repairs only that ambiguity before source admission or removal implementation. This does not change the chosen authoritative-settings boundary or authorize any image effect.

Options are to infer that promotion ends retention, require an explicit approved condition, or silently invent a registry. Choose the explicit-condition boundary at88% confidence: observe exact completed promotion and container/reference evidence; retain the image with a truthful pending outcome when approved retention release is absent or unknown. Preserve historical selector evidence rather than delete it to manufacture proof. Implement the safe reader/refusal path now and retain the bounded source/provider binding as required remaining work. Do not ask the Operator or perform an actual image operation.
