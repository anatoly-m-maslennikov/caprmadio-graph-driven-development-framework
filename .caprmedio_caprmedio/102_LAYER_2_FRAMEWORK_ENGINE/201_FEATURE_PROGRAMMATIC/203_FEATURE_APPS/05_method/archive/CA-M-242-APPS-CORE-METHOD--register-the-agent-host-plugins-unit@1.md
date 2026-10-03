---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 1
updated_at: 2026-09-02 00:21:00 +0400
relations:
  method_for:
    - CA-R-1101
  derived_from:
    - CA-A-058
---
# Register the AGENT_HOST_PLUGINS unit

## Applicable when

Use this Method when registering or changing the AGENT_HOST_PLUGINS Scope Unit owned immediately by APPS.

## Procedure

1. Resolve the active APPS authority and the current immediate-child Scope Unit declarations.
2. Register exactly one unordered immediate child with prefix `AGENT_HOST_PLUGINS`, Structural level `4`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS`, and the corresponding source path.
3. Assign the unit ownership of installable agent-host-specific plugin packages and their host wiring.
4. Require every provider-neutral CAPRMEDIO Skill, Tool, and Methodology behavior used by a host package to remain referenced from its existing owner rather than copied into this unit.
5. Confirm that the declaration has one immediate typed owner, one identity, and no duplicated provider-neutral responsibility.

## Outcome

AGENT_HOST_PLUGINS is one identifiable immediate APPS unit with the required boundary, address, realization path, and host-specific-only responsibilities.

## Failure or stop

Stop when AGENT_HOST_PLUGINS is missing, duplicated, non-immediate, ordered, assigned a conflicting address or path, or made an owner of provider-neutral behavior.
