---
atom_id: CA-P-1103
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
    - CA-P-1104
---
# Validate Project Structure migration

the Assignee **must** verify that caprmedio's Project Structure migration is complete **and** preserves the agreed single-source boundary.

## Scope

the complete caprmedio structural migration result **and** its selected authority, manifest, Tool consumers, Settings boundaries, Goals, Carrier bindings, **and** Applicable Methodology; validation is read-only apart from its own permitted evidence.

## Definition of Done

the Task is **not** Done **if** (any non-cancelled Epic Task remains incomplete **or** an inventory disposition is unresolved **or** duplicate source authority survives **or** a Goal/reference/consumer fails **or** a declared unit is hidden **or** repeat validation/rebuild changes authoritative inputs **or** recovery evidence is insufficient).

## Details

check the accepted 11-field row shape, optional order/mode semantics, root-parent reference, uniqueness, acyclic parentage, structural/navigation independence, readability consistency, concrete path ownership, **and** per-Project isolation. confirm no Name/Order declaration Atoms **or** concrete binding D Atoms remain active **as** competing sources; preserve distinct valid Claims rather than treating every mention **as** duplication.

verify all admitted units **and** source dispositions, current Tool entry points, current derived outputs, preserved historical revisions, **and** no accidental completion of other Epics. rerun the applicable validations **and** use the earlier controlled rebuild results **to** check idempotence/currentness **without** requiring byte-identical timestamps. disclose any unresolved issue **and** leave this Task/Epic open. mark the Epic complete **only** after every Task's Definition of Done is satisfied; creating the plan never counts as execution.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

current scope correction: do **not** require **or** build a separate Project Structure Projection. validate direct consumers of `project_structure.toml` **and** removal of the retired structural-Projection dependency. CA-P-1102 is Cancelled; CA-P-1104 is the direct prerequisite. unrelated graph Projections remain outside this Epic unless explicitly affected **and** separately authorized.
