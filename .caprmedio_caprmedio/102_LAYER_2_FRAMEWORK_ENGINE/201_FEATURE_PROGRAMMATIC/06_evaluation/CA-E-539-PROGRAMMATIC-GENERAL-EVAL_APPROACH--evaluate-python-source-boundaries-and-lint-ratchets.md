---
atom_id: CA-E-539
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:32:41 +0400"
subjects:
  governs: "python-source-boundary-admission"
  depends_on:
    - "programmatic software"
    - "Evaluation"
    - "Implementation"
relations:
  evaluation_for:
    - CA-M-162
    - CA-M-164
    - CA-M-282
---
# Summary

Evaluate Python source boundaries and lint ratchets

## Scope

new **or** materially changed hand-authored PROGRAMMATIC Python source **in**
Tools, App backend services, **and** MCP components.

## Claim

given changed-source measurements, the admitted pinned Ruff profile, diagnostics,
baseline, **and** bounded exception evidence, admit source-boundary conformance
**only when** **all** applicable size, cohesion, complexity, lint, **and** ratchet
conditions below hold. reject a violated condition; return unresolved **when**
required measurements, configuration, **or** exception authority are unavailable.

## Details

- target **`<=200`** physical lines per file **and** **`<=25`** logical lines per
  executable unit. units with 26–40 logical lines retain one coherent job;
  a larger file **or** unit requires one specific accepted bounded exception.
- the exception identifies measured size **or** failed rule, applicable maximum,
  reason, bounded scope, **and** reconsideration condition; a unit-size exception
  preserves a single responsibility.
- **every** changed executable unit has current cyclomatic-complexity evidence
  from the admitted `C901` profile. its value satisfies the admitted maximum
  materialized **in** canonical configuration **or** its accepted bounded exception.
- changed source passes the current pinned Ruff formatting **and** lint profile
  **or** records the bounded exception for the failed rule. an absent profile
  **or** unpinned checker yields unresolved conformance.
- a static mapping larger than 20 entries **or** 25 source lines is externalized.
  CA-M-162 owns the representation choice for that data.
- changed source does **not** silently regress below its admitted passing
  boundary. unmodified oversized legacy source **and** generated Runtime **or**
  Delivery outputs are outside this changed-source check.
- review cohesion, responsibility, dependency direction, **and** testability
  separately from size **and** complexity scores. reducing a score does **not**
  justify obscuring a separate responsibility **or** required recovery boundary.
  measurements guide diagnosis **and** do **not** independently prove quality.

this policy preserves the previously accepted CA-M-162, CA-M-164, **and**
CA-M-282 acceptance conditions under Evaluation ownership.
