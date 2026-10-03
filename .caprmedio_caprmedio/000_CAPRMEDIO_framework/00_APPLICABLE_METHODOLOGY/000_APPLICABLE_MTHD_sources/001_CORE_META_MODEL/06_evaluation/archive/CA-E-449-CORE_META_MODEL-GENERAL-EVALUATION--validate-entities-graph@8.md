---
subjects:
  governs: "Projection/Type: Entities Graph"
  depends_on:
    - "Entity"
    - "Dependent Entity"
    - "Primary Entity"
    - "Property"
    - "Term"
    - "IS_BORNE_BY"
    - "IS_ALLOWED_VALUE_OF"
    - "BEARS"
    - "Relation Kind"
    - "Subject Path"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Artifact/Revision"
    - "Projection"
    - "Action"
    - "Workflow"
    - "Scope Unit"
    - "Journal"
    - "Carrier"
    - "Atom"
version: 8
updated_at: "2026-09-22 20:07:50 +0000"
relations:
  evaluation_for:
    - CA-R-1438
    - CA-R-1456
    - CA-R-1248
    - CA-R-1406
    - CA-R-1247
    - CA-R-1201
    - CA-R-1246
    - CA-R-1260
    - CA-R-1192
    - CA-R-1351
    - CA-R-1436
    - CA-R-1346
    - CA-R-1243
---
# Validate Entities Graph

the Evaluation **must** reject an Entities Graph **if** **any** of:

- a node is **not** an Entity under its governing authority, **or** a separate Entity identity is invented for an existing Action **or** Workflow Atom.
- a selected view includes a node **or** source Relation that fails its declared source selection **or** fails its declared display selection, omits an eligible node **or** source Relation under CA-R-1456, **or** silently imports outside authority **to** complete the view.
- a displayed node **or** edge lacks its exact governing source Claim **or** Artifact Revision for Entity **or** Relation admission, **or** a represented observed structural **or** recorded historical fact lacks its appropriate Scope Unit **or** Journal source under CAPRMEDIO-META-REQU-657; derived inverse navigation lacks traceability **to** the original source Relation.
- display membership, repeated appearance, a reusable Term, **or** a shortened path substitutes for the existing canonical Entity identity **or** complete bearer-qualified Subject Path.
- multiple governing Atoms are treated as multiple identities for one Entity, **or** the **`=1`** GOVERNS target per Atom is treated as permitting **only** **`=1`** governing Atom per Entity.
- a tree display is treated as the full combined graph **without** satisfying its declared selection, **or** legitimate sharing is rejected, duplicated, **or** discarded **to** force a tree.
- a Relation Kind is unregistered **or** belongs **to** another graph kind under CA-R-1246.
- an IS_BORNE_BY Relation has an invalid endpoint **or** direction under CA-R-1260, **or** violates the applicable immediate-bearer cardinality under CA-R-1192 **or** CA-R-1351.
- an IS_ALLOWED_VALUE_OF Relation admits a value **without** governing authority for its qualified Property context under CA-R-1436.
- admission **in** one Property context is used **to** justify admission **in** another context **without** its applicable authority.
- allowed-value admission is treated as assigning a value **to** a particular Property occurrence **or** determining that Property's cardinality.
- BEARS is independently authored as another primitive Relation Kind instead of being derived from IS_BORNE_BY under CA-R-1243.

the Evaluation **must not** reject the reuse of one Term as an allowed-value name **in** multiple qualified Property contexts **when** the value is separately admitted **in** **every** such context. the checks **must** cover valid **and** invalid bearer endpoints, applicable bearer cardinalities, independent value admission across Property contexts, derived inverse navigation, **and** a Relation Kind imported from another graph kind.

native endpoint **and** cardinality checks use the cited governing source facts; a filtered view does **not** establish absence of a bearer, change a qualified identity, **or** alter allowed-value admission. **if** selected evidence cannot establish an applicable source constraint, the Evaluation **must** retain the source-backed limitation as unresolved **without** inventing an edge **or** silently enlarging selection. a truthful limited view does **not** prove that the unexamined source model passes its checks.

the checks **must** also cover exact selected-source node **and** edge provenance, eligible omissions **and** outside-selection additions, repeated appearances of one identity, distinct qualified occurrences sharing a reusable Term, multiple governing Atoms for one Entity, Action **and** Workflow Atoms admitted under their existing Atom identities **when** selected, rejection of duplicate identities **and** type-only exclusion, a legitimate shared value admitted independently **in** two Property contexts, **and** explicit hierarchy filtering **without** a universal-tree assumption.

the Evaluation **must** reject a graph **or** filtered view **if**

- its rendered content is treated as independent model authority,
- a graph specification is used **to** grant source authority **to** its derived contents,
- an upstream Projection substitutes for the appropriate source facts,
- an observed Carrier **or** Journal occurrence is used **to** admit an Entity identity, define a Term, **or** admit a Relation Kind **without** the required governing source Claims,
- a Projection chain loses upstream identity **or** ultimate source traceability,
- **or** an arbitrary display filter is treated as another admitted Projection Type.

a source-faithful view derived through an upstream Entities Graph Projection **must** pass these Projection-specific checks **when** the remaining applicable source, display-selection **and** graph constraints pass.
