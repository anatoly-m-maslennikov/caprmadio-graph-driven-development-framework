# Source Reconciliation extraction and replacement-event support

Non-authoritative execution evidence, 2026-09-14 01:48:45 +0400. The Operator approved the M224 extraction, the one-time M274 Git deferral, and the required replacement-event payload/validator support. No other Task is executed or closed.

## Changes

- R1462 admits Action and Process as open Ops definition-Atom Types; D433 and D434 specify their filename tokens and authoritative placement.
- O004–O009 define selection, conflict assessment, correction proposals, actual Operator decisions, authorized upstream corrections, and reconciled publication. O010 defines their explicit bounded Action flow. O011 preserves the named Applicable Methodology Compilation target and binds the same flow without duplicating its Actions.
- E379 v11→v12 preserves its full criteria/fixture body and existing R targets; evaluation_for changes M224 to O011 under already-active R1018 v9.
- M224 v12 moves byte-for-byte to its @12 archive after all eight O successors are Active. R/D prerequisites and E379 are not replacement successors.
- D435 specifies paired predecessor_atom_id/successor_atom_ids fields on the archiving event; E462 supplies format and evidence-binding checks. The existing schema-3 Journal validator accepts this optional pair without changing ordinary or historical events. It is one event in the existing Journal, not a separate log or authoritative source map.
- P1086 v11 records this bounded work and stays Active. Its previous v10 is preserved. The remaining 15 reserved source dispositions and other Task gates are unchanged.

## Exact M224 behavior coverage

| Original clause | Preserved source responsibility |
|---|---|
| 1–3: complete registered current selection, Settings activation, every eligible exact revision, unknown conforming contents, empty extension handling | O004 selection Action + O011 selection binding; reuse R1228/R1315/R1434; E379 body unchanged |
| 4: exact ID/revision/owner/Claim; no synthesis/merge | O009 publication + O011 publication binding; reuse R1314/R1316/R1461 and D305/D306/D313 |
| 5: all five conflict categories; no silent discard | O005 assessment + O011 assessment binding; reuse R1373/R1375; E379 body unchanged |
| 6–7: deterministic exact-frontier digest and complete report before membership changes | O011 assessment binding; O010 routes assessment before publication |
| 8: exact recorded Operator approval, separately authorized upstream correction, reselection/recheck after changes, no unapproved Core override | O006 proposal, O007 actual Operator decision, O008 gated source correction, O010 explicit re-evaluation loop, O011 specific approval/authority binding; reuse R1317/R1375 |
| 9: unresolved or invalid approval fails without membership change | O005/O007/O008 gate outcomes + O009 publication + O010 blocked branches + O011 fail-closed membership binding |
| 10: no source-order, synthesis/merge or LLM resolution | O005 assessment; O006 non-authorizing proposal; O011 source-specific binding |
| 11: same ordered membership from same resolved frontier | O011 publication binding; E379 existing deterministic-membership criterion unchanged |

Six Action boundaries correspond to independently governed outputs: exact selection; conflict assessment; proposed change; actual human decision; authorized source mutation; derived publication. Proposal, approval and mutation must not collapse across their distinct authority boundaries. Normal re-evaluation reuses selection/assessment; retries and escalation remain explicitly bounded by applicable authority, with no invented universal retry count or flow schema. No pure Method choice remains in M224: no algorithm, library or implementation convention is selected by it, so no M successor is fabricated.

R1462 supplies open Action/Process definition-Atom Type admission; D433 supplies the two filename Type tokens; D434 supplies authoritative 09_ops placement separately. Legacy GOV752/D403 stay unchanged. Already-active R1018@9 permits evaluation_for to target Requirement, Method, Evaluation, Delivery and Ops, retaining all ownership, checked-authority and tier/cardinality guards; its stage-15 revision and E447@5 remain untouched. E379 consequently replaces only M224 with O011 among its evaluation_for targets, preserving its existing R targets; it also depends on Applicable Methodology Compilation. Its validation target and entire criteria/fixture body remain byte-identical. O011 preserves M224's existing Applicable Methodology Compilation governed Process identity, retaining the parent target used by R1316/R1317 and E379; its Source Reconciliation dependency reuses O010's same Action flow without a Process-in-Process node or alias. The earlier RMD-only workaround is superseded, not applied. No universal self-evaluation/cycle policy or global Subject cleanup is introduced.

M224 is an actual replacement under R1432, with all eight O successors named in its replacement lineage. The Operator's one-time M274 exception defers the prescribed Git commit ordering for this extraction only. Exact M224@12 bytes move to its archive and actual replacement provenance must be journaled; no retrospective event, broad exception, M274 rewrite or Git mutation is authorized. R/D prerequisites and E379 are not falsely recorded as M224 successors.

