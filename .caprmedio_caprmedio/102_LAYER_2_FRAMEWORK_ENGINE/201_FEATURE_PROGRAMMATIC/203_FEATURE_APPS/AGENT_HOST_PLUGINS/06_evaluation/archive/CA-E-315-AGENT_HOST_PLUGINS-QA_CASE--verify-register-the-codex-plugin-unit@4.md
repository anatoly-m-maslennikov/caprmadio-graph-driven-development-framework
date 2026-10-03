---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-197
---
# Verify register the codex_plugin unit

## Claim checked

CA-M-197 registers one CODEX_PLUGIN child under AGENT_HOST_PLUGINS without duplicating provider-neutral CAPRMEDIO Skill, Tool, or Methodology behavior.

## Applicable when

Apply whenever CODEX_PLUGIN structure, package boundary, or host wiring changes.

## Test case

Examine the current active AGENT_HOST_PLUGINS and CODEX_PLUGIN authority, using any available derived representation only as supporting evidence. Determine CODEX_PLUGIN's immediate typed ownership, identity, path, host-specific contents, and every reference to provider-neutral CAPRMEDIO behavior.

## Acceptance criteria

Exactly one immediate typed ownership edge connects AGENT_HOST_PLUGINS to CODEX_PLUGIN; its address and path are valid; its owned content is Codex-specific package or host wiring; and every provider-neutral CAPRMEDIO Skill, Tool, or Methodology behavior appears only as a reference to its existing owner.

## Failure disposition

Reject the registration and preserve the examined authority, any supporting derived representation, path evidence, and every duplicated or misowned behavior claim.
