---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-validation"
  depends_on:
    - "Atom/Type"
    - "Artifact/Carrier"
    - "Atom/Property"
version: 1
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-D-478", "CA-D-480", "CA-R-1136"]}
---
# Summary

Validate internally carried Atom Type

## Claim

the Carrier validation Tool **must** accept a valid Atom Type carried inside its Markdown file under the applicable Delivery schema **and** reject missing required **or** contradictory representations.

- parse the carried Type without using a filename Type token as its source; a matching token is a valid representation, **not** prohibited duplication.
- remove the required internal value while leaving a valid filename token: reject the Atom.
- alter the token so that it disagrees with the carried Type: reject the mismatch **without** silently selecting the address value.
- a CLI failure reports the affected Property **and** Carrier with a non-zero exit; the Tool **must not** repair the source as part of validation.
