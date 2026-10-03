---
atom_id: CA-M-224
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    continuant:
      - Applicable Methodology/Sources
      - Applicable Methodology
      - Local Configuration
      - Methodology Source
      - Scope Unit
      - Framework Instance Settings
      - Extension
      - Artifact/Revision
      - Methodology Source/Expansion Boundary
      - Atom/Claim
      - Operator
version: 11
updated_at: "2026-09-11 02:49:55 +0400"
relations:
  method_for:
    - CA-R-1228
    - CA-R-1434
---
# Compile Applicable Methodology Deterministically

**to** compile Applicable Methodology, the Compiler **must** perform **all** of:

1. resolve the complete current source set under CA-R-1228 from the registered Methodology Source Scope Units, using Framework Instance Settings for current Extension activation **and** selected Extension revisions.
2. include CORE_META_MODEL, LOCAL_CONFIGURATION, **and** **every** applicable installed Extension revision. discover source contents from their registered Carriers **without** requiring particular Extension names **or** Project-specific Local Configuration Claims. an empty Extension contribution **must not** require an empty collection Carrier.
3. collect **`=1`** current active Revision of **every** source Atom eligible under CA-R-1315 from **all** those sources; do **not** omit eligible Atoms merely because their Extension **or** Local Configuration content was previously unknown.
4. preserve **every** selected Atom ID, exact source revision, authority owner, **and** Claim **without** synthesis **or** merge.
5. check source conformance to Core expansion boundaries under CA-R-1375 **and** detect **every** boundary violation, duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, **and** unresolved priority. do **not** silently discard conflicting source Atoms.
6. calculate one deterministic digest of the exact selected source frontier.
7. report the complete deterministic conflict set **before** changing Applicable Methodology membership.
8. accept a conflict resolution **only** **if** source authority records one unambiguous Operator approval bound to that exact conflict **and** source-frontier digest. require needed source corrections through their separately authorized governed change workflow, **not** as a compilation side effect **or** an edit to projected Claims. **if** a source changes, restart source selection **and** conflict checks against the new source frontier; approval **must not** make a prohibited Extension **or** Local Configuration override conform **without** an authorized change to the governing Core authority.
9. fail **without** changing Applicable Methodology membership **if** **any** conflict remains unresolved **or** **any** approval is stale, partial, missing, ambiguous, **or** mismatched.
10. do **not** use source order, Claim synthesis, Claim merge, **or** LLM inference to resolve a conflict.
11. produce the same ordered Applicable Methodology membership from the same resolved source frontier.
