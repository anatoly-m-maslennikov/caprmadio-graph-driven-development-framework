---
atom_id: CA-E-573
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Installed-delivery QA"
  depends_on: [Tool, Runtime, Methodology, Skill, Image, Manifest]
relations:
  evaluation_for: [CA-R-1877, CA-R-1878, CA-M-332]
---
# Summary

Verify installed runtime, Skill, and candidate-image evidence

## Scope

Post-suite-gate evidence for a separately retained complete derived runtime, project-local `ca` Skill without hooks, and actual candidate image before public promotion.

## Claim

After CA-E-572 passes, the QA case **must** prove exact separately installed N+1 package and runtime Methodology bytes against the sealed manifest, one staged reviewed project-local `ca` Skill copy without host-hook change, and execution of the actual candidate image by immutable image identity; active runtime selection and public Skill remain N until every promotion gate passes. File presence, image build success, or an Engine-only install is insufficient.

## Details

The case separately records unsupported client target, unavailable image runtime, or missing full Framework installer surface as blockers. It does not infer a successful installation from a dry run.
