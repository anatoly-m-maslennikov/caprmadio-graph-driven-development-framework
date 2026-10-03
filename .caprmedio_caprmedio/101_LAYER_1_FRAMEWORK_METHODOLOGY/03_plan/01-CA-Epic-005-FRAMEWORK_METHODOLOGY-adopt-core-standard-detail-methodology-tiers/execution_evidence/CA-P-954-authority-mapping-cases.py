"""Finite CA-P-954 design checks; no live authority or production code is changed.

Semantic fixture qualifications are already resolved. These checks exercise the
specified mappings and failure boundaries, not a general natural-language parser.
The CA-P-953 membership model is reused with the accepted current tier names.
"""

from dataclasses import replace
from itertools import product
from pathlib import Path
import json
import runpy


TIERS = ("Core", "General", "Standard")
TOKENS = {"PRINCIPLE": "Principle", "CORE": "Core", "GENERAL": "General", "": "Standard"}
QUALIFICATIONS = {"foundation": "Core", "shared_specification": "General", "concrete": "Standard"}


def depth(unit, parents, project="PROJECT", visiting=()):
    if unit not in parents:
        raise ValueError("unresolved structural owner")
    if unit == project:
        return 0
    if unit in visiting:
        raise ValueError("cyclic parentage")
    if parents[unit] is None:
        raise ValueError("unanchored structural component")
    return depth(parents[unit], parents, project, visiting + (unit,)) + 1


def global_tier(unit, tier, parents):
    d = depth(unit, parents)
    if tier == "Principle":
        if d != 0:
            raise ValueError("Principle is Project-only")
        return 0
    if tier not in TIERS:
        raise ValueError("unresolved Local Tier")
    return 3 * d + TIERS.index(tier) + 1


def goal(target, parents):
    if target == "PROJECT":
        return ("OPERATOR", None, -1)
    depth(target, parents)
    owner = parents[target]
    return (owner, "Standard", global_tier(owner, "Standard", parents))


def tier_from_segment(segment, *, external_goal=False):
    if external_goal:
        if segment:
            raise ValueError("external Project Goal cannot have a tier token")
        return None
    if segment not in TOKENS:
        raise ValueError("noncanonical Local Tier segment")
    return TOKENS[segment]


def classify(qualification, *, role="R", type_name=None, old_tier=None, source=None):
    if role not in "CAPRMEDIO" or qualification not in QUALIFICATIONS:
        raise ValueError("unresolved semantic qualification")
    tier = QUALIFICATIONS[qualification]
    if type_name == "Implementation Decision" and tier != "Standard":
        raise ValueError("concrete Implementation Decision requires Standard")
    return tier


def tier_parent(child_owner, child_tier, parent_owner, parent_tier):
    order = ("Principle", *TIERS)
    return (child_owner == parent_owner and child_tier in order and parent_tier in order
            and order.index(parent_tier) < order.index(child_tier))


def extension_action(operation, permission, source_tier):
    if source_tier not in TIERS:
        raise ValueError("unresolved source tier")
    return operation == "add_at_permitted_boundary" and permission


