---
atom_id: CA-M-343
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 22:00:58 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite test procedure"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Source Carrier, Compiled Candidate, JUnit Report, Writable Output]
relations:
  method_for: [CA-R-1886]
---
# Summary

Discover, run, and attest the declared Release suite

## Scope

The deterministic execution and source-attestation procedure for one sealed Release Version full-suite invocation.

## Claim

RELEASE_VERSION **must** use standard-library `unittest` discovery to derive the complete sealed in-tree Framework test-case set once, derive exactly one binding record with **>=1** sealed source reference for every discovered test ID from the maintained module rules, execute it once, and emit the observed JUnit result and source-read evidence.

## Details

1. Enumerate every sealed package-row carrier whose source path is `102_FRAMEWORK_ENGINE/**/test_*.py`, sorted by source path. For each module, use standard-library `unittest` discovery in a fresh child Python process with that module's parent as the start directory, its basename as the pattern, and `/workspace` as the working directory. Reject an empty module set, an unsafe or duplicate module path, an unavailable child process, or a test module that cannot be discovered.
2. Flatten the `unittest.TestCase.id()` values returned by all child processes and reject duplicate test IDs, an empty set, or a mismatch between the discovered test IDs and the JUnit test IDs. Each test ID has exactly one derived binding record containing its test-method definition carrier and the explicit probe sources for its module; that record has **>=1** source reference.
3. Load the immutable binding envelope from the read-only workspace and verify its exact SHA-256 from the sealed environment. The envelope contains the candidate manifest digest, the complete `compilation.package_rows`, and the maintained module-rule carrier and digest. Each derived referenced path and SHA-256 must equal a package row.
4. For each executed test case, read every source reference through the sealed workspace, verify its SHA-256, and emit its test ID, the envelope SHA-256, and one exact source-probe record per reference in JUnit properties. The bindings are source-attestation mappings, not a statement that the test provides complete code coverage.
5. Use maintained module rules rather than an import trace because compiled Methodology and Skill carriers need not be imported by Python. The rules contain only module-level explicit package probes; the test-module definition carrier is always derived. A maintainer adds a probe only when that module's test case exercises the source or a byte-and-digest probe is needed to establish its sealed-carrier integrity; the procedure must not mechanically mark arbitrary package components as covered.
6. Write **=1** JUnit testcase row per executed `unittest.TestCase.id()` and all temporary fixtures beneath the executor's writable output mount. Set `TMPDIR` to `/tmp` and `PYTHONDONTWRITEBYTECODE` to `1`; the procedure records only sealed repository-relative source paths, never host absolute paths, and it does not mutate the read-only workspace.
7. Any discovery error, missing declared module, unmapped test ID, unreadable carrier, digest or envelope mismatch, test failure, error, skip, missing compiled-candidate evidence, or incomplete required group ends the run without a passing full-suite result.

The existing RELEASE_VERSION Tool and its sealed full-suite environment invoke this procedure. This Method creates neither a selected Workflow nor an MCP route.
