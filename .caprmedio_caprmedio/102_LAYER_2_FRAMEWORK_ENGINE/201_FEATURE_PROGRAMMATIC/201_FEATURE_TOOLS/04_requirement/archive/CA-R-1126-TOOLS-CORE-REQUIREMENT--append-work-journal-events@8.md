---
subjects:
  declared:
    continuant:
      - work-journal
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 8
updated_at: 2026-08-23 16:16:20 +0400
---
# Append Work Journal events

Every Journal-appending Doer must use shared deterministic non-executable logic that validates and atomically appends one sealed Work Journal event without rewriting or rereading the complete logical Journal. The logic must validate and use the event's already sealed full GitHub username, configured Artifact timestamp timezone, and local calendar date without resolving or recomputing them; serialize competing appends to the affected author-date partition; verify the current carrier digest inside that serialization boundary; continue the current `<author>-<YYYY-MM-DD>-part-<N>.ndjson` segment while it contains fewer than 100 accepted events; and open the next numbered segment otherwise. Its receipt binds the event identity, canonical event digest, carrier, line position, `previous_carrier_digest`, and `appended_carrier_digest`; the carrier digests describe the Journal append and never duplicate a governed subject's previous and resulting states. Reapplying the same sealed event identity with the same canonical event digest must return its existing receipt without appending a duplicate. Reusing an accepted event identity with different canonical event bytes must fail before mutation with a stable identity-collision diagnostic. The shared logic is not an independently executable Tool.