def main():
    passed = []

    def check(name, actual, expected):
        assert actual == expected, (name, actual, expected)
        passed.append(name)

    def reject(name, action):
        try:
            action()
        except ValueError:
            passed.append(name)
        else:
            raise AssertionError(name)

    parents = {"PROJECT": None, "CHILD": "PROJECT", "SIBLING": "PROJECT", "GRANDCHILD": "CHILD"}
    check("Project complete block", tuple(global_tier("PROJECT", t, parents) for t in ("Principle", *TIERS)), (0, 1, 2, 3))
    check("first child complete block", tuple(global_tier("CHILD", t, parents) for t in TIERS), (4, 5, 6))
    check("grandchild complete block", tuple(global_tier("GRANDCHILD", t, parents) for t in TIERS), (7, 8, 9))
    check("siblings share positions without sharing ownership", global_tier("SIBLING", "General", parents), 5)
    check("Project Goal exception", goal("PROJECT", parents), ("OPERATOR", None, -1))
    check("child Goal remains parent Standard", goal("CHILD", parents), ("PROJECT", "Standard", 3))
    check("grandchild Goal remains parent Standard", goal("GRANDCHILD", parents), ("CHILD", "Standard", 6))
    reject("non-Project Principle rejected", lambda: global_tier("CHILD", "Principle", parents))
    reject("unknown Local Tier rejected", lambda: global_tier("CHILD", "Detail", parents))
    reject("unadmitted outside owner rejected", lambda: global_tier("BOOTSTRAP", "Core", parents))
    reject("missing parent unresolved", lambda: global_tier("CHILD", "Core", {"CHILD": "MISSING"}))
    reject("cycle unresolved", lambda: global_tier("A", "Core", {"A": "B", "B": "A"}))
    reject("unanchored component unresolved", lambda: global_tier("OUTSIDE", "Core", {"OUTSIDE": None}))

    chain = {"PROJECT": None}
    previous = "PROJECT"
    for d in range(1, 41):
        unit = f"DEPTH-{d}"
        chain[unit] = previous
        assert global_tier(unit, "Core", chain) == global_tier(previous, "Standard", chain) + 1
        assert goal(unit, chain)[2] == 3 * d
        previous = unit
    check("forty-level recursive Goal and block mapping", global_tier(previous, "Standard", chain), 123)

    check("current canonical segment mapping", tuple(tier_from_segment(t) for t in TOKENS), ("Principle", "Core", "General", "Standard"))
    check("Goal omission differs from ordinary default", tier_from_segment("", external_goal=True), None)
    for token in ("STD", "STANDARD", "DETAIL", "CORE_META_MODEL", "core"):
        reject(f"noncanonical segment {token} rejected", lambda token=token: tier_from_segment(token))
    reject("Goal explicit token rejected", lambda: tier_from_segment("GENERAL", external_goal=True))
    for old in ("Core", "Standard"):
        check(f"old {old} does not fix new classification", tuple(classify(q, old_tier=old) for q in QUALIFICATIONS), TIERS)
    check("source owner does not fix Local Tier", classify("concrete", source="CORE_META_MODEL"), "Standard")
    reject("omission is not evidence of new semantic class", lambda: classify(None, old_tier="Standard"))
    reject("mixed unresolved semantics rejected", lambda: classify("foundation+concrete"))
    for role in "CAPRMEDIO":
        check(f"role {role} does not force a tier", tuple(classify(q, role=role) for q in QUALIFICATIONS), TIERS)
    check("Implementation Method supports all semantic levels", tuple(classify(q, role="M", type_name="Implementation Method") for q in QUALIFICATIONS), TIERS)
    check("concrete Decision remains Standard", classify("concrete", role="M", type_name="Implementation Decision"), "Standard")
    reject("Decision cannot be promoted by reusability", lambda: classify("shared_specification", role="M", type_name="Implementation Decision"))
    check("same-scope General parent for Standard", tier_parent("UNIT", "Standard", "UNIT", "General"), True)
    check("direct Core parent can skip empty General", tier_parent("UNIT", "Standard", "UNIT", "Core"), True)
    check("same-tier peers cannot be tier parents", tier_parent("UNIT", "General", "UNIT", "General"), False)
    check("tier parent cannot cross Atom Scope", tier_parent("CHILD", "Standard", "PROJECT", "Core"), False)
    prohibited_actions = 0
    for tier in TIERS:
        check(f"{tier} source admits permitted expansion", extension_action("add_at_permitted_boundary", True, tier), True)
        check(f"{tier} source rejects unpermitted expansion", extension_action("add_at_permitted_boundary", False, tier), False)
        for operation in ("replace", "weaken", "shadow", "delete", "reinterpret", "mutate", "contradict"):
            assert not extension_action(operation, True, tier)
            prohibited_actions += 1
    check("replacement prohibited across every source tier", prohibited_actions, 21)

    scope_model = runpy.run_path(str(Path(__file__).with_name("CA-P-953-scope-design-cases.py")))
    Atom, derive = scope_model["Atom"], scope_model["derive"]
    atoms = tuple(Atom(f"FIX-{role}", "UNIT", role) for role in "RMED")
    expected = derive("UNIT", atoms)
    assignments = 0
    for tiers in product(TIERS, repeat=4):
        changed = tuple(replace(atom, tier=tier) for atom, tier in zip(atoms, tiers))
        assert derive("UNIT", changed) == expected
        assignments += 1
    check("Scope unchanged under all current-name tier assignments", assignments, 81)
    check("empty basis still empty", derive("EMPTY", atoms), ())
    reject("incomplete Scope still unresolved", lambda: derive("UNIT", atoms, complete=False))
    print(json.dumps({"non_authoritative": True, "case_count": len(passed), "passed": passed,
                      "scope_tier_assignments": assignments, "recursive_depths": 40,
                      "production_parser_tested": False, "live_authority_changed": False}, indent=2))


if __name__ == "__main__":
    main()
