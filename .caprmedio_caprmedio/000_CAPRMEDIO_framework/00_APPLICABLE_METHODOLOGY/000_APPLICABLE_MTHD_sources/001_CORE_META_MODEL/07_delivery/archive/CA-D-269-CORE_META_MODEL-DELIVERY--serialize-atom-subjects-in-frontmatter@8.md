---
atom_id: CA-D-269
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Subjects/Frontmatter"
  depends_on:
    - "Atom/Subjects"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Path"
    - "Subject"
    - "Relation Kind"
version: 8
updated_at: "2026-09-14 04:00:22 +0400"
relations: {}
---
# Serialize Atom Subjects in Frontmatter

**every** new **or** migrated Markdown Atom Carrier **must** serialize its Subjects directly as **`=1`** scalar Subject Path at `subjects.governs` **and** an unordered collection of **`>=0`** unique scalar Subject Paths at `subjects.depends_on`; an absent dependency collection **means** zero dependencies. the `governs` **or** `depends_on` key encodes the Subject Relation Kind; the source Atom is implicit **and** the scalar value encodes its target's Subject Path, **not** the Subject Relation itself. these values resolve their canonical targets under CA-R-1202 **without** an intermediate Subject/Entity **or** Subject/Reference field **or** a repeated target-kind field.

an existing unmigrated Carrier **may** temporarily retain `subjects.<governs|depends_on>.<continuant|occurrent>` **only** **until** its explicitly assigned carrier-migration Task is executed. this compatibility is migration-limited, preserves the same direct relation facts **and** target identities, **and** does **not** establish a second canonical representation. legacy temporal-classification authority **and** bulk Carrier conversion require their separately assigned migration Tasks.
