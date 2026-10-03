---
atom_id: CA-D-398
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Revision/Frontmatter"
  depends_on:
    - "Atom/Claim"
    - "Project Structure"
    - "Project Settings"
    - "Framework Instance Settings"
version: 4
updated_at: "2026-09-15 00:19:55 +0000"
relations:
  child_of:
    - "CA-D-311"
    - "CAPRMEDIO-META-REQU-675"
---
# Encode configuration surfaces in owning Atoms

an owning Atom **may** carry an optional machine-readable representation of its own Claim **only** **if** it faithfully preserves that Claim **and** is **not** an independent source. legacy `project_scope_unit_graph` **or** `project_graph_state` YAML maps **may** be read as migration evidence; they **must not** own current Scope Unit declarations, paths, Name/order values, Project identity, Atom prefix, **or** selected Authority Modes. Project initialization inputs belong **to** Project Settings; instance defaults belong **to** Framework Instance Settings; unit declarations **and** explicit unit overrides belong **to** Project Structure. this format does **not** require creation **or** consumption of a structural Projection.
