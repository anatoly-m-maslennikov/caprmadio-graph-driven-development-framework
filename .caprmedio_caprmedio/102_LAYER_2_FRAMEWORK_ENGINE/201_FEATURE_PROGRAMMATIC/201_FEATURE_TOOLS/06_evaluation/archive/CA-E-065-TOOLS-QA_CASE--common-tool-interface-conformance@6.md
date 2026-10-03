---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-23 17:53:53 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1063
    - CA-R-1064
    - CA-R-1065
    - CA-R-1066
    - CA-R-1067
    - CA-M-144
---
# Common Tool interface conformance

## Claim checked

Every registered Tool is discoverable and invocable through one common interface while capability-specific safety and targeting obligations remain enforced.

## Applicable conditions

1. Ask the router for representative Finder, Checker, source-editing Doer, and Projection-materializing Doer intents and require every applicable option plus sufficient machine-readable how-to after selection.
2. Validate identical capability, help, input-schema, result-envelope, diagnostics, and exit-status fields for every registered Tool.
3. Resolve targets independently from structural-unit, Type, and subtype filters and from explicit Atom filenames, and require the same stable target set before execution.
4. Snapshot all Atom bytes, run every Finder and Checker fixture, and require no Atom, relation, lifecycle, or authoritative carrier change.
5. Run every source-editing Doer fixture in dry-run mode, require complete planned effects and validation results with no mutation, then apply an approved plan and require the realized effect to match it.
6. Run representative Projection-materializing Doer fixtures first in dry-run mode and then in apply mode, and require writes only to declared governed Projections or non-authoritative runtime rendering outputs.
7. Inspect every process environment and dependency resolution path. Require
   executable Tool code and shared libraries to resolve only from the selected
   project-local release under `.caprmedio_install`, and require
   `.caprmedio_runtime` to contain only mutable state with no executable Tool
   implementation or Tool-specific environment.

## Acceptance criteria

Every Tool conforms to the common contract, resolves identical targets, and satisfies its registered capability boundary without undeclared writes.

## Failure disposition

Reject Tool registration or execution, identify the first divergent interface or unauthorized effect, and record a Concern before Tool-surface readiness.
