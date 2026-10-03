---
atom_id: CA-R-1385
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - provenance
version: 1
updated_at: 2026-09-04 03:10:59 +0400
relations: {}
---
# Bound commit automation with an explicit autonomy envelope

Every autonomous `COMMIT_AUTOMATION` run MUST be admitted by one current, durable autonomy envelope. The envelope identifies its authorizing Work, repository, permitted subject scope, start and expiry or bounded execution window, permitted action kinds, queue and concurrency caps, resource and retry budgets, hard admission guards, circuit state, and the independent authority that may pause, resume, narrow, replace, or escalate it.

For the current CAPRMEDIO Tool surface, the only permitted Git action kinds are a local real-change commit and a local Journal-only commit. The envelope cannot admit branch, upstream, remote, synchronization, push, tag, release, or other Git effects. A broader request MUST stop for explicit Operator or external handling rather than widening the envelope.

The service MUST revalidate the envelope before admitting an action, before dispatching each effectful step, and immediately before commit creation. Missing Work linkage, ambiguity, expiry, exhausted caps, failed guards, stale authority, circuit opening, or scope escape pauses the affected work before the effect and preserves it for inspection or independently authorized recovery. The actor that authorizes or overrides an envelope MUST be distinct from the worker that executes its commit effect.

An envelope replacement may preserve or narrow already admitted work only when stable action identities and the still-valid original boundaries remain provable. Expansion, escalation, or resumption after an integrity failure requires an independently authorized new envelope.
