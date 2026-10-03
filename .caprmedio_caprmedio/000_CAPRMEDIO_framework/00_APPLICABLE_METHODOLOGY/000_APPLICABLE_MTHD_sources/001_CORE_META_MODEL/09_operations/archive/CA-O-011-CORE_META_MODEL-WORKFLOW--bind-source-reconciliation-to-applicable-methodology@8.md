---
subjects:
  governs: "Applicable Methodology Compilation"
  depends_on:
    - "Workflow/Relation Kind: On Result"
    - "Step Run"
    - "Workflow Run"
    - "Action"
    - "Step"
    - "Workflow"
    - "Source Reconciliation"
    - "Applicable Methodology"
    - "Methodology Source"
    - "Scope Unit"
    - "Framework Instance Settings"
    - "Extension"
    - "Project Configuration"
    - "Methodology Source/Expansion Boundary"
    - "Atom/Revision"
    - "Atom/Claim"
    - "Operator"
    - "Applicable Methodology/Source Frontier Digest"
    - "Journal/Record"
version: 8
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
---
# Bind source reconciliation to Applicable Methodology

Applicable Methodology Compilation **must** bind Source Reconciliation **to** producing Applicable Methodology by reusing CA-O-010's Steps **and** typed control-flow Relations with the following bindings. this preserves the named methodology-specific Workflow target; it does **not** introduce a Step that invokes another Workflow **or** duplicate an Action definition.

| Reused Step | Action reference | Parameters **and** inputs for Applicable Methodology |
|---|---|---|
| select | CA-O-004, Select Reconciliation Sources | resolve the complete current source set under CA-R-1228 from registered Methodology Source Scope Units, using Framework Instance Settings for current Extension activation **and** selected Extension Revisions. include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** applicable installed Extension Revision. discover registered source Carriers **without** requiring particular Extension names **or** Project-specific Project Configuration Claims; an empty Extension contribution requires no empty collection Carrier. collect **`=1`** current active Revision of **every** eligible source Atom under CA-R-1315 **without** omitting previously unknown conforming contents. |
| assess | CA-O-005, Assess Source Conflicts | check Core expansion-boundary conformance under CA-R-1375 **and** the applicable conflict authority, including CA-R-1373; detect **every** boundary violation, duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, **and** unresolved priority. retain conflicting source Atoms rather than silently discarding them. calculate one deterministic digest of the exact selected frontier **and** report the complete deterministic conflict set **before** changing Applicable Methodology membership. |
| propose | CA-O-006, Propose Source Corrections | propose needed changes **only** through the separately authorized workflow of the owning source authority. source order, Claim synthesis, Claim merge, **and** LLM inference **must not** resolve a conflict. a prohibited Extension **or** Project Configuration override **must not** become conforming **without** an authorized change **to** its governing Core authority. |
| decide | CA-O-007, Obtain Source Correction Decision | enforce CA-R-1317 through CA-O-007: obtain **`=1`** unambiguous actual Operator approval **and** record it **in** the Journal, bound **to** the exact proposal, conflict, **and** source-frontier digest. stale, partial, missing, ambiguous, **or** mismatched approval does **not** qualify. do **not** create an approval Atom **in** Project Configuration; approval **must not** itself bypass Core expansion boundaries. |
| correct | CA-O-008, Apply Approved Source Corrections | require the separately authorized source change workflow; corrections are **not** compiler side effects **or** edits **to** projected Claims. **if** **any** source changes, the Workflow Run returns **to** select **and** repeats assessment against the new frontier. failure **or** partial effects never justify publishing from the earlier assessment. |
| publish | CA-O-009, Publish Reconciled Projection | preserve **every** selected Atom ID, exact source Revision, authority owner, **and** Claim under CA-R-1314 **and** CA-R-1316; enforce CA-R-1461 **and** CA-D-305 **and** CA-D-306 source identity, exact source Carrier bytes **and** Carrier form. fail **without** changing Applicable Methodology membership **if** **any** conflict remains unresolved **or** **any** required approval is invalid. produce the same ordered Applicable Methodology membership from the same resolved source frontier. |

these bindings preserve CA-O-010's entry Step, Step-to-Action references, ON_RESULT transitions, **and** run boundaries under CA-R-1509, CA-R-1510, **and** CA-R-1511.
