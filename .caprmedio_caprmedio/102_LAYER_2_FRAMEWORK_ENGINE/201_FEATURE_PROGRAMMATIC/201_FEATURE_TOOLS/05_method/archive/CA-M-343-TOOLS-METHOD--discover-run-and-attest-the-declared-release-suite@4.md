---
atom_id: CA-M-343
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-06 14:06:45 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Full suite test procedure"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Test Case, Source Carrier, Compiled Candidate, JUnit Report, Writable Output]
relations:
  method_for: [CA-R-1886]
---
# Summary

Discover, run, and attest the declared Release suite

## Scope

The deterministic closed Unit Gate execution and source-attestation procedure for one sealed Release Version candidate.

## Claim

RELEASE_VERSION **must** derive the sealed phase assignment once, use standard-library `unittest` discovery to derive and execute the complete `unit` test-case set once, derive exactly one binding record with **>=1** sealed source reference for every discovered Unit test ID from the maintained module rules, and emit the observed Unit JUnit result and source-read evidence.

## Details

1. Enumerate every sealed package-row carrier whose source path is `102_FRAMEWORK_ENGINE/**/test_*.py`, sorted by source path, and derive one phase assignment for each. `candidate_e2e` is exactly `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py`, and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py`; every other declared path is `unit`. Reject an empty suite, unsafe or duplicate module path, absent, duplicate, unknown, unsealed, altered, or out-of-set assignment. For each `unit` module, use standard-library `unittest` discovery in a fresh child Python process with that module's parent as the start directory, its basename as the pattern, and `/workspace` as the working directory. The three `candidate_e2e` modules are not Unit skips: their fixed separate procedure is CA-M-346.
2. Flatten the `unittest.TestCase.id()` values returned by all Unit child processes and reject duplicate test IDs, an empty Unit set, or a mismatch between the discovered Unit test IDs and the Unit JUnit test IDs. Each Unit test ID has exactly one derived binding record containing its test-method definition carrier and the explicit probe sources for its module; that record has **>=1** source reference.
3. Load the immutable binding envelope from the read-only workspace and verify its exact SHA-256 from the sealed environment. The envelope contains the candidate manifest digest, the complete `compilation.package_rows`, and the maintained module-rule carrier and digest. Each derived referenced path and SHA-256 must equal a package row.
4. For each executed test case, read every source reference through the sealed workspace, verify its SHA-256, and emit its test ID, the envelope SHA-256, and one exact source-probe record per reference in JUnit properties. The bindings are source-attestation mappings, not a statement that the test provides complete code coverage.
5. Use maintained module rules rather than an import trace because compiled Methodology and Skill carriers need not be imported by Python. The rules contain module-level explicit package probes for `unit` modules only; the test-module definition carrier is always derived. Exactly one rule, for `RELEASE_VERSION/tests/test_release_compilation.py`, sets `compiled_candidate_probe: true`. For that rule, select exactly the first source-path-sorted sealed METHODOLOGY package row beneath the bound compiled-candidate root and include it as an explicit byte-and-digest integrity probe. An absent flag means false. Reject non-boolean, duplicate or misplaced true flags and static probes beneath the runtime compiled root. A maintainer adds a probe only when that module's test case exercises the source or a byte-and-digest probe is needed to establish its sealed-carrier integrity; the procedure must not mechanically mark arbitrary package components as covered.
6. Before issuing the sealed Unit command, resolve the finite Unit execution budget from the captured CA-D-580 rows: `[release_suite].unit_timeout_seconds` from Framework Instance settings when present, otherwise the canonical default. Reject `bool`, non-finite, non-positive, and over-`7200` values. Write the private CA-D-579 `unit-deadline.json` snapshot and pass only the resulting bounded process deadline to the Suite Owner executor; a private fixture value may only shorten it. Then write **=1** Unit JUnit testcase row per executed `unittest.TestCase.id()` at `/output/coverage.xml`. Driver-owned result files use the writable `/output` mount; child-process temporary files use `/tmp` through `TMPDIR`. Set `PYTHONDONTWRITEBYTECODE` to `1`; neither class of writable data uses the read-only `/workspace`. The procedure records only sealed repository-relative source paths, never host absolute paths.
7. Any phase-assignment or discovery error, missing `unit` module, unmapped Unit test ID, unreadable carrier, digest or envelope mismatch, test failure, error, skip, missing compiled-candidate evidence, or incomplete required group ends the Unit Gate without a passing result. A passing Unit Gate is an image-build prerequisite only; CA-M-346 supplies the later candidate-image-bound E2E evidence and the Full Gate aggregates both actual results before promotion.

The existing RELEASE_VERSION Tool and its sealed closed Unit environment invoke this procedure without changing its schema-2 control-context digest, maintained probes, fixed CLI, or source-proof rules. A timeout, missing deadline carrier, invalid setting, or changed context is non-passing and retains N; it never drops a test, retries the suite, or creates a public override. This Method creates neither a selected Workflow nor an MCP route.
