---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - extension-packaging
    occurrent:
      - evaluation
version: 5
updated_at: 2026-09-02 00:40:00 +0400
relations:
  evaluation_for:
    - CA-M-217
---
# Verify package one extension for exact installation

## Claim checked

CA-M-217 produces a reproducible exactly versioned Extension package whose manifest exactly accounts for its package contents.

## Applicable when

Apply whenever Extension packaging, manifest, versioning, or package-content derivation changes.

## Test case

Package the same sealed Extension candidate twice, compare manifests and package digests, then compare each package inventory with its manifest without performing an installed-state operation.

## Acceptance criteria

Both builds have identical identity, exact version, manifest, and package digest; each package inventory matches its manifest exactly. Installation, uninstallation, update, downgrade, and installed-state verification are delegated to CA-M-252.

## Failure disposition

Reject the package and preserve candidate frontier, both builds, manifests, digests, package inventories, manifest comparisons, and delegation boundary.