## Verification and limits

The source frontier is 1,566 + 13 new sources - M224 = 1,578. E379 is revised, not a new source. Exact source hashes, prior revisions, 53 excluded Drafts, 16 previous source maps, other Tasks, and unrelated baseline files are checked. All prior Journal bytes and the raw Git index remain unchanged; new events append with current timestamps. Tool prior bytes are bound to immutable Git commit `29b861b0d34369918336645a0f8d30cecb1c8e70`, not reconstructed historical authorship or times.

Tool verification supplied by its implementation worker:

```json
{
  "schema_version": 1,
  "task": "Bounded schema-v3 Journal replacement payload validator support",
  "repository": "/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework",
  "runtime": {
    "python": "CPython 3.14.7",
    "prefix": "TMPDIR=/private/tmp UV_PROJECT_ENVIRONMENT=/private/tmp/ca-p-1086.ACurlj/tool-check-venv PYTHONDONTWRITEBYTECODE=1 uv run --locked --python 3.14 python -B",
    "warnings": [
      "Current pyproject.toml lacks requires-python; uv reports default >=3.14. Explicit --python 3.14 selects supported series.",
      "Current pyproject.toml declares standard-library-only runtime but has no admitted Ruff or Mypy profile, target set, or pinned development dependencies."
    ]
  },
  "path_map": [
    {
      "source": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py",
      "before_snapshot": "/private/tmp/ca-p-1086.ACurlj/tool-before/work_journal.py",
      "before_sha256": "e8c133608ff56cdbb6a7a62b59c74f06a8de5c2e899ab89a4aa581ae1e45c643",
      "after_sha256": "7b49f15fc33b12e6529b873dbb3ce6174cc368e063d70637004b32813d3874f9",
      "insertions": 62,
      "deletions": 0
    },
    {
      "source": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/tests/test_append_change_records.py",
      "before_snapshot": "/private/tmp/ca-p-1086.ACurlj/tool-before/test_append_change_records.py",
      "before_sha256": "2978c4c465f506723fa360aec2d926b8b25d18f9840471884425ab4ac255ad0c",
      "after_sha256": "fa5d1637ab252ba6f5772690b32c38dc5e68ae0596dc490552652051c50fb4ea",
      "insertions": 269,
      "deletions": 0
    }
  ],
  "accepted_payload": {
    "fields": [
      "predecessor_atom_id",
      "successor_atom_ids"
    ],
    "pair": "Both absent, or both present and valid; null is never a present valid value.",
    "event_boundary": "Exact integer schema_version 3, completed governed_project_change, file subject, MOVE action, present result under an exact archive path segment.",
    "id_format_guard": "[A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)*-[CAPRMEDIO]-[0-9]+",
    "ids": "Canonical numbered project-owned IDs; successors are a nonempty array of distinct IDs excluding predecessor. Input order is preserved.",
    "binding": "result.path basename equals result.filename; filename binds the literal predecessor at the canonical leading identity boundary, optionally after a numeric sequence prefix, and ends with exactly one @<result.version>.md suffix.",
    "compatibility": "Existing ordinary schema-v2 and schema-v3 file/recovered/folder/removed event behavior is unchanged; fields are not inserted when absent.",
    "digest": "Existing canonical event digest includes both optional fields without exclusions."
  },
  "checks": [
    {
      "name": "pre-edit APPEND_CHANGE_RECORDS suite",
      "command": "UV_PROJECT_ENVIRONMENT=/private/tmp/ca-p-1086.ACurlj/tool-check-venv PYTHONDONTWRITEBYTECODE=1 uv run --locked --python 3.14 python -B -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/tests -v",
      "exit_code": 1,
      "tests_run": 8,
      "errors": 8,
      "scope": "Original test class before any edits.",
      "outcome": "Environment-blocked: all eight test errors arise during existing tearDown cleanup, where sandbox denies rmdir of temporary .git/refs/tags. This is not a passing suite result."
    },
    {
      "name": "first direct replacement class",
      "command": "TMPDIR=/private/tmp UV_PROJECT_ENVIRONMENT=/private/tmp/ca-p-1086.ACurlj/tool-check-venv PYTHONDONTWRITEBYTECODE=1 uv run --locked --python 3.14 python -B 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/tests/test_append_change_records.py ReplacementPayloadTest -v",
      "exit_code": 1,
      "tests_run": 15,
      "errors": 1,
      "outcome": "At that source frontier fourteen pure tests passed; idempotence assertions completed but TemporaryDirectory cleanup was denied at /private/tmp/tmpa3pyqzhv/.caprmedio_caprmedio/work_journal. The standard cleanup fixture was left unchanged. Additional cases were added afterward."
    },
    {
      "name": "final pure tests and retained scratch append",
      "command": "TMPDIR=/private/tmp UV_PROJECT_ENVIRONMENT=/private/tmp/ca-p-1086.ACurlj/tool-check-venv PYTHONDONTWRITEBYTECODE=1 uv run --locked --python 3.14 python -B /private/tmp/ca-p-1086.ACurlj/verify_replacement_validator.py",
      "exit_code": 0,
      "tests_run": 15,
      "errors": 0,
      "failures": 0,
      "excluded_standard_test": "test_repeated_replacement_append_is_idempotent",
      "outcome": "PASS: all 15 pure validator tests plus retained-scratch append idempotence, receipt equality, exact single-line persisted bytes, and changed-payload identity-collision rejection.",
      "prefix_regressions": [
        "MY-PROJECT and PROJ_2 accepted",
        "CA--M-224, CA---M-224, CA_-M-224, C--A-M-224 rejected as predecessors",
        "Equivalent malformed successor IDs rejected"
      ]
    },
    {
      "name": "syntax",
      "command": "TMPDIR=/private/tmp UV_PROJECT_ENVIRONMENT=/private/tmp/ca-p-1086.ACurlj/tool-check-venv PYTHONDONTWRITEBYTECODE=1 uv run --locked --python 3.14 python -B -c 'import ast, pathlib, sys; paths = [pathlib.Path(p) for p in sys.argv[1:]]; trees = [ast.parse(p.read_bytes(), filename=str(p)) for p in paths]; print(\"Syntax accepted for\", len(trees), \"files\"); print(sys.version)' 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/tests/test_append_change_records.py",
      "exit_code": 0,
      "outcome": "Syntax accepted for both changed files under CPython 3.14.7."
    },
    {
      "name": "diff whitespace",
      "command": "git diff --check -- 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/tests/test_append_change_records.py",
      "exit_code": 0,
      "outcome": "PASS"
    },
    {
      "name": "Ruff and Mypy",
      "outcome": "Not claimed: canonical profiles, target set, and pinned tool dependencies are absent. No configuration or dependency changes were made."
    }
  ],
  "retained_scratch_append": {
    "root": "/private/tmp/ca-p-1086.ACurlj/retained-replacement-append",
    "carrier": "/private/tmp/ca-p-1086.ACurlj/retained-replacement-append/.caprmedio_caprmedio/work_journal/test-user-2026-09-14-part-1.ndjson",
    "lines": 1,
    "event_digest": "69408017cb18bb84de754b4afd203546d3f8ac710fcc8d80eedf8d94b2225238",
    "carrier_sha256": "fb1e714ca041bbe438bc365a347726aa2cf2d5a52e579e750a13b3adf079cd49",
    "cleanup": "Retained intentionally for inspectable evidence; no denied cleanup operation repeated."
  },
  "limitations": [
    "Format support does not establish registered Project prefix admission, live Atom existence, successor ACTIVE authority, predecessor content preservation, or commit-before-archive ordering. Caller must verify exact successor and predecessor source states immediately before archival and append.",
    "Opaque legacy and external identities in replacement fields require separate admission. Historical ordinary events without replacement fields retain compatibility.",
    "No COMMIT_CONTEXT producer migration or installed Tool release update was performed. This implements only the source Journal library's optional envelope extension and tests.",
    "No real Project Journal append, Git mutation, source Atom creation, settings change, generated projection change, or installed-copy change was performed by this worker. Test Git operations were confined to the existing disposable fixture repositories.",
    "Whole-file size and preexisting validate_sealed_event complexity already exceed current source guidance; only the bounded payload helper functions and two validation call-site additions are added. No full Programmatic profile conformance is claimed.",
    "Standard integration test cleanup remains environment-blocked; retained-scratch operational evidence does not turn the original full suite into a pass."
  ]
}
```

The state preflight separately verifies the eight exact successor files before M224 is archived; payload syntax alone does not establish Active authority. The archive event must retain the explicit predecessor and successor IDs and the exact archived digest. Tests use temporary repositories; no real Source Reconciliation workflow, conflict correction, or compiler build is executed. Existing Tool consumers naming M224 remain deferred to their owning migration work. COMMIT_CONTEXT, installed Tools, settings, generated Applicable Methodology, Drafts and unrelated Tasks are not migrated. Git remains untouched under the scoped deferral.

Independent root verification passed all 15 pure validator tests and compared old/new validation of all 7,990 existing schema-2/3 Journal events: no pre-existing invalid records, no behavior changes, no Journal mutations. Separate read-only reviews found no source-content blocker; a permissive prefix-scanner edge case was hardened and covered by expected-failure tests without introducing a new global prefix policy. The final scanner still does not prove prefix registration or live source admission.
