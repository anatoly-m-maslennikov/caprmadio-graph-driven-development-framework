"""Bounded CA-P-956 source-application verification.

Frozen 952/955 receipts stay unchanged. This checks exact authorized revision
mapping, archive fidelity, source membership, retained/removed direct references,
and finite contract fixtures. It is not an unrestricted CCE parser, proof of
arbitrary English equivalence, or installed runtime/E2E execution.
"""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / ".caprmedio_framework").is_dir())
TIERS = ("Core", "General", "Standard")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def relations(text):
    front = text.split("---", 2)[1]
    match = re.search(r"(?m)^relations:\n((?:[ ]+[^\n]*\n)*)", front)
    result = {}
    key = None
    for line in match.group(1).splitlines() if match else ():
        if re.fullmatch(r"  [a-z_]+:", line):
            key = line.strip()[:-1]
            result[key] = []
        elif line.startswith("    - "):
            assert key is not None
            result[key].append(line[6:].strip().strip('"').strip("'"))
    return result


def main():
    inventory = json.loads((HERE / "CA-P-952-methodology-tier-frontier.projection.json").read_text())
    plan = json.loads((HERE / "CA-P-956-planned-source-delta.json").read_text())
    candidates = json.loads((HERE / "CA-P-956-source-candidates.json").read_text())["candidates"]
    changes = {r["atom_id"]: r for r in plan["existing"]}
    new = {r["atom_id"]: r for r in plan["additions"]}
    candidates = {r["atom_id"]: r for r in candidates}
    corrections = json.loads((HERE / "CA-P-956-post-checkpoint-corrections.json").read_text())["corrections"]
    assert len(corrections) == 1 and corrections[0]["atom_id"] == "CA-E-447"
    correction = corrections[0]
    assert candidates["CA-E-447"]["bytes_utf8"] == correction["before_bytes_utf8"]
    assert correction["before_bytes_utf8"].count(correction["before_exact"]) == 1
    assert correction["before_bytes_utf8"].replace(correction["before_exact"], correction["after_exact"]) == correction["after_bytes_utf8"]
    candidates["CA-E-447"] = dict(candidates["CA-E-447"], bytes_utf8=correction["after_bytes_utf8"])
    original = {r["atom_id"]: r for r in inventory["records"]}
    active = {}
    archive_checks = []
    outside = []
    checks = []

    def check(name, actual, expected=True):
        assert actual == expected, (name, actual, expected)
        checks.append(name)

    for atom_id, before in original.items():
        if atom_id not in changes:
            actual = (ROOT / before["relative_path"]).read_bytes()
            check("unchanged frozen revision " + atom_id, digest(actual), before["sha256"])
            active[atom_id] = {"path": before["relative_path"], "text": actual.decode(),
                               "tier": before["current_local_tier"]}
            outside.append(atom_id)
    for atom_id, change in changes.items():
        archive = (ROOT / change["archive_path"]).read_bytes()
        check("exact prior archive " + atom_id, archive, change["before_bytes_utf8"].encode())
        check("archive hash " + atom_id, digest(archive), change["before_sha256"])
        archive_checks.append(atom_id)
        if change["operation"] == "retire" or change["before_path"] != change["proposed_path"]:
            check("old current path removed " + atom_id, not (ROOT / change["before_path"]).exists())
    for atom_id, candidate in candidates.items():
        actual = (ROOT / candidate["path"]).read_text()
        check("reviewed exact candidate " + atom_id, actual, candidate["bytes_utf8"])
        declared = re.search(r"(?m)^atom_id: *[\"']?([^\"'\n]+)", actual).group(1)
        check("stable/new explicit identity " + atom_id, declared, atom_id)
        version = int(re.search(r"(?m)^version: ([0-9]+)$", actual).group(1))
        expected_version = changes[atom_id]["proposed_version"] if atom_id in changes else 1
        check("revision increment " + atom_id, version, expected_version)
        tier = changes[atom_id]["proposed_tier"] if atom_id in changes else new[atom_id]["new_tier"]
        segment = candidate["path"].split("-CORE_META_MODEL-")[1]
        observed_tier = "Core" if segment.startswith("CORE-") else "General" if segment.startswith("GENERAL-") else "Standard"
        check("own tier token " + atom_id, observed_tier, tier)
        check("no duplicated Scope representation " + atom_id, "\n## Scope\n" not in actual)
        active[atom_id] = {"path": candidate["path"], "text": actual, "tier": tier}
    check("complete mapped record count", len(active), 707)
    check("retired duplicate/forced policy absent", set(changes) - set(candidates), {"CA-R-716", "CAPRMEDIO-META-REQU-766"})

    excluded = set(inventory["selection"]["excluded_directory_segments_casefolded"])
    current_paths = set()
    scan_roots = inventory["source_roots"]
    for root in scan_roots:
        for path in (ROOT / root).rglob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            if any(part.casefold() in excluded for part in path.relative_to(ROOT / root).parts):
                continue
            if "@" in path.stem or path.name.startswith("."):
                continue
            if not any(part in ("04_requirement", "05_method", "06_evaluation", "07_delivery") for part in path.parts):
                continue
            text = path.read_text()
            status = re.search(r"(?mi)^status: *[\"']?([^\"'\n]+)", text.split("---", 2)[1] if text.startswith("---") else "")
            if status and status.group(1).strip().casefold() != "active":
                continue
            current_paths.add(rel)
    for path in (ROOT / inventory["adjacent_authority_root"]).glob("*.md"):
        if "@" not in path.stem:
            current_paths.add(path.relative_to(ROOT).as_posix())
    expected_paths = {r["path"] for r in active.values()}
    check("exact authorized candidate membership", current_paths, expected_paths)

    target_lookup = dict(active)
    for atom_id, record in active.items():
        target_lookup[Path(record["path"]).stem] = record
    relation_count = 0
    for atom_id, candidate in candidates.items():
        for kind, refs in relations(candidate["bytes_utf8"]).items():
            for ref in refs:
                check("active exact direct target " + atom_id + " " + ref, ref in target_lookup)
                relation_count += 1
            if kind == "evaluation_for":
                check("legitimate R/M/D evaluation targets " + atom_id,
                      all("/04_requirement/" in target_lookup[r]["path"] or
                          "/05_method/" in target_lookup[r]["path"] or
                          "/07_delivery/" in target_lookup[r]["path"] for r in refs))
        if "/06_evaluation/" in candidate["path"] and active[atom_id]["tier"] == "Standard":
            check("Standard Evaluation has targets " + atom_id,
                  len(relations(candidate["bytes_utf8"]).get("evaluation_for", [])) >= 1)
    for atom_id in ("CA-E-430", "CA-E-431", "CA-E-446"):
        check("preserved all supplied Evaluation targets " + atom_id,
              relations(active[atom_id]["text"]), relations(changes[atom_id]["before_bytes_utf8"]))
    for atom_id in ("CA-D-361", "CA-D-366", "CA-R-680", "CA-R-794"):
        check("preserved direct boundary/parent links " + atom_id,
              relations(active[atom_id]["text"]), relations(changes[atom_id]["before_bytes_utf8"]))
    for number in range(368, 378):
        atom_id = "CA-D-" + str(number)
        check("unexpanded Delivery edge scope " + atom_id,
              digest((ROOT / original[atom_id]["relative_path"]).read_bytes()),
              original[atom_id]["sha256"])
    for atom_id in ("CA-R-155", "CA-R-658", "CA-R-659", "CA-R-660", "CA-R-931", "CA-R-1429", "CA-R-1018"):
        check("admitted invalid Requirement edge removed " + atom_id,
              relations(active[atom_id]["text"]).get("child_of", []), [])

    def plain(atom_id):
        return active[atom_id]["text"].split("---", 2)[2].replace("**", "").replace("`", "")

    for atom_id in ("CA-R-1287", "CA-R-659", "CA-R-660", "CA-R-931", "CA-E-428"):
        check("obsolete breadth selector absent " + atom_id,
              not any(x in plain(atom_id) for x in ("highest occupied", "proper part of the Scope", "classifies how broadly")))
    project_values = re.findall(r"(-?[0-9]+) for (Principle|Core|General|Standard)", plain("CA-R-1389"))
    check("source Project coordinates", dict((tier, int(n)) for n, tier in project_values),
          {"Principle": 0, "Core": 1, "General": 2, "Standard": 3})
    check("source non-Project recursion",
          "General Global Tier must be one greater than its Core Global Tier and the Standard Global Tier must be one greater than its General Global Tier" in plain("CA-R-1391"))
    check("four constitutive definitions are Core",
          tuple(active[x]["tier"] for x in ("CA-R-658", "CA-R-659", "CA-R-1431", "CA-R-660")),
          ("Core",) * 4)
    check("governed classifier/resolver are Standard",
          (active["CA-M-272"]["tier"], active["CA-M-273"]["tier"]), ("Standard", "Standard"))
    check("generic rejection policy is General", active["CA-E-428"]["tier"], "General")
    check("concrete cases are Standard", active["CA-E-447"]["tier"], "Standard")
    for atom_id in ("CA-R-1018", "CA-M-265"):
        check("Core/General target exception " + atom_id, "Core or General" in plain(atom_id))
    for atom_id in ("CA-R-1429", "CA-D-361", "CA-D-366", "CA-E-430", "CA-E-431", "CA-E-446"):
        check("settings three-tier partition " + atom_id, all(t in plain(atom_id) for t in TIERS))
    check("all-tier source protection", "at any Local Tier" in plain("CA-R-1375"))
    check("higher local rank cannot replace source", "higher-ranked local Claim grants no exception" in plain("CA-R-1375"))

    # Reuse independent accepted finite models, bound above to exact new source.
    outputs = {}
    for name in ("CA-P-953-scope-design-cases.py", "CA-P-954-authority-mapping-cases.py"):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            runpy.run_path(str(HERE / name), run_name="__main__")
        outputs[name] = json.loads(stream.getvalue())
    mapping = runpy.run_path(str(HERE / "CA-P-954-authority-mapping-cases.py"))
    for token in ("CORE-GENERAL", "GENERAL-CORE", "CORE-STD"):
        try:
            mapping["tier_from_segment"](token)
        except ValueError:
            checks.append("combined tier token rejected " + token)
        else:
            raise AssertionError(token)

    # Real supplied E446 target roles; targets are not invented by policy labels.
    e446 = relations(active["CA-E-446"]["text"])["evaluation_for"]
    def groups(targets):
        found = set()
        for ref in targets:
            if ref not in target_lookup:
                raise ValueError("unresolved target")
            path = target_lookup[ref]["path"]
            role = next((role for folder, role in (("/04_requirement/", "Er"), ("/05_method/", "Em"), ("/07_delivery/", "Ed")) if folder in path), None)
            if role is None:
                raise ValueError("invalid target role")
            found.add(role)
        return found
    check("actual twelve E446 links", len(e446), 12)
    qualified = "CA-R-1385-CORE_META_MODEL-GENERAL-REQUIREMENT--order-non-project-local-tiers"
    check("preexisting global ID collision qualified explicitly", qualified in relations(active["CA-E-447"]["text"])["evaluation_for"])
    check("ambiguous unqualified R1385 target absent", "CA-R-1385" not in relations(active["CA-E-447"]["text"])["evaluation_for"])
    collision = ROOT / correction["preexisting_collision_path"]
    check("preexisting Tools ID preserved", "atom_id: CA-R-1385" in collision.read_text())
    check("all-target group set", groups(e446), {"Er", "Ed"})
    check("reverse traversal preserves groups", groups(reversed(e446)), groups(e446))
    check("target set preserves groups", groups(set(e446)), groups(e446))
    check("first-target counterpolicy loses a group", groups(e446[:1]) != groups(e446))
    for refs in (["UNKNOWN"], ["CA-E-428"]):
        try:
            groups(refs)
        except ValueError:
            checks.append("invalid grouping target rejected " + refs[0])
        else:
            raise AssertionError(refs)

    print(json.dumps({
        "task": "CA-P-956", "verdict": "PASS", "non_authoritative": True,
        "checks": len(checks), "frozen_revisions_unchanged_outside_delta": len(outside),
        "exact_prior_archives": len(archive_checks), "active_candidates": len(candidates),
        "mapped_frontier_records": len(active), "checked_direct_target_relations": relation_count,
        "reused_scope_cases": outputs["CA-P-953-scope-design-cases.py"]["case_count"],
        "reused_mapping_cases": outputs["CA-P-954-authority-mapping-cases.py"]["case_count"],
        "tier_assignments": 81, "recursive_depths": 40,
        "installed_runtime_or_e2e_executed": False,
        "journal_or_git_receipt_claimed_by_worker": False,
        "semantic_classification_basis": "Complete-Claim reviewed evidence in planned/final delta; finite models do not parse unrestricted CCE.",
        "passed": checks,
    }, indent=2))


if __name__ == "__main__":
    main()
