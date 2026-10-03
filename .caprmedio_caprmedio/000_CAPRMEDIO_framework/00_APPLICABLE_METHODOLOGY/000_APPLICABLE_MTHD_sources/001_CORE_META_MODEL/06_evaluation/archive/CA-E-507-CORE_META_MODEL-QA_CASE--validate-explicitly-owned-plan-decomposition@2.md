---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Directory Carrier"
    - "File Carrier"
    - "Atom/Identifier"
    - "Plan Graph"
version: 2
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"evaluation_for": ["CA-R-1579", "CA-R-1534", "CA-R-1536", "CA-R-1537", "CA-R-1538", "CA-D-481", "CA-D-460", "CA-D-461"]}
---
# Summary

Validate explicitly owned Plan decomposition

## Claim

the decomposition Evaluation **must** reproduce **only** the Plan Relations declared under CA-D-481.

- declare `B IS_DECOMPOSITION_OF A` on `B` **and** `C IS_DECOMPOSITION_OF B` on `C`; derive their exact `DECOMPOSES_INTO` inverses **and** derive `A` reaching `C` **only** **in** the recursive view.
- retain the same graph with **all** three Markdown files directly **in** `03_plan`, with matching optional Hub folders, **and** across valid Status placements. the declarations, **not** adjacency, determine the graph.
- count matching same-identity file **and** folder Carriers once, **without** a self-edge.
- change **only** Labels **or** navigation numbers: retain identities **and** Relation meanings.
- reject a cycle, self-edge, non-Plan **or** unresolved endpoint, **`>1`** immediate decomposition targets, authored inverse list, duplicate declaration, transitive edge invented by closure, **or** a missing mandatory Markdown file.
- reject nesting a Plan inside another Plan's directory **when** its carried decomposition target is absent **or** different; do **not** silently derive **or** repair the edge from that nesting.
- preserve every related Atom's independent Claim, Revision, Status, **and** owning Scope Unit.

report exact expected **and** observed endpoints **without** silently changing declarations **or** placement.
