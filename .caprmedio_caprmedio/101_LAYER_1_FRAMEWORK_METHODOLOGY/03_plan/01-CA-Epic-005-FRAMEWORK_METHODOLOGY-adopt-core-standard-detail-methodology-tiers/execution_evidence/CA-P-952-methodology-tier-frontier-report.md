# CA-P-952 — Frozen methodology tier change frontier

Non-authoritative execution evidence. This report records the observed inputs and review queue; it does not introduce authority, assign the proposed tiers, or execute later Tasks.

## Result

The narrow CA-P-952 Definition of Done passes. The inventory contains **705 exact Atom revisions**: **702 active RMED source Atoms** and **3 immediate METHODOLOGY_SOURCES Goal declarations**. Every record includes its observed identity, positive version, relative Carrier path, SHA-256 digest, current Local Tier, source owner, and bounded change disposition.

Recorded at: `2026-09-09T20:46:23.945819+00:00`.
Frontier SHA-256 (canonical JSON of the ordered records): `816aece3b235322241c4107ba83966ddebf9a3723082e4f222fd546942512bc1`.

| Source Scope Unit | R | M | E | D | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| CORE_META_MODEL | 472 | 38 | 34 | 106 | 650 |
| LOCAL_CONFIGURATION | 37 | 0 | 1 | 14 | 52 |
| METHODOLOGY_SOURCES | 3 | 0 | 0 | 0 | 3 |

Current tiers: CORE_META_MODEL has **456 Core + 194 Standard**; LOCAL_CONFIGURATION has **52 Standard**; the adjacent source Goal declarations have **3 Standard**. Source ownership and Local Tier are distinct, as required by CA-R-1234@5. There are no Principle-tier source Atoms in this frontier.

## Input boundaries and exclusions

The live canonical source folders remain under `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources`; a migrated `.caprmedio_caprmedio/000_CAPRMEDIO_framework` source tree is not present. The visibly stale Project Settings Projection was not used to select authority.

The adjacent Goal declarations are CA-R-1174@7, CA-R-1175@7, and CA-R-1176@8. Including the INSTALLED_EXTENSIONS Goal does not make the empty installed-extension source a contributor.

Excluded: **4,915** files in non-active Status/history directories; **1** non-RMED settings Carrier; **7** ignored `.DS_Store` files. Exclusion groups carry counts, example paths, and digests of their sorted path lists in the inventory. Generated Applicable Methodology files are outside the source roots and were not scanned into the frontier. Drafts, archives, history, non-Markdown files, explicit non-Active Status, projection metadata, and `@version` archive basenames are not admitted.

Legacy spelling in an active Atom identity is not evidence that its current Carrier is historical Bootstrap authority. The source Scope Unit and lifecycle placement determine inclusion.

## Identity fidelity

**26** Atoms omit an explicit `atom_id`; their existing filename identities were recorded without allocating or changing identities. All 705 have positive versions. No duplicate active identities were found.

Two explicit opaque legacy identities were preserved, with their filename-prefix difference visible:
- `CAPRMEDIO-R-791-REQUIREMENT-BSEED_METAMODEL` (filename numeric prefix: `CAPRMEDIO-R-791`).
- `CAPRMEDIO-R-793-REQUIREMENT-BSEED_GOVERNANCE` (filename numeric prefix: `CAPRMEDIO-R-793`).

The identity parser first preserves explicit `atom_id`; otherwise it extracts the existing numeric identity prefix using:

```python
r'(?:[0-9]+-)?((?:CA-[CAPRMEDIO]|CAPRMEDIO-(?:[A-Z]+-)*[A-Z]+)-[0-9]+)(?:-|\\.|@|$)'
```

For an unmatched unmigrated legacy filename, its pre-summary stem remains opaque. The inventory separately records explicit identity, filename identity, and resolution basis. No identity migration was performed.

## Review dispositions

**69** Atoms are conservatively queued for FX-04 authority review before later application; **636** are queued for FX-03 application review after the FX-04 gate. These are work dispositions, not proposed Core/Standard/Detail assignments.

Review tags may overlap: **35** tier, **16** Scope, **20** Goal placement, **9** Type admission, and **1** tier Carrier representation. The following exact deterministic predicates make the review selection reproducible; they normalize only bold/backtick markup in the body, not authority:

```python
def categories(body, governs, name, role, adjunct):
    plain = body.replace('**', '').replace('`', '')
    tags = []
    if re.search(r'\btiers?\b|highest occupied|highest local Requirement', plain, re.I):
        tags.append('tier_authority_review')
    if any(v == 'Scope' or re.search(r'/(?:Scope|Claim Scope|Current Scope)$', v) for v in governs) or re.search(r'highest (?:occupied Local Tier|local Requirement)|Scope.*derived set|derived.*Scope', plain, re.I):
        tags.append('scope_authority_review')
    if adjunct or 'GOAL_FOR' in name or (re.search(r'\bGoal\b', plain) and re.search(r'parent|child|ancestor|owner|placement|outside|Project Goal|Claim Scope', plain, re.I)):
        tags.append('goal_placement_review')
    if re.search(r'\bType\b', plain) and re.search(r'Local Tier|Global Tier|\bCore\b|\bStandard\b|\bPrinciple\b', plain):
        tags.append('type_admission_review')
    if role == 'D' and (re.search(r'Local Tier|Global Tier|\bCORE\b|\bSTANDARD\b|\bPRINCIPLE\b', plain) or any('/Local Tier' in v or '/Global Tier' in v for v in governs)):
        tags.append('carrier_tier_representation_review')
    return tags or ['application_review']
```

Any non-application tag selects `fx04_authority_review_then_fx03_application`; otherwise the disposition is `fx03_application_review_after_fx04_gate`. These conservative lexical review tags do not prove semantic applicability or replace the later per-Atom review. All active source Atoms are inventoried regardless of their tag.

Current Local Tier comes from CA-D-285@4: `CORE` → Core, `PRINCIPLE` → Principle, omitted token → Standard. An explicit frontmatter tier is checked against that result. The source-unit name `CORE_META_MODEL` is removed before inspecting tier tokens, so it cannot be mistaken for Core tier.

## Definition-of-Done checks

| Falsifying condition | Observed result |
| --- | --- |
| Missing identity, version, relative path, digest, current tier, or change disposition | None; 705 complete records |
| CORE_META_MODEL ownership confused with Core tier | No; separate fields and 194 Standard Atoms in that source |
| Generated, Draft, Archived, or historical Bootstrap material admitted as current source | None under the explicit source/lifecycle predicate |
| Changed input silently treated as the recorded revision | None; all recorded hashes and active membership rechecked after inventory |
| Duplicate active identities or parse errors | None |

The original Task Carrier bytes and their SHA-256 are embedded in the inventory. The inventory is a frozen observation, not a claim that future source bytes remain unchanged: every consuming Task must compare current bytes and membership against it, then explicitly record any authorized frontier change.

No source Atom, Task Carrier, lifecycle state, Journal, Git state, compiler, Tool, or physical folder migration was changed by this Task worker. Only the two non-authoritative evidence files were added inside this Epic. The ephemeral builder is at `/tmp/ca-p-952-frontier-m9yuRK/build_inventory.py`; its review predicates are reproduced above, so the durable evidence does not depend on that temporary file.

## Handoff

CA-P-952 can be moved to Done after parent receipt verification. CA-P-953 is next. Scope derivation policy, Global Tier mapping, the default new tier, labels, and Carrier changes are deliberately not decided here. They remain FX-04 design work under the 99% confidence threshold.
