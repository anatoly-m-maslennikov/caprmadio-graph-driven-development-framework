---
cce_version: cce_1
cce_form: definition
subjects:
  declared:
    occurrent:
      - runtime
version: 9
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
    - CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions
---
# Register Work Journal events

GOVERNANCE MUST register `started`, `progressed`, `completed`, `failed`, `interrupted`, `abandoned`, and `recovered` Work Journal events. Every newly accepted schema-version `2` event identifies its `event_id`, `action_id`, lifecycle `event`, `kind`, full GitHub `author`, timezone-qualified `occurred_at`, session provenance, and structural scope. LLM session provenance is stored only in the Journal as a structured `llm_session` object containing canonical `app` and host `uuid` values; together with the event's one `occurred_at`, it can project `<app>:<uuid>:<occurred_at>` without storing that concatenated value. `preceding_event`, when present, links lifecycle events inside one action and MUST NOT be used as an Artifact-state predecessor. Commit and pull-request provenance remain optional bindings.

A `governed_file_change` event is one `completed` event with:

- the `llm_session` resolved for the triggering LLM application and sealed with `occurred_at` before the event digest is computed;
- `action_type` equal to `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`;
- `sources`, a deterministically ordered array containing every direct typed relation reference exactly once as `relation_type`, source `filename`, and source `version`, or an empty array when none exists; when a registry row names `work_journal_event` as its `declaration_carrier`, this array is the sole persisted declaration of that direct relation;
- singular `result`, identifying the one governed subject outcome by `state`, `filename`, and `version`; a `present` result also requires its resulting repository-relative `path` and `sha256`, while a `removed` result omits them; and
- `previous_result_event`, omitted for an `ADD` or first known state and otherwise identifying the latest accepted event whose `result` is the state immediately before this result.

When an existing governed subject has no prior accepted result event, a separate `recovered` `governed_file_state` event MAY establish the evidenced prior `result` under the Work Journal recovery rule; the change event then names that event as `previous_result_event`. The same sealed `llm_session` and `occurred_at` values MUST survive every retry of one event identity. A file-change or file-state event MUST NOT store `action_message`, a pre-rendered LLM-session string, `before_path`, `before_sha256`, or another copy of prior result state, and the auto-commit flow MUST NOT copy event session provenance into Atom or Projection carriers. The canonical Git message is a deterministic Projection of the structured change event and its referenced previous result when the change syntax requires the prior carrier address. Previously accepted events remain valid under their declared schema version.
