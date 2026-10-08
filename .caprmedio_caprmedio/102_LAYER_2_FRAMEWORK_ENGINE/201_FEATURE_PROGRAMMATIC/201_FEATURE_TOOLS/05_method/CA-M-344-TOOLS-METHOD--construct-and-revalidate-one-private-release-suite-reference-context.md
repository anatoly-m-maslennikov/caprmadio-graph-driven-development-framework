---
atom_id: CA-M-344
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 14:06:45 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Private suite reference-context construction"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest]
relations:
  method_for: [CA-R-1887]
---
# Summary

Construct and revalidate one private Release-suite reference context

## Scope

The deterministic Suite-owner procedure for the control-reference closure outside the candidate package rows.

## Claim

RELEASE_VERSION **must** derive the private context only from current trusted internal candidate, compilation, selected-N, image-context, and source-admission handoffs; it must not accept a caller-selected path, digest, reference row, or success assertion.

## Details

1. Start from the trusted candidate manifest SHA-256, compiled-candidate root, frozen selected-N identity, and selected-N image-context identity already admitted to the suite invocation.
2. Read and validate the regular, non-symlinked roots: `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`, `.caprmedio_caprmedio/operators_registry.toml`, the current Project settings carrier, and the source-registry reference resolved by the selected manifest. Resolve the Release admission only through current CA-D-572; collect its declared acceptance, Workflow, Step, Action, and RMED pins and the source-path closure named by the selected manifest. Read CA-D-580's two exact Prompt binding carriers, verify their declared digests, then include only their explicit `sources` pins after checking current Atom identity, revision, status, path and byte digest. Include the exact canonical Framework default-settings carrier and Framework Instance settings carrier declared by CA-D-579; reject a duplicate declaration within a binding, an unknown binding, conflicting shared pins, or a missing, escaping, runtime, Journal, secret-shaped, or non-regular path. Union identical shared pins once, without arbitrary transitive discovery.
3. Sort the resulting typed `reference_rows` by source path, read each byte once before mounting, verify its SHA-256 and mode, and form `control_context_digest` from canonical JSON of the rows plus the trusted internal bindings. Copy only those verified bytes to their identical relative paths in the disposable workspace, then mount that closure read-only.
4. Issue the schema-2 private envelope and execute the already sealed suite command. The command receives no additional caller-controlled path or control input.
5. After execution, rederive the entire closure and trusted internal bindings from Project state. Require identical rows and `control_context_digest`; otherwise retain truthful non-passing evidence. The procedure never refreshes a changed input in place, replays a suite, or writes the canonical Project control carriers.

6. Before issuing the sealed Unit command, resolve the exact `[release_suite].unit_timeout_seconds` value from the captured bytes. An explicit Framework Instance value overrides the canonical default; an absent instance table/key falls back to the default. Accept only a finite numeric value that is not `bool`, is greater than zero, and is no greater than `7200` seconds. Write the derived private `unit-deadline.json` snapshot specified by CA-D-579 with the two source fingerprints, `control_context_digest`, configured seconds, and effective seconds; verify it against the captured context. A private fixture timeout may only shorten the configured value. This snapshot adds no public receipt or schema-2 field, and any source or context mismatch remains non-passing.
