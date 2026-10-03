---
atom_id: CA-M-166
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - compatibility-boundary
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 01:45:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Preserve declared interface compatibility boundaries

Preserve or explicitly replace each declared PROGRAMMATIC interface or host
compatibility boundary; do not infer a broader support claim from
local use, stale workflow configuration, or one implementation.

## Applicable when

Apply when a Tool, App backend service, or MCP component changes a declared
technical interface, host integration, transport, or dependency-facing
interface boundary.

## Procedure

1. Identify the current Requirement, technical contract, or pinned external
   origin that declares the affected interface boundary.
2. Preserve its declared behavior or obtain an accepted bounded replacement
   before releasing the change.
3. Keep component-specific interface details at the child Scope that owns
   them.
4. When no current boundary exists, record the absence rather than claiming
   platform or cross-host compatibility.

## Outcome

Every compatibility claim has one current authority and remains limited to its
declared interface surface.

## Failure or stop

Stop release or compatibility claims when the affected interface boundary has
no current authority, pinned external origin where one is required, or
accepted replacement.

## Sources

- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
