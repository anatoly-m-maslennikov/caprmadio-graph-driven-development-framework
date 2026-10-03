---
artifact_subtype: change_plan
priority: medium
version: 2
updated_at: 2026-08-19 07:37:46
---

# Remove derivable frontmatter

1. [ ] Ditch the default priority (`medium`).
2. [x] Ditch types in frontmatter; they are already in the filename.
3. [x] Consider deleting `scope_path` from frontmatter; it can also be derived from where the file sits.
