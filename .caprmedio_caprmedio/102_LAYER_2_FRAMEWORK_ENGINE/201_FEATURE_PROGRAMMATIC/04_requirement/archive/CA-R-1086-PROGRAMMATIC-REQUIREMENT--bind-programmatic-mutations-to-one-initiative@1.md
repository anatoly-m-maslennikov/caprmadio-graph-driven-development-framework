---
subjects:
  - programmatic-mutation
cce_version: cce_1
cce_form: obligation
version: 1
updated_at: 2026-08-23 13:54:18
relations:
  child_of:
    - CA-R-1084
---
# Bind each programmatic mutation to one Initiative

Every accepted programmatic mutation MUST belong to exactly one sealed Initiative and one stable action identity. The Initiative MAY reference a persisted Plan or Task Atom or an ephemeral session task, and MUST retain a short summary derived from the human instruction plus sufficient structured context to identify that instruction without inventing a governed Plan Atom.

The sealed Initiative and action identity MUST survive asynchronous handoffs, retries, concurrent workers, Git commits, Journal records, and reconciliation. A worker MUST NOT replace them with a process, thread, adapter, or queue parent identity.
