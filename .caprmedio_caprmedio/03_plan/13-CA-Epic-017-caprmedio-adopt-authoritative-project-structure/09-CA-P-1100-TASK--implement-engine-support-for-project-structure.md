---
atom_id: CA-P-1100
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-15 00:07:17 +0000"
relations:
  depends_on:
    - CA-P-1099
---
# Implement Engine support for Project Structure

the Assignee **must** implement the Engine's specified Project Structure support **and** verify it against the candidate.

## Scope

FRAMEWORK_ENGINE Implementation **and** tests for the consumers selected under CA-P-1099, including their selected project-local execution entry points; the caprmedio candidate is a read-only integration fixture.

## Definition of Done

the Task is **not** Done **if** (an admitted consumer still independently selects structural truth **or** an invalid structure passes the applicable tests **or** a permitted read mutates source authority **or** an installed/selected entry point silently executes incompatible behavior **or** failed writes leave mixed authoritative state).

## Details

implement applicable E tests before required behavior where prerequisites permit; apply the current programmatic M authority **and** D boundaries. cover parent/name references, readability-field consistency, Type/order rules, Settings defaults plus explicit unit overrides, method/source-unit discovery, path exceptions, missing/orphan materialization reporting, deterministic projections, authorized mutations, rename/reparent reference repair, **and** interrupted-update recovery.

reuse the declared schema/model rules; do **not** hard-code this Project's unit roster. check cross-Project isolation **and** declared/observed divergence. test the candidate in a controlled work area **without** activating it. use canonical implementations unless a scoped project-local install update is required by the accepted consumer map; no hooks, host-profile mutation, unrelated upgrades, **or** live Project topology changes are included. record exactly which entry points were tested **and** retain any deployment blocker for cutover.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

current scope correction: Project Structure consumers read `project_structure.toml` directly. migrate consumers away from the existing structural graph Projection; do **not** implement **or** retain an automatic structural-Projection rebuild as the new source-resolution path. optional graph visualization capabilities are **not** required by this Epic.
