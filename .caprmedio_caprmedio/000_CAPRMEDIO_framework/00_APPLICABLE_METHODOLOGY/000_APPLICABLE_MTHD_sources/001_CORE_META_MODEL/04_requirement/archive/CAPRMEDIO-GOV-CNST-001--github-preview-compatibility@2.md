---
subject_scopes:
  - external-boundary
version: 2
updated_at: 2026-08-18 07:41:22
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-GOV-REQU-306--job-based-carrier-policy
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Preserve GitHub preview compatibility

Every CAPRMEDIO-owned Markdown, TOML, or YAML artifact must remain legible and navigable in GitHub's repository file preview.

Markdown artifacts must:

- use valid YAML frontmatter and GitHub Flavored Markdown;
- use repository-relative Markdown links and image paths;
- use only GitHub-supported alerts: `NOTE`, `TIP`, `IMPORTANT`, `WARNING`, and
  `CAUTION`;
- use `<details><summary>` for collapsible sections;
- use fenced `mermaid` blocks for diagrams; and
- avoid Obsidian wiki links, embeds, and Obsidian-only callout syntax.

TOML artifacts must:

- remain valid UTF-8 TOML;
- be understandable in GitHub's source view without a generated renderer;
- use descriptive keys, comments, and section ordering when they materially
  improve readability; and
- avoid encoding required meaning only through editor-specific behavior.

YAML artifacts must:

- remain valid UTF-8 YAML;
- expose branching structure through descriptive keys and consistent indentation;
- remain understandable without a generated renderer; and
- avoid encoding required meaning only through anchors, tags, or editor-specific behavior.

GitHub-preview compatibility does not require GitHub Pages publication or
prevent other consumers from rendering the same portable files.

## Historical frontmatter metadata

```yaml
source_refs:
  - "https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax"
  - "https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams"
  - "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes"
  - "https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files"
  - "https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter"
```
