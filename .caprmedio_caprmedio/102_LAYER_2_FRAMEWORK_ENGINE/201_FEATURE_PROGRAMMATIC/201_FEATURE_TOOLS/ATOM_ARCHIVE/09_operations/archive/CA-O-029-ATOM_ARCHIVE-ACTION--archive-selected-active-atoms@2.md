---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Archive Selected Active Atoms"
  depends_on:
    - "Action"
    - "Tool/ATOM_ARCHIVE"
    - "Atom"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 2
updated_at: "2026-09-17 03:42:35 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Archive selected active Atoms

Archive Selected Active Atoms **means** the reusable Action that withdraws the selected active Atom authority as **=1** all-or-nothing archive transaction while preserving its exact historical Carriers. its modeled boundary is that withdrawal transaction: a partially archived selected set is **not** a useful independently successful outcome.

## Applicable conditions

- select **=1** active Atom **or** a frozen bulk set of **>=2** active Atoms.
- actual archival requires an authorized Project-local MCP delegation with a sealed Initiative action envelope. a preview grants no apply authority.
- preserve the Atom ID, Version, content, Summary, prior history, **and** resolvable historical dependents. derive the archive location **and** basename from the applicable Delivery authority under CA-D-289 **and** CA-D-303; byte preservation does **not** require an unchanged active basename.

## Action

1. resolve **every** selected Atom uniquely, establish its active classification **and** owning Content Role, **and** retain its exact path, ID, Version, digest, **and** historical references as preconditions.
2. derive **=1** role-local archive destination per target using the required `@<version>` suffix. reject Drafts, already archived Carriers, non-Atoms, invalid destinations, collisions, repeated targets, **and** stale targets.
3. freeze the complete source-to-destination map **and** return its mutation-free dry run.
4. on explicit authorized `--apply`, recheck **every** source **and** destination precondition. move the complete selected set as **=1** rollbackable transaction **and** exclude it from current-authority discovery.
5. verify exact archived bytes, unchanged ID **and** Version, correct archive basename, absence from the active locations, **and** retained historical resolution.
6. **if** an effect **or** postcondition fails, restore **every** selected mutable source **and** destination **to** its before-state; preserve unrelated Carriers **and** immutable accepted Journal evidence. report the failed attempt **and** recovery result rather than archive success.

## Outcome

success requires the complete selected set **to** be archived, historically resolvable, **and** absent from current authority. remain **in** dry-run mode **without** delegated apply authority. stop **or** roll back the full set on a failed lifecycle, source, destination, collision, **or** postcondition check; incomplete **or** unverified restoration is **not** successful recovery.
