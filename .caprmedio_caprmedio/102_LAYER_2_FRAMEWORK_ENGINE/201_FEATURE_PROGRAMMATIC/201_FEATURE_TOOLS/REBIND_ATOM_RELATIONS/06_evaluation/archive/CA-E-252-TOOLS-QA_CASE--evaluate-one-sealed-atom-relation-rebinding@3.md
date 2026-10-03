---
subjects:
  declared:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-1049
    - CA-R-1093
---
# Evaluate one sealed Atom relation rebinding

Given temporary active Markdown Atom carriers, perform dry runs of sealed requests that rewrite one exact relation target to a verified canonical active ID or remove one exact target. Repeated requests must return byte-identical receipts, preserve filename, body, and undeclared frontmatter, advance version once only in the planned result, and report no Journal or Git effect.

Verify direct `--apply` is rejected without authorized project-local MCP delegation. Verify an authorized MCP delegation replaces only the sealed source carrier, returns the deterministic receipt, and receives durable `COMMIT_TRIGGER` intake acknowledgement without a Journal append, staged file, or Git commit. Rejections for inactive source, changed digest, wrong version, unavailable relation, missing old target, repeated old target, and invalid new target leave source bytes unchanged.
