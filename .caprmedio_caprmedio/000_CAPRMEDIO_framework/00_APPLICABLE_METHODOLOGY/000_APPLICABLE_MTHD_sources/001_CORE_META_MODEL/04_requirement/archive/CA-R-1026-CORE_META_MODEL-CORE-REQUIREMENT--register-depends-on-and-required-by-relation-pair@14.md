---
subjects:
  governs: "Dependency Relation Pair"
  depends_on:
    - "atom-boundary"
    - "relation-model"
    - "Artifact"
version: 14
updated_at: "2026-09-22 14:41:44 +0000"
relations: {}
---
# Register depends_on and required_by relation pair

`depends_on` **means** a direct dependency-ordering relation from a dependent Artifact **to** its prerequisite Artifact, with `required_by` as its inverse-derived view. Plan start dependencies use the Plan Graph's `BLOCKS` under CA-R-1580 instead; this Relation Kind **must not** duplicate that scheduling fact.
