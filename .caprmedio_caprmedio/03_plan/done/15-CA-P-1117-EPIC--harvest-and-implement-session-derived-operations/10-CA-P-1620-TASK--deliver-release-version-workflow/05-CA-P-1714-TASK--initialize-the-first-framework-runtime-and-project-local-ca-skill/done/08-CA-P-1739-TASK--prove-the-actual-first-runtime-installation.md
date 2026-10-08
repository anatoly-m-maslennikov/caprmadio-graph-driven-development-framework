---
atom_id: CA-P-1739
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-06 00:18:42 +0000"
subjects:
  governs: "First Framework runtime delivery/Prove the actual first runtime installation"
  depends_on: [Implementation, Evaluation, Framework Package, Methodology, Docker Image, Journal, Skill]
relations:
  is_decomposition_of: [CA-P-1714]
---
# Summary

Prove the actual first runtime installation

## Objective

Establish the actual complete Framework N and hook-free project-local ca Skill through the admitted explicit Action.

## Details

Require fresh canonical compilation, real immutable image build/inspection/canary and canonical started/terminal Journal evidence. Retain old Runs and rollback data. If permissions deny a real operation, preserve its actual state and leave this Task Active. Expected bounded effort: <=15 minutes; decompose further if necessary.

## Definition of Done

The actual admitted installation and its current package, Skill, selector, immutable image and canonical Action proof are independently verified. Source and mock evidence alone do not satisfy this Task.

## Actual first-N acceptance

Run `first-framework-runtime-20261006-03` completed the admitted O180 installation. Independently verified package and selector SHA `6f2e3a615a4f4d6da0f16831800f9e4b7ff84f89b89faeefc359f51711d28c57`: all 15,135 package rows match exact bytes, modes and complete path set (694 Engine, 14,439 Methodology and two Skill resources). Public `.agents/skills/ca` has exactly the two hook-free packaged files.

Immutable image `sha256:79899cfe59fb36c8da5ce1c12ea52c529a61738e51100b3d3e8488c52496d54e` passed actual build, inspection and complete-package/MCP canary, all exit 0 with no timeout. The canary verified 15,135 files and 28 MCP Tools; independent acceptance reopened retained receipts and performed a fresh read-only immutable-image inspection. Bootstrap receipt SHA: `b804cc3800566489ee875ce25e5be6be742cc46ec7ad5f3503a2851f10606e59`.

Canonical started/completed Action facts and persisted receipts match the exact immutable installation intent and all four effects. Completed event: `.caprmedio_caprmedio/_journal/anatoly-m-maslennikov-2026-10-06-part-1.ndjson`, line 2, digest `203fa0be69330ec6531738e2749b11b66e60577b11022e5409361431cf4632f1`. The retained result's pre-terminal `published_pending_terminal` state is closed by this canonical terminal fact, not relabeled as an independent final-state ledger.

This closes CA-P-1739's first-install scope only. N-to-N+1 complete-suite, candidate E2E, promotion and deferred retirement remain separate unfinished Release gates; installed N remains immutable and available as the working baseline.
