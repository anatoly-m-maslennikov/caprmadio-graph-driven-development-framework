---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Upgrade Selected Atom Authority"
  depends_on:
    - "Action"
    - "Atom"
    - "Atom/Local Tier"
    - "Atom/Global Tier"
    - "Scope Unit"
    - "Artifact/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 3
updated_at: "2026-09-17 23:13:13 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Upgrade selected active Atom authority

Upgrade Selected Atom Authority **means** the reusable Action that produces the complete explicitly admitted higher-authority Carrier set under CA-R-870. its operational boundary is the full selected transition; a partially upgraded set is **not** an independently accepted result.

## Applicable when

use this Action **when** a caller prepares one active Atom **or** one frozen bulk set of two **or** more active Atoms for an explicitly supplied enabled higher `core` **or** `standard` Tier while retaining stable identity. actual upgrade is permitted **only** **when** an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Action

1. resolve **every** source as an active Atom **and** capture its current Tier, Scope Unit, stable ID, revision, **and** digest together with its explicit target Tier **and** optional target Scope Unit.
2. require **every** target Tier **to** be enabled, `core` **or** `standard`, **and** strictly higher than the source Tier; require the target Scope Unit **to** be the source unit **or** one explicitly named ancestor.
3. derive the target authority location **and**, **when** Scope Unit changes, the canonical filename scope segment while preserving the stable Atom ID **and** advancing revision metadata once.
4. validate target placement, authority relations, ID **and** destination collision freedom, **and** **every** complete resulting carrier; **then** publish the frozen dry-run map.
5. on explicit authorized `--apply`, recheck **every** source **and** destination precondition **and** perform the complete atomic **or** bulk upgrade as one rollbackable transaction.
6. verify that **=1** active carrier owns **every** stable ID at its approved higher Tier **and** that **every** former carrier is absent.
7. **if** an effect **or** postcondition fails, restore **every** selected mutable source **and** destination **to** its exact before-state. preserve unrelated Carriers, pre-existing history **and** immutable accepted Journal Records of actual effects. report the failed attempt **and** recovery result; incomplete **or** unverified restoration is **not** success.

## Outcome

**every** Atom retains its stable identity while its current authority is represented exactly once at the approved higher Tier.

## Failure or stop

remain **in** dry-run mode **without** delegated apply authority. stop **or** roll back on a non-active source, forbidden, disabled, **or** non-higher target Tier, invalid scope ancestry, collision, stale precondition, **or** failed uniqueness check.
