---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "provenance"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 17
updated_at: "2026-10-08 02:28:30 +0000"
relations:
  relates_to:
    - CA-R-1491
  delivery_for:
    - CA-R-812
    - CA-R-1124
    - CA-R-1064
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver the change-record appender script

APPEND_CHANGE_RECORDS **must** be delivered through the canonical source script `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py` **and** its content-identical Carrier **in** the selected `.caprmedio_runtime/tools` release.

- expose the common Doer CLI contract with dry-run **and** apply modes.
- use the release-local shared non-executable Journal append implementation for schema-version-3 `governed_project_change` file **or** folder events, including the recorded ordered folder entry set; retain read compatibility with accepted schema-version-2 file records.
- restrict admission checks **to** the event representation **and** storage-integrity boundary of CA-R-1491 **and** CA-D-340. the shared library **must not** apply Atom-ID grammar, filename conventions, lifecycle rules, folder-placement rules, **or** relation-validity checks as append gates.
- preserve recorded Project values **without** renaming **or** repairing them. accepted event storage does **not** certify the recorded Project state.
- keep mutable lease **and** append state under `.caprmedio_runtime`. the shared implementation remains a library, **not** an additional executable Tool.

## Carrier-only recovered baseline

schema-version-3 `recovered` `governed_project_state` file records **may** encode observed present state through `recovery_evidence` with **=1** `carrier` object:

- `path`: the recorded result path;
- `sha256`: the recorded result digest;
- `observed_at`: the record's timezone-qualified Occurred At; **and**
- `observer_run_id`: the actual observing Run identifier.

this closed Carrier-only representation establishes present state **only**. the Author **and** Occurred At identify its recorder **and** observation, **not** an unobserved historical creator **or** creation time. historical Actor, time, intent, Scope, **and** outcome remain unproven unless separately evidenced.

retain accepted schema-version-3 `git` **and** `carrier` recovery evidence **and** schema-version-2 read compatibility. Git corroboration is optional for this Carrier-only representation. a recovered record carries **none** of `action_type`, `sources`, **or** `previous_result_event`; a subsequent non-ADD change links **to** the confirmed baseline through `previous_result_event`. admission verifies this representation **and** recording integrity, **not** current Project grammar.
