---
subjects:
  governs: "Atom/Carrier/Canonical Address"
  depends_on:
    - "Atom/Property"
    - "Atom/Summary"
    - "Atom/Identifier"
    - "Atom/Revision/Status"
    - "Markdown Atom Carrier"
version: 2
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-D-478", "CA-D-282", "CA-D-466"]}
---
# Summary

Keep Atom addresses consistent with carried Properties

## Claim

**every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.

- compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
- a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
- agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.
