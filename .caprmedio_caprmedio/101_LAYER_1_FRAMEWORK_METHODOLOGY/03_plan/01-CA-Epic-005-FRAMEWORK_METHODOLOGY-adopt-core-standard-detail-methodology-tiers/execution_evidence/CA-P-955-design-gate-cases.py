"""Read-only, source-bound CA-P-955 witness checks, not an NLP classifier.

The report performs semantic classification from complete live Claims. This
script independently exercises the resulting contracts and their countermodels;
it does not accept a tier label and return that label. Synthetic alternative
policies/encodings are counterfactual evidence, never admitted source changes.
Run before source application; changed source bytes deliberately invalidate it.
"""

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import re
import runpy
import tomllib


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / ".caprmedio_framework").is_dir())
INVENTORY = HERE / "CA-P-952-methodology-tier-frontier.projection.json"
EXPECTED_FRONTIER = "816aece3b235322241c4107ba83966ddebf9a3723082e4f222fd546942512bc1"
SOURCE_EXCERPTS = {
    "CA-R-1402": "authoritative Artifact containing Operator-selected behavior",
    "CA-R-1430": "using a default and optional explicit target-specific overrides",
    "CA-R-1429": "every concrete section or field specification",
    "CA-M-235": "serialize one canonical comparison CCE Operator immediately followed",
    "CA-M-265": "include it in every applicable group",
    "CA-E-428": "a Core Claim that does not apply to the full Scope",
    "CA-E-446": "create two Projects in one repository",
    "CA-D-280": "a symbolic CCE Operator must use bold inline-code rendering",
    "CA-D-368": "confidence.necessary_information_threshold_percent",
    "CA-D-374": "under authority_modes",
    "CA-D-311": "without adding, removing, duplicating, or changing authoritative content",
    "CA-D-304": "without semantic change",
    "CA-R-918": "=1 independently replaceable Claim",
    "CA-R-1052": "observed Project structure must not become a settings authority",
    "CA-R-1234": "must remain independent coordinates",
    "CA-R-1207": "only where the Core Meta-Model permits expansion",
    "CA-R-1218": "without replacing Core authority",
    "CA-R-1375": "must not redefine, replace, shadow, weaken, delete, contradict, reinterpret, or mutate",
    "CA-R-1018": "a Standard Evaluation Atom must own >=1 such target relations",
    "CA-M-264": "preserve the distinction between general Core evaluation criteria and concrete Standard cases",
    "CA-E-384": "an independently replaceable component inside one Claim",
    "CAPRMEDIO-META-REQU-675": "an Operator-selected setting must have =1 authoritative owner",
    "CA-R-658": "the Local Tier value Principle means the Project-only highest Local Tier",
    "CA-R-659": "whose Claim applies to the full Scope",
    "CA-R-660": "whose Claim applies to a proper part of the Scope",
    "CA-R-155": "=1 Local Tier in (Principle, Core, Standard)",
    "CA-R-1287": "classifies how broadly one Atom Claim applies",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_frontier():
    inventory = json.loads(INVENTORY.read_text())
    records = inventory["records"]
    digest = sha256(json.dumps(records, ensure_ascii=False, sort_keys=True,
                               separators=(",", ":")).encode()).hexdigest()
    require(digest == EXPECTED_FRONTIER, "changed frozen record set")
    by_id = {r["atom_id"]: r for r in records}
    require(len(records) == len(by_id) == 705, "missing or duplicate frontier identities")
    for record in records:
        path = ROOT / record["relative_path"]
        require(path.is_file(), f"missing source: {record['atom_id']}")
        require(sha256(path.read_bytes()).hexdigest() == record["sha256"],
                f"stale source: {record['atom_id']}")
    excluded = set(inventory["selection"]["excluded_directory_segments_casefolded"])
    candidates = set()
    for source in inventory["source_roots"]:
        for directory in inventory["selection"]["roles"]:
            for path in (ROOT / source / directory).rglob("*.md"):
                relative = path.relative_to(ROOT)
                if excluded.intersection(part.casefold() for part in relative.parts):
                    continue
                if re.search(r"@\d+\.md$", path.name):
                    continue
                # This strict superset makes a new unknown candidate fail closed.
                candidates.add(relative.as_posix())
    for path in (ROOT / inventory["adjacent_authority_root"]).glob("*.md"):
        if not re.search(r"@\d+\.md$", path.name):
            candidates.add(path.relative_to(ROOT).as_posix())
    expected = {record["relative_path"] for record in records}
    require(candidates == expected,
            f"candidate membership changed: added={sorted(candidates - expected)}, "
            f"missing={sorted(expected - candidates)}")
    source_evidence = []
    for atom_id, excerpt in SOURCE_EXCERPTS.items():
        record = by_id[atom_id]
        text = (ROOT / record["relative_path"]).read_text()
        plain = text.replace("**", "").replace("`", "")
        require(excerpt in plain, f"contract excerpt no longer matches {atom_id}")
        source_evidence.append({key: record[key] for key in
                               ("atom_id", "version", "relative_path", "sha256")})
    return inventory, by_id, source_evidence


@dataclass(frozen=True)
class Instance:
    projects: tuple = ("P",)
    authoritative_owner: str = "Framework Instance Settings"
    selected_by: str = "Operator"
    default: str = "strict"
    overrides: tuple = (("U", "casual"),)
    atom_authority: tuple = ("a@1", "b@2")


def foundation(instance):
    """Finite settings identity/authority obligation from R1402 and META675."""
    return (len(instance.projects) == 1
            and instance.authoritative_owner == "Framework Instance Settings"
            and instance.selected_by == "Operator")


def mode(instance, target):
    """R1430's semantic selection contract, with exact-target overrides."""
    require(foundation(instance), "settings authority/ownership boundary failed")
    require(instance.default in ("strict", "casual"), "missing or invalid default")
    require(len(dict(instance.overrides)) == len(instance.overrides), "duplicate target selection")
    require(all(value in ("strict", "casual") for _, value in instance.overrides),
            "invalid Authority Mode")
    return dict(instance.overrides).get(target, instance.default), instance.atom_authority


def decode_modes(text, section="authority_modes"):
    """Two hypothetical Carrier contracts can decode to the same semantics."""
    parsed = tomllib.loads(text)[section]
    return Instance(default=parsed["default"], overrides=tuple(sorted(parsed.get("overrides", {}).items())))


def groups(targets, roles):
    """M265's extensional rule. Names refer to semantic role groups."""
    labels = {"R": "Er", "M": "Em", "D": "Ed"}
    require(all(target in roles for target in targets), "unresolved evaluation target")
    require(all(roles[target] in labels for target in targets), "invalid evaluation target role")
    return frozenset(labels[roles[target]] for target in targets)


def validate_case(projects):
    """Finite E446 scenario oracle; it is not an installed integration test."""
    for project, data in projects.items():
        require(data["settings_owner"] == project, "cross-Project settings fallback")
        require(data["structure"] == ("U",), "observed unit concealed")
        require(data["active_goals"] == (), "Draft or Archived Goal promoted")
        require(not data["projection_writes_source"], "Projection edits authority")
    return True


def parse_cardinality(text):
    """Bounded M235 specimen recognizer; these three operators occur in Claim."""
    match = re.fullmatch(r"(=|>=|<=)([0-9]+) ([A-Za-z][A-Za-z ]*)", text)
    require(match is not None, "invalid cardinality prefix specimen")
    return match[1], int(match[2]), match[3]


def operator_rendering(canonical, rendered, symbolic=False):
    """D280's exact rendering contract for one known operator occurrence."""
    require(canonical == canonical.lower(), "word operator is not canonical lowercase")
    expected = f"**`{canonical}`**" if symbolic else f"**{canonical}**"
    require(rendered == expected, "incorrect operator spelling or rendering")
    return canonical


def confidence_field(text):
    data = tomllib.loads(text)
    value = data["confidence"]["necessary_information_threshold_percent"]
    require(type(value) is int, "confidence default is not an integer percentage")
    return value


def main():
    inventory, by_id, source_evidence = verify_frontier()
    passed = []

    def check(name, actual, expected):
        require(actual == expected, f"{name}: {actual!r} != {expected!r}")
        passed.append(name)

    def reject(name, action):
        try:
            action()
        except (ValueError, KeyError):
            passed.append(name)
        else:
            raise AssertionError(f"expected failure absent: {name}")

    base = Instance()
    check("R1402 one authoritative instance/Project positive", foundation(base), True)
    check("R1402 shared artifact for two Projects violates foundation",
          foundation(replace(base, projects=("P", "Q"))), False)
    check("R1402 Projection as authority violates foundation",
          foundation(replace(base, authoritative_owner="Projection")), False)
    check("R1402 missing Operator selection violates foundation",
          foundation(replace(base, selected_by="unattributed")), False)
    check("R1402 recovery restores authority owner", foundation(base), True)
    check("R1430 default semantic selection", mode(base, "P"), ("strict", base.atom_authority))
    check("R1430 exact target override", mode(base, "U"), ("casual", base.atom_authority))
    check("R1430 modes preserve active Atom authority", mode(base, "U")[1], mode(base, "P")[1])
    reject("R1430 missing default fails", lambda: mode(replace(base, default=None), "P"))
    reject("R1430 invalid mode fails", lambda: mode(replace(base, overrides=(("U", "ignore"),)), "U"))
    reject("R1430 conflicting duplicate target fails",
           lambda: mode(replace(base, overrides=(("U", "strict"), ("U", "casual"))), "U"))
    check("R1430 recovery uses corrected selected value", mode(base, "U")[0], "casual")

    old_carrier = '[authority_modes]\ndefault = "strict"\n[authority_modes.overrides]\nU = "casual"\n'
    alternative = '[instance_modes]\ndefault = "strict"\n[instance_modes.overrides]\nU = "casual"\n'
    decoded_a = decode_modes(old_carrier)
    decoded_b = decode_modes(alternative, "instance_modes")
    check("Std-change witness different section names equal decoded semantics", decoded_a, decoded_b)
    check("Std-change preserves General results for both targets",
          tuple(mode(decoded_a, target) for target in ("P", "U")),
          tuple(mode(decoded_b, target) for target in ("P", "U")))
    reject("hypothetical alternative is rejected by unchanged D374 Carrier contract",
           lambda: decode_modes(alternative))
    check("Standard recovery returns to admitted Carrier", decode_modes(old_carrier), base)

    # Counterfactual General change: require an explicit selection for every
    # target, without a default. This contradicts R1430 while preserving R1402.
    explicit_only = replace(base, default=None, overrides=(("P", "strict"), ("U", "casual")))
    check("General-change witness preserves settings foundation", foundation(explicit_only), True)
    check("General-change explicit policy retains both intended behaviors",
          tuple(dict(explicit_only.overrides)[target] for target in ("P", "U")), ("strict", "casual"))
    reject("General-change witness violates current default obligation",
           lambda: mode(explicit_only, "P"))
    check("General recovery reinstates current policy", mode(base, "P")[0], "strict")

    roles = {atom_id: record["content_role"] for atom_id, record in by_id.items()}
    e446 = (ROOT / by_id["CA-E-446"]["relative_path"]).read_text()
    relation_block = e446.split("  evaluation_for:\n", 1)[1].split("\n---", 1)[0]
    real_targets = tuple(re.findall(r'^    - "([^"]+)"$', relation_block, re.M))
    check("M265 real E446 targets resolve to Requirement and Delivery groups",
          groups(real_targets, roles), frozenset(("Er", "Ed")))
    rm_d = ("CA-R-1402", "CA-M-235", "CA-D-280")
    for order in permutations(rm_d):
        require(groups(order, roles) == frozenset(("Er", "Em", "Ed")), "target-order dependence")
    check("M265 every group independent of all six target orders", len(tuple(permutations(rm_d))), 6)
    check("M265 duplicate references cannot invent another group",
          groups(rm_d + ("CA-R-1402",), roles), groups(rm_d, roles))
    check("M265 no individual targets yields no invented group", groups((), roles), frozenset())
    reject("M265 unresolved target fails", lambda: groups(("missing",), roles))
    reject("M265 non-RMED target fails", lambda: groups(("plan",), {"plan": "P"}))
    check("M265 recovery resolves target before grouping", groups(("CA-M-235",), roles), frozenset(("Em",)))
    # A stored list, a set, and reverse traversal are alternative realizations
    # of the same extensional specification, not new methodology Atoms.
    check("M265 realization change preserves General relation",
          groups(tuple(reversed(real_targets)), roles), groups(set(real_targets), roles))
    check("M265 first-target-only policy is a substantive General counterexample",
          groups(real_targets[:1], roles) == groups(real_targets, roles), False)

    check("M235 exact prefix serialization positive", parse_cardinality("=1 Author"), ("=", 1, "Author"))
    reject("M235 equivalent count meaning does not satisfy prefix placement",
           lambda: parse_cardinality("Author =1"))
    reject("M235 negative integer counterexample", lambda: parse_cardinality("=-1 Author"))
    check("M235 recovery restores required placement", parse_cardinality(">=0 Property"), (">=", 0, "Property"))
    check("D280 word operator rendering positive", operator_rendering("must", "**must**"), "must")
    check("D280 symbolic operator rendering positive", operator_rendering("=1", "**`=1`**", True), "=1")
    reject("D280 uppercase spelling counterexample", lambda: operator_rendering("must", "**MUST**"))
    reject("D280 symbolic inline-code omission fails", lambda: operator_rendering("=1", "**=1**", True))
    check("D280 recovery preserves operator semantics", operator_rendering("=1", "**`=1`**", True), "=1")
    check("D368 integer percentage field decodes", confidence_field(
        '[confidence]\nnecessary_information_threshold_percent = 99\n'), 99)
    reject("D368 string percentage fails", lambda: confidence_field(
        '[confidence]\nnecessary_information_threshold_percent = "99"\n'))
    reject("D368 alternate field spelling fails", lambda: confidence_field(
        '[confidence]\nthreshold = 99\n'))
    check("D368 recovery restores field and type", confidence_field(
        '[confidence]\nnecessary_information_threshold_percent = 99\n'), 99)

    mapping = runpy.run_path(str(HERE / "CA-P-954-authority-mapping-cases.py"))
    parents = {"PROJECT": None, "U": "PROJECT"}
    check("E428 proposed Project tier criteria include General",
          tuple(mapping["global_tier"]("PROJECT", tier, parents) for tier in ("Principle", "Core", "General", "Standard")),
          (0, 1, 2, 3))
    check("E428 historical Project Standard rank 2 is rejected",
          mapping["global_tier"]("PROJECT", "Standard", parents) == 2, False)
    reject("E428 non-Project Principle fails", lambda: mapping["global_tier"]("U", "Principle", parents))
    check("E428 recovery uses current structural rank", mapping["global_tier"]("U", "Standard", parents), 6)
    check("tier definition subject does not change its own observed Local Tier",
          by_id["CA-R-658"]["current_local_tier"], "Core")
    check("tier definition peers cannot become authority parents by value order",
          mapping["tier_parent"]("CORE_META_MODEL", "Core", "CORE_META_MODEL", "Core"), False)
    reject("Core definition mentioning Principle cannot be a non-Project Principle Atom",
           lambda: mapping["global_tier"]("U", "Principle", parents))

    projects = {project: {"settings_owner": project, "structure": ("U",),
                          "active_goals": (), "projection_writes_source": False}
                for project in ("P", "Q")}
    check("E446 two-Project scenario satisfies bounded oracle", validate_case(projects), True)
    for key, bad_value in (("settings_owner", "P"), ("structure", ()),
                           ("active_goals", ("Draft Goal",)), ("projection_writes_source", True)):
        bad = {project: dict(data) for project, data in projects.items()}
        bad["Q"][key] = bad_value
        reject(f"E446 {key} counterexample rejected", lambda bad=bad: validate_case(bad))
    check("E446 recovery restores Project-local source state", validate_case(projects), True)
    third = dict(projects, Z=dict(projects["Q"], settings_owner="Z"))
    check("E446 alternative concrete three-Project case preserves boundary oracle", validate_case(third), True)

    scope = runpy.run_path(str(HERE / "CA-P-953-scope-design-cases.py"))
    atoms = tuple(scope["Atom"](atom_id, "CORE_META_MODEL", by_id[atom_id]["content_role"],
                               subject=atom_id, claim_constraints=by_id[atom_id]["sha256"])
                  for atom_id in ("CA-R-1402", "CA-M-235", "CA-E-446", "CA-D-280"))
    baseline = scope["derive"]("CORE_META_MODEL", atoms)
    assignments = 0
    for tiers in product(("Core", "General", "Standard"), repeat=4):
        require(scope["derive"]("CORE_META_MODEL", tuple(replace(a, tier=t) for a, t in zip(atoms, tiers))) == baseline,
                "tier change altered Scope basis")
        assignments += 1
    check("source-bound RMED identities and Claims survive all tier assignments", assignments, 81)
    for tier in ("Core", "General", "Standard"):
        check(f"{tier} source rejects local replacement",
              mapping["extension_action"]("replace", True, tier), False)
    check("Standard omitted default", mapping["tier_from_segment"](""), "Standard")
    reject("explicit STD is not canonical", lambda: mapping["tier_from_segment"]("STD"))
    reject("unresolved classification cannot fall back to omitted Standard",
           lambda: mapping["classify"](None))

    print(json.dumps({"non_authoritative": True, "case_count": len(passed), "passed": passed,
                      "frontier_hashes_verified": len(inventory["records"]),
                      "frontier_candidate_membership_verified": True,
                      "source_contracts_bound": len(source_evidence),
                      "source_evidence": source_evidence,
                      "real_E446_target_count": len(real_targets),
                      "scope_tier_assignments": assignments,
                      "automated_natural_language_classification": False,
                      "installed_integration_test": False, "live_authority_changed": False}, indent=2))


if __name__ == "__main__":
    main()
