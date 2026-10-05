---
atom_id: CA-C-472
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 16:49:29 +0000"
subjects:
  governs: "Release suite isolation"
  depends_on: [Implementation, Skill, Methodology, Evaluation, Image, Manifest]
relations:
  concern_about: [CA-P-1717, CA-R-1879, CA-E-574]
---
# Summary

Isolate Release tests from the executing runtime

## Concern

The Release suite runs its selected command against the authoritative Project root. It detects changes to the executing runtime N, selector, source files or active ca Skill only after execution, instead of preserving those carriers during the test.

## Evidences

/root/checkpoint_integration_review independently rejected `RELEASE_VERSION/release_suite.py` against CA-R-1879 and CA-E-574: the command can mutate the real root, and the subsequent stale check does not prevent or restore those writes.

The local repair now has **9** focused adapter passes, including explicit sealed-command entrypoint override, restricted mounts, symlink/leaf-path rejection, bounded timeout recovery, and incomplete evidence when identity cannot be verified. Immutable-image bootstrap checks passed **2** cases and generic suite-boundary checks passed **2** cases. These checks do not prove an installed-N Docker run.

The complete retained-suite run still stops before executor invocation: `release_compilation.py:313` receives `EPERM` from `os.replace`. An earlier Action O174 `deliver_sources` attempt also stopped at a rename `EPERM`. Both conditions leave actual full-suite evidence unavailable.

## Blast radius

Release test execution and its promotion gate. Exact prior-image retirement received bounded static acceptance, not actual image-execution proof. The complete suite, installed-N image PATH integration, and delivery/compilation publication gates remain unproved. Other independent source, recovery and publication implementation may continue.

## Decision

Execute the complete declared suite behind the repaired isolation boundary once the EPERM delivery and compilation gates permit it. Canonical sources, executing N and active ca must remain unavailable or read-only, with a separate writable fixture/report area. Retain post-run currentness checks as race detection, not preservation. Existing CA-R-1879 and CA-E-574 govern this repair; no smaller suite or mock-only proof substitutes for the required real test gate.
