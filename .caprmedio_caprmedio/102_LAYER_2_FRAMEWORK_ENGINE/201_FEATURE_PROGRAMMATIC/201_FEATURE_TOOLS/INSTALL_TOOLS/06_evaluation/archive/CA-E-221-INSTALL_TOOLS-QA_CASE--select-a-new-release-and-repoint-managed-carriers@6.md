---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103

---
# Select a new release behind stable managed carriers

## Claim checked

Changing one canonical installation input creates a new release identity and repoints every release-resolving managed carrier without changing the stable Codex Hook identity.

## Test case

Install one canonical Tool frontier, change one machine-readable registry byte in the canonical source, and apply installation again.

## Acceptance criteria

The second release digest differs, current status verifies the second release, every stable launcher resolves only the second release, and release-specific Git Hook carriers name only the second release. The canonical and merged user-level Codex Hook groups remain byte-for-byte unchanged, resolve the current repository at invocation time, and address its stable `commit-trigger` launcher rather than either release path. The first immutable release may remain as reconstructible installation history.

## Failure disposition

Reject delivery if source change does not change release identity, current selection is ambiguous, managed carriers mix releases, the Codex Hook identity changes only because the selected release changed, or reinstallation edits an earlier release.
