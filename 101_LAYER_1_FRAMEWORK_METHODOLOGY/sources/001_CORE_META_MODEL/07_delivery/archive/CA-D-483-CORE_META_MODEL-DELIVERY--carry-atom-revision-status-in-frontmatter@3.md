---
subjects:
  governs: "Atom/Revision/Status/Carrier"
  depends_on:
    - "Atom/Revision/Status"
    - "Atom/Content Role"
    - "Atom/Type"
    - "Artifact/Carrier Placement"
version: 3
updated_at: "2026-09-24 14:16:19 +0000"
relations: {"relates_to": ["CA-D-478", "CA-D-480", "CA-D-466", "CA-D-461"]}
---
# Summary

Carry Atom Revision Status in frontmatter

## Claim

**every** Atom Revision **must** carry **`=1`** explicit `status` value **in** its own Markdown frontmatter.

- the value **must** belong **to** the applicable Content Role **and** Type Status model.
- placement **must** agree under CA-D-466 **and** its specific Delivery rules; it is **not** a second Status source.
- another Revision **or** a containing Hub **must not** override this Revision's carried Status.

- encode `status` as **=1** nonempty YAML string using the exact value admitted by the selected Status model. do **not** accept a list, null, **or** another Revision's value as this Revision's Status.
