---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - extension-packaging
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1151
  derived_from:
    - CA-A-058
---
# Resolve GitHub Extension source

## Applicable when

Use this Method when determining the declared GitHub source boundary for one Extension package.

## Procedure

1. Resolve the declared GitHub repository for one Extension and determine whether its package root is the complete repository or one declared directory.
2. Normalize the repository identity and optional declared directory without inventing an implicit subdirectory or alternate source provider.
3. Retrieve the source boundary and report the declared repository and package-root path as attributable source metadata.
4. Reject a missing repository, undeclared subdirectory, or source boundary that cannot be mapped to the Extension package.
5. Return source-resolution facts only; do not choose an installed version or change installed Extension state.

## Outcome

One Extension has an exact attributable GitHub repository source boundary and either its complete repository or one declared package-root directory.

## Failure or stop

Stop on an ambiguous repository, undeclared package root, missing source boundary, or an attempt to manage installed state.
