---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Package Extension"
  depends_on:
    - "Action"
    - "Extension"
    - "Artifact/Carrier"
    - "Artifact/Revision"
version: 1
updated_at: "2026-09-17 03:40:16 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Package one Extension for exact installation

Package Extension **means** the reusable Action that produces one verified, exactly versioned, reproducible Extension package **without** changing the installed state under CA-R-1150. its modeled boundary is the complete requested result; partial comparison, incomplete attribution, **or** an unreported unresolved input is **not** an independently successful outcome.

## Applicable when

use this Action **when** an accepted Extension candidate is ready **to** become an exactly installable package.

## Action

1. Seal the Extension identity, exact version, source Atom revisions, dependency contract, **and** compatibility boundary.
2. Assemble **only** declared authority, implementations, deliveries, **and** required package metadata into a deterministic manifest.
3. Build the package reproducibly from that manifest **and** record the manifest **and** package digests.
4. Compare the package contents with the manifest **and** reject **any** omitted, additional, **or** nondeterministic packaged item.
5. finish packaging **without** changing installed state. installation, uninstallation, update, downgrade, **and** installed-state verification belong **to** the separate CA-O-042 Action; packaging does **not** invoke that Action as a required final step.

## Outcome

the Extension has one stable identity, exact version, deterministic manifest, **and** reproducible package digest.

## Failure or stop

Do **not** publish a package with unresolved dependencies, mutable version identity, nondeterministic contents, **or** a manifest-package mismatch.
