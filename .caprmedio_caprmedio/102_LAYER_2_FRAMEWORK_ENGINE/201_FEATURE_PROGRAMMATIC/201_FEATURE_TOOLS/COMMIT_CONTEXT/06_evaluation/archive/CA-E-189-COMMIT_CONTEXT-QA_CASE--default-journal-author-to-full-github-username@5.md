---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-804
---
# Default the Journal author to the full GitHub username

## Claim checked

Context gathering uses the current operator's full GitHub username when no author is supplied.

## Test case

Configure Git display name `Anatoly Maslennikov` and GitHub username `anatoly-m-maslennikov`, omit the author input, and gather one valid file-change context.

## Acceptance criteria

The sealed context author is exactly `anatoly-m-maslennikov`, and the predicted Journal filename begins `anatoly-m-maslennikov-` rather than using the display name, email, abbreviation, or repository owner inferred ambiguously.

## Failure disposition

Reject the Finder if it emits another author value or continues when the current full GitHub username cannot be resolved unambiguously.
