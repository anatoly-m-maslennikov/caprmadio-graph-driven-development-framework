---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Package Extension"
  depends_on:
    - "Action"
    - "Extension"
    - "Artifact/Carrier"
    - "Artifact/Revision"
version: 12
updated_at: "2026-09-17 03:40:16 +0000"
relations: {"evaluation_for":["CA-R-1150","CA-O-044"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify package one extension for exact installation

## Claim checked

CA-O-044 produces a reproducible exactly versioned Extension package whose manifest exactly accounts for its package contents.

## Applicable when

apply whenever Extension packaging, manifest, versioning, **or** package-content derivation changes.

## Test case

package the same sealed Extension candidate twice, compare manifests **and** package digests, **then** compare each package inventory with its manifest **without** performing an installed-state operation.

## Acceptance criteria

both builds have identical identity, exact version, manifest, **and** package digest; each package inventory matches its manifest exactly. installation, uninstallation, update, downgrade, **and** installed-state verification are delegated **to** CA-O-042.

## Failure disposition

reject the package **and** preserve candidate frontier, both builds, manifests, digests, package inventories, manifest comparisons, **and** delegation boundary.
