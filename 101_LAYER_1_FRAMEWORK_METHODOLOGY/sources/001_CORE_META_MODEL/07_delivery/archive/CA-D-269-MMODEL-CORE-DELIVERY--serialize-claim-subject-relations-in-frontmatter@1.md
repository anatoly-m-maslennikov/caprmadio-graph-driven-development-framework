---
atom_id: CA-D-269
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Claim-Subject Relation/Frontmatter
  depends_on:
    continuant:
      - Claim-Subject Relation/Kind
      - Claim-Subject Relation/Temporal Form
      - Subject
version: 1
updated_at: 2026-08-28 23:15:00 +0400
relations: {}
---
# Serialize Claim-Subject Relations in Frontmatter

every Markdown Atom Carrier **must** serialize each Claim-Subject relation as one Subject Path in `subjects.<governs|depends_on>.<continuant|occurrent>` so the path encodes exactly one relation Kind and one Temporal Form without owning the referenced Subject.
