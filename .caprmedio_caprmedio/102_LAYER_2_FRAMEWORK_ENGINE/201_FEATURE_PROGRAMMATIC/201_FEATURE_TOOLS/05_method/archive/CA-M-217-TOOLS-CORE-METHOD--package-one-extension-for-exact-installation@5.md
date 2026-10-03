---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - extension-packaging
version: 5
updated_at: 2026-09-02 00:40:00 +0400
relations:
  method_for:
    - CA-R-1150
  derived_from:
    - CA-A-058
---
# Package one Extension for exact installation

## Applicable when

Use this Method when an accepted Extension candidate is ready to become an exactly installable package.

## Procedure

1. Seal the Extension identity, exact version, source Atom revisions, dependency contract, and compatibility boundary.
2. Assemble only declared authority, implementations, deliveries, and required package metadata into a deterministic manifest.
3. Build the package reproducibly from that manifest and record the manifest and package digests.
4. Compare the package contents with the manifest and reject any omitted, additional, or nondeterministic packaged item.
5. Delegate installation, uninstallation, update, downgrade, and installed-state verification to CA-M-252.

## Outcome

The Extension has one stable identity, exact version, deterministic manifest, and reproducible package digest.

## Failure or stop

Do not publish a package with unresolved dependencies, mutable version identity, nondeterministic contents, or a manifest-package mismatch.
