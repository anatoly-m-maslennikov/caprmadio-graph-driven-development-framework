---
subjects:
  governs: "Projection/Type: Entities Graph"
  depends_on:
    - "Entity"
    - "Subject Path"
    - "Atom/Claim"
    - "Atom/Subjects"
    - "Artifact/Revision"
    - "Relation"
    - "Relation Kind"
    - "IS_BORNE_BY"
    - "IS_ALLOWED_VALUE_OF"
    - "BEARS"
    - "Projection"
    - "Term"
    - "Scope Unit"
    - "Journal"
    - "Carrier"
version: 5
updated_at: "2026-09-15 01:47:49 +0400"
relations:
  child_of:
    - CA-R-1438
    - CA-R-1248
    - CA-R-1406
    - CA-R-1437
---
# Derive Entities views from selected authority

a derived Entities Graph view **must** declare its requested source selection **and** **any** narrower display selection, including a hierarchy view. it **must** include **all** **and** **only** Entity identities admitted under CA-R-1248 by the selected source Claims that satisfy the declared display selection, **and** Relations explicitly declared by selected source Atoms whose endpoints are included, whose Relation Kind is admitted for the Entities Graph, **and** that satisfy the declared display selection. a narrower view **must not** silently enlarge the source selection **or** be represented as the full combined graph.

**every** displayed node **and** edge **must** retain its existing canonical identity **and** traceability **to** its exact governing source Claim **and** Artifact Revision for Entity **or** Relation admission; **any** represented observed structural **or** recorded historical facts additionally retain their appropriate Scope Unit **or** Journal sources under CAPRMEDIO-META-REQU-657. dependent occurrences retain their complete bearer-qualified Subject Paths under CA-R-1247; reuse of a Term, appearance **in** multiple views, **or** multiple governing Atoms for one Entity **must not** duplicate **or** merge source identities. source Relation facts retain their graph ownership, direction, qualified endpoints, **and** source declaration; derived BEARS navigation retains traceability **to** its original IS_BORNE_BY fact under CA-R-1243 **without** becoming another primitive Relation fact.

this selection reuses the Entities Graph under CA-R-1438 **without** another graph kind **or** independent model authority. a hierarchy display **must not** impose a tree constraint on the full graph, discard legitimate sharing, **or** introduce a global ordinal-position rule. display filtering **must not** change source bearer cardinalities, qualified identities, **or** allowed-value admission; IS_BORNE_BY **and** IS_ALLOWED_VALUE_OF retain their distinct governing authority.

the view **may** be derived from an upstream Entities Graph Projection **when** the upstream selection **and** source evidence support the requested view. the view **must** retain the upstream Projection identity **and** Revision together with traceability **to** the ultimate authoritative sources; the upstream Projection **must not** replace source authority **or** establish source completeness beyond its evidenced coverage. an observed Carrier **or** Journal occurrence alone **must not** admit an Entity identity, define a Term, **or** admit a Relation Kind **without** the required governing source Claims. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Entities Graph Type **and** its Relation Kind authority; a display filter alone does **not** admit another Type.

these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their admitted endpoint classes, graph-qualified Relation authority, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.
