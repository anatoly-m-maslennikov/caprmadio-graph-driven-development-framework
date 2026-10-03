---
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-837
subjects:
  governs:
    continuant:
      - scope-topology
version: 10
updated_at: "2026-09-10 07:15:17 +0400"
relations: {}
---
# Derive Artifact scope inclusion

For **every** Artifact contained **in** a Scope Unit, the resolver **must** derive its one direct Scope Unit from its canonical carrier address **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.

An Atom with no containing Scope Unit uses the separately governed Scope rule under CA-R-930; a failed Scope Unit resolution does **not** establish that no containing Scope Unit exists.
