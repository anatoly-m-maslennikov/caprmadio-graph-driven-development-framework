---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Objective Atom Validation"
  depends_on:
    - "Atom/Content Role: Plan/Type: Objective"
    - "Atom/Content Role: Plan/Type: Objective/Carrier/Filename"
    - "Atom/Content Role: Plan/Type: Objective/Carrier/Placement"
    - "Atom Collection/Type: Epic/Objective"
version: 8
updated_at: "2026-09-16 14:01:24 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1365
    - CA-R-1367
    - CA-D-350
    - CA-D-351
    - CA-D-273
    - CA-D-447
---
# Validate Objective Atoms

## Claim checked

an Objective Atom states one Epic-wide outcome for **`=1`** Epic, uses the canonical Objective filename, remains outside its target Epic Directory Carrier, **and** is the **`<=1`** Objective Atom for that Epic.

## Test case

create one valid Objective Atom **in** its Atom Scope's `03_plan` folder **and** one Epic with no Objective Atom. **then** create two Objective Atoms for one Epic, omit the target Epic, target multiple Epics, use a noncanonical filename, **and** move the Objective Atom Carrier into its target Epic Directory Carrier.

## override cases

- add valid confidence **and** retry overrides **to** the existing Objective frontmatter; omit either field **and** **then** the whole optional mapping.
- try a separate Epic settings file, duplicated override sources, an override attributed **to** the Objective's containing folder instead of its target Epic, **or** an empty Objective body containing **only** settings metadata. reject these alternatives.
- retain the same canonical Objective filename, external placement, identity, **and** **=1** intended outcome. do **not** require an Objective for an Epic that inherits its settings.

## Acceptance criteria

**only** the valid Objective Atom **and** the Epic with no Objective Atom pass. optional Epic overrides are valid **only** **in** the target Objective's frontmatter under CA-D-273 **and** CA-D-447; they do **not** replace its intended outcome **or** create an additional Claim. an Epic **without** an Objective **or** explicit field inherits **without** a new settings Carrier.

## Failure disposition

record a Concern naming the invalid Objective fact.
