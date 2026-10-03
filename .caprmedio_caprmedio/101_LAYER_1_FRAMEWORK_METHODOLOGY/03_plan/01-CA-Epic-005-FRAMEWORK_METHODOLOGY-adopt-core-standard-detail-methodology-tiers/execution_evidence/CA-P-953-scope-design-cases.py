"""Non-authoritative finite model for CA-P-953; never reads or changes authority.

The model consumes already resolved Claim Scope bindings. It is neither a CCE
parser nor proof that arbitrary live expressions have been resolved correctly.
All fixture IDs and scope names are synthetic; no persistent model is proposed.
"""

from dataclasses import dataclass, replace
from itertools import product
import json


@dataclass(frozen=True)
class Atom:
    atom_id: str
    owner: str
    role: str
    status: str = "Active"
    tier: str = "Core"
    binding: str = "current"
    explicit_scope: str | None = None
    subject: str = "fixture-subject"
    claim_constraints: str = "fixture-content-constraints"


def derive(unit, atoms, *, complete=True, coherent=True):
    """Select the basis after tier-independent ownership/scope resolution."""
    if not complete or not coherent:
        raise ValueError("unresolved source frontier")
    selected = []
    for atom in atoms:
        if atom.owner != unit or atom.status != "Active" or atom.role not in ("R", "M", "E", "D"):
            continue
        if atom.binding not in ("current", "different"):
            raise ValueError(f"unresolved Claim Scope: {atom.atom_id}")
        if atom.binding == "current" and atom.explicit_scope is not None:
            raise ValueError(f"redundant explicit current scope: {atom.atom_id}")
        if atom.binding == "different" and atom.explicit_scope is None:
            raise ValueError(f"missing relational scope: {atom.atom_id}")
        if atom.binding == "current":
            selected.append((atom.atom_id, atom.owner, atom.binding,
                             atom.subject, atom.claim_constraints))
    return tuple(sorted(selected))


def ids(result):
    return tuple(row[0] for row in result)


def main():
    passed = []

    def check(name, actual, expected):
        assert actual == expected, (name, actual, expected)
        passed.append(name)

    def reject(name, **kwargs):
        try:
            derive("UNIT", **kwargs)
        except ValueError:
            passed.append(name)
        else:
            raise AssertionError(name)

    base = tuple(Atom(f"FIX-{role}", "UNIT", role) for role in "RMED")
    expected = ("FIX-D", "FIX-E", "FIX-M", "FIX-R")
    baseline = derive("UNIT", base)
    check("default admits all four RMED roles", ids(baseline), expected)
    check("contextual components retained", baseline[0][3:],
          ("fixture-subject", "fixture-content-constraints"))

    inactive = tuple(Atom(f"FIX-{status}", "UNIT", "R", status=status)
                     for status in ("Draft", "Archived"))
    check("inactive revisions excluded", ids(derive("UNIT", base + inactive)), expected)
    other_roles = tuple(Atom(f"FIX-{role}", "UNIT", role) for role in ("C", "A", "P", "I", "O"))
    check("non-RMED roles excluded", ids(derive("UNIT", base + other_roles)), expected)

    incoming = (
        Atom("FIX-IN-GOAL", "PARENT", "R", binding="different", explicit_scope="UNIT"),
        Atom("FIX-IN-DEMAND", "PEER", "R", binding="different", explicit_scope="UNIT/result"),
    )
    outgoing = (
        Atom("FIX-OUT-GOAL", "UNIT", "R", binding="different", explicit_scope="CHILD"),
        Atom("FIX-OUT-DEMAND", "UNIT", "R", binding="different", explicit_scope="PEER/result"),
    )
    check("incoming relational ownership retained", ids(derive("UNIT", base + incoming)), expected)
    check("outgoing relational targets retained", ids(derive("UNIT", base + outgoing)), expected)
    descendants = (Atom("FIX-CHILD", "CHILD", "M"), Atom("FIX-GRANDCHILD", "GRANDCHILD", "D"))
    ancestor = (Atom("FIX-INHERITED", "PARENT", "R"),)
    check("descendants not aggregated", ids(derive("UNIT", base + descendants)), expected)
    check("inherited authority not relocalized", ids(derive("UNIT", base + ancestor)), expected)

    composite = Atom("FIX-COMPOSITE", "UNIT", "M", binding="different",
                     explicit_scope="(entity-a or entity-b)")
    check("resolved proper composite stays relational", ids(derive("UNIT", base + (composite,))), expected)
    check("composite expression retained", composite.explicit_scope, "(entity-a or entity-b)")
    check("complete empty basis", derive("EMPTY", base + incoming + ancestor), ())
    reject("incomplete frontier is unresolved", atoms=base, complete=False)
    reject("contradictory frontier is unresolved", atoms=base, coherent=False)
    reject("cyclic or ambiguous binding is unresolved", atoms=base + (
        Atom("FIX-CYCLE", "UNIT", "R", binding="unresolved", explicit_scope="Scope(UNIT)"),))
    reject("explicit current-scope representation rejected", atoms=base + (
        Atom("FIX-REDUNDANT", "UNIT", "D", explicit_scope="UNIT"),))
    reject("missing relational expression rejected", atoms=base + (
        Atom("FIX-MISSING", "UNIT", "E", binding="different"),))

    tier_trials = 0
    for tiers in product(("Core", "Standard", "Detail"), repeat=len(base)):
        changed = tuple(replace(atom, tier=tier) for atom, tier in zip(base, tiers))
        assert derive("UNIT", changed) == baseline
        tier_trials += 1
    check("all independent tier combinations invariant", tier_trials, 81)

    check("activation is an explicit basis change", ids(derive("UNIT", base + (
        Atom("FIX-NEW", "UNIT", "E"),))), ("FIX-D", "FIX-E", "FIX-M", "FIX-NEW", "FIX-R"))
    check("archival is an explicit basis change", ids(derive("UNIT", (
        replace(base[0], status="Archived"),) + base[1:])), ("FIX-D", "FIX-E", "FIX-M"))
    check("ownership change is an explicit basis change", ids(derive("UNIT", (
        replace(base[0], owner="CHILD"),) + base[1:])), ("FIX-D", "FIX-E", "FIX-M"))
    check("claim-scope change is an explicit basis change", ids(derive("UNIT", (
        replace(base[0], binding="different", explicit_scope="CHILD"),) + base[1:])),
          ("FIX-D", "FIX-E", "FIX-M"))

    print(json.dumps({"non_authoritative": True, "case_count": len(passed),
                      "passed": passed, "tier_assignments_checked": tier_trials,
                      "production_parser_tested": False, "live_authority_changed": False},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
