---
atom_id: CA-P-108
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Methodology Migration Map
    occurrent:
      - Bootstrap Migration
  depends_on:
    occurrent:
      - CA-P-107
version: 1
updated_at: 2026-08-26 04:35:53 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Freeze the Bootstrap-to-Methodology Migration Map

**when** CA-P-107 is Done, **then** the Assignee **must** freeze one complete source-to-target disposition and carrier map for every governed item in the Bootstrap, .caprmedio, .caprmedio_install, and framework-consumer migration frontier.

## Scope

`(the exact frozen source frontier from CA-P-102 plus every accepted successor, target ownership root, target source Layer, target Content-role folder, target filename, relation rewrite, generated Projection, configuration entry, active Plan disposition, Journal boundary, and Tool, MCP, App, or Skill consumer required by CA-P-103 through CA-P-107)`

## Definition of Done

the Task is **not done if** (any source item lacks exactly one retain, move, rename, replace, archive, cancel, done, or defer disposition **or** any active Bootstrap Plan lacks an exact disposition and successor mapping **or** any .caprmedio or .caprmedio_install carrier lacks exactly one framework, project, runtime, archive, or retirement target **or** any target collision exists **or** any Current Scope, Claim Scope, Subject, relation, Atom ID, Summary, version, archive path, or source frontier consequence is unresolved **or** byte-preserving carrier moves are mixed with Claim revisions without separate dispositions **or** rollback cannot restore every pre-migration carrier **or** the mapping mutates a governed source).

## Details

record exact source and target paths and content digests. keep pure carrier migration separate from governed Claim replacement. preserve all Plan lifecycle history and explicitly disposition obsolete Bootstrap carriers, the old .caprmedio ownership root, and .caprmedio_install. protect 000_APPLICABLE_MTHD_sources from generated-output cleanup.
