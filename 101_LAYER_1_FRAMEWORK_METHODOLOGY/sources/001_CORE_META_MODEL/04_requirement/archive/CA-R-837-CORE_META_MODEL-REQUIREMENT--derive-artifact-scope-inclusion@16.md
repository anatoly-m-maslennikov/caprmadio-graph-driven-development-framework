---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 16
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
---
# Summary

Derive Artifact scope inclusion

## Claim

for **every** Artifact contained **in** a Scope Unit, the resolver **must** resolve its one direct Scope Unit from the Atom's internally carried ownership, checked against its canonical Carrier address, **or** from the registered canonical Carrier authority for a non-Atom Artifact **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.

an Atom with no containing Scope Unit uses the separately governed Scope rule under CA-R-930; a failed Scope Unit resolution does **not** establish that no containing Scope Unit exists.
