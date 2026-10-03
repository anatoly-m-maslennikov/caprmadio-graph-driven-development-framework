---
atom_id: CA-E-224
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-857
    - CA-M-104
  check_of:
    - CA-D-012
---
# Reject a service dependency outside the installation

## Claim checked

A registered background service cannot load framework implementation from the canonical source, runtime, or another project path.

## Test case

Install a service registry whose Python command addresses a script in the repository outside `.caprmedio_install`; invoke dry-run.

## Acceptance criteria

The Tool returns one stable dependency-boundary diagnostic before starting a process or creating service runtime state. Git, governed source, installation, registry, runtime, and the external script remain byte-identical.

## Failure disposition

Reject delivery if the external script is accepted, read as framework dependency, copied implicitly, or started; or if rejection mutates project state.
