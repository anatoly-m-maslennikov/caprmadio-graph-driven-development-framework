---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:21:00 +0400
relations:
  evaluation_for:
    - CA-M-242
---
# Verify register the AGENT_HOST_PLUGINS unit

## Claim checked

CA-M-242 registers AGENT_HOST_PLUGINS as one immediate unordered APPS unit with the exact required boundary and no provider-neutral CAPRMEDIO authority.

## Applicable when

Apply whenever AGENT_HOST_PLUGINS's APPS ownership, structural identity, responsibility boundary, or realization path changes.

## Test case

Examine the current active APPS and AGENT_HOST_PLUGINS authority, using any available derived representation only as supporting evidence. Determine whether the AGENT_HOST_PLUGINS declaration has one immediate typed owner, the declared prefix, level, address, path, host-specific responsibility boundary, and provider-neutral non-duplication condition.

## Acceptance criteria

AGENT_HOST_PLUGINS is the sole matching immediate unordered child of APPS at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS` and realized at its declared source path; it owns installable agent-host-specific packages and host wiring, while every provider-neutral CAPRMEDIO Skill, Tool, and Methodology behavior remains a reference to its existing owner.

## Failure disposition

Reject the AGENT_HOST_PLUGINS registration and preserve the examined authority, any supporting derived representation, the observed owner and identity facts, and every missing, duplicate, or copied provider-neutral claim.
