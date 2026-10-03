"""Bounded read-only source/evidence closure checks for CA-P-957; no classifier or runtime."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import runpy
import subprocess
import sys

HERE = Path(__file__).resolve().parent
H = runpy.run_path(str(HERE / "CA-P-957-evidence.py"))
ROOT = H["ROOT"]
def sha(data):
    return hashlib.sha256(data).hexdigest()

def collect():
    inv, prior, active, origins = H["frontier"]()
    ledger = json.loads((HERE / "CA-P-957-master-review-ledger.json").read_text())
    assert len(origins) == len(ledger["records"]) == 620
    assert len({r["atom_id"] for r in ledger["records"]}) == 620
    assert all(r["batch"] is not None for r in ledger["records"])
    batches = sorted(ledger["batch_registry"], key=lambda r: int(r["batch"]))
    evidence = {}
    for batch in batches:
        _, plan = H["read_batch_plan"](batch["batch"])
        for r in H["read_batch_dispositions"](batch["batch"], plan):
            if r.get("cross_frontier_dependency_repair"):
                continue
            if r["decisive_test"] not in ("dependency_repair_only", "reference_binding_only"):
                evidence[r["atom_id"]] = dict(r, evidence_record=batch["dispositions"] + "#" + r["atom_id"])
    assert set(evidence) == {r["atom_id"] for r in origins}
    paths = json.loads((HERE / "CA-P-957-applied-source-delta.json").read_text())["applied_batch_mappings"]
    changes, additions, compact = [], [], []
    for name in paths:
        batch = json.loads((HERE / name).read_text())
        for row in batch["existing"]:
            x = dict(row, batch=batch["batch"], mapping=name)
            changes.append(x)
            compact.append({k: x.get(k) for k in ("atom_id", "batch", "operation", "before_path", "before_version", "before_sha256", "archive_path", "archive_sha256", "after_path", "after_version", "after_sha256", "after_tier", "mapping")})
        additions.extend(dict(r, batch=batch["batch"], mapping=name) for r in batch.get("additions", []))
    core_ids = {r["atom_id"] for r in origins}
    core_changes = [r for r in changes if r["atom_id"] in core_ids]
    local_changes = [r for r in changes if r["atom_id"] not in core_ids]
    for r in origins:
        if not r.get("retired_by_957"):
            assert evidence[r["atom_id"]]["new_tier"] == r["current_local_tier"], ("tier/evidence mismatch", r["atom_id"])
    extra_roles = {r["atom_id"]: r["content_role"] for r in prior["additions"]}
    def counts(rows):
        out = {role: dict(Counter(r["current_local_tier"] for r in rows if r.get("content_role", extra_roles.get(r["atom_id"])) == role)) for role in "RMED"}
        out["total"] = dict(Counter(r["current_local_tier"] for r in rows))
        return out
    core_active = [r for r in active if r["source_scope_unit"] == "CORE_META_MODEL"]
    origin_active = [r for r in origins if not r.get("retired_by_957")]
    excluded = [r for r in core_active if r["excluded_as_956_result"]]
    new = [r for r in core_active if r.get("added_by_957")]
    assert len(excluded) == 32 and len(new) == 3 and len(core_active) == 648
    assert len(active) == 703 and len(origin_active) == 613
    assert len([r for r in core_changes if r["operation"] == "retire"]) == 7
    assert len({r["archive_path"] for r in changes}) == len(changes)
    # All exact histories are checked by frontier and each frozen applied checker.
    external = []
    for p in sorted(HERE.glob("CA-P-957-external*.json")):
        external.append(dict(path=p.name, sha256=sha(p.read_bytes())))
    summary = dict(
        result="PASS", original_dispositions=620, unclassified_origins=0,
        active_originals=613, retired_originals=7, new_authorities=3,
        active_core_source=648, excluded_956_results=32, mapped_active=703,
        original_active_counts=counts(origin_active), new_authority_counts=counts(new),
        excluded_956_counts=counts(excluded), all_core_source_counts=counts(core_active),
        core_revision_operations=sum(r["operation"] == "revise" for r in core_changes),
        core_unique_revised_origins=len({r["atom_id"] for r in core_changes if r["operation"] == "revise"}),
        unchanged_origin_count=620-len({r["atom_id"] for r in core_changes}),
        local_reference_revision_operations=len(local_changes),
        local_reference_identities=len({r["atom_id"] for r in local_changes}),
        exact_prior_archives=len(changes), total_revision_operations=sum(r["operation"] == "revise" for r in changes),
        external_root_evidence=external,
        limit="Exact source lineage/frontier and explicit per-origin evidence closure; not runtime, Journal, global relation-registry or source-owner migration conformance."
    )
    return summary, origins, evidence, changes, additions, compact, ledger

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-ledger", action="store_true")
    ap.add_argument("--check-batches", action="store_true")
    ap.add_argument("--check-external", action="store_true")
    ap.add_argument("--check-references", action="store_true")
    args = ap.parse_args()
    summary, origins, evidence, changes, additions, compact, ledger = collect()
    if args.check_external:
        records = []
        for item in summary["external_root_evidence"]:
            value = json.loads((HERE / item["path"]).read_text())
            records.extend(value.get("records", [value]))
        for row in records:
            archive_path = row.get("archive_path", row.get("exact_prior_archive"))
            before = (ROOT / archive_path).read_bytes()
            assert sha(before) == row["before_sha256"]
            path = row.get("after_path", row.get("path"))
            after = (ROOT / path).read_bytes()
            if sha(after) != row["after_sha256"]:
                successor = next(r for r in records if r["atom_id"] == row["atom_id"] and r["before_sha256"] == row["after_sha256"])
                after = (ROOT / successor.get("archive_path", successor.get("exact_prior_archive"))).read_bytes()
            assert sha(after) == row["after_sha256"]
            assert before.decode().split("---", 2)[2] == after.decode().split("---", 2)[2]
        summary["external_project_reference_revisions_verified"] = len(records)
        summary["external_project_identities_verified"] = len({r["atom_id"] for r in records})
    if args.check_references:
        tool = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"
        sys.path[:0] = [str(tool), str(tool / "COMMIT_CONTEXT")]
        import commit_context_logic as canonical
        graph = canonical.working_graph(ROOT)
        obsolete = {Path(r["before_path"]).stem for r in changes if r["operation"] == "retire" or r.get("after_path") != r["before_path"]}
        retired = {r["atom_id"] for r in changes if r["operation"] == "retire"}
        dangling = []
        for carrier in {c.path: c for c in graph.values()}.values():
            for kind, targets in carrier.relations.items():
                for target in targets:
                    if Path(target).name.removesuffix(".md") in obsolete or target in retired:
                        dangling.append((carrier.identity, kind, target))
        assert not dangling, dangling
        summary["dangling_changed_relation_references"] = 0
    if args.check_ledger:
        rows = {r["atom_id"]: r for r in ledger["records"]}
        for source in origins:
            row = rows[source["atom_id"]]
            assert row["classification_complete"]
            if source.get("retired_by_957"):
                assert row["outcome"] == "absorbed_retired" and row["current_path"] is None
                assert row["archive_path"] == source["relative_path"]
            else:
                assert (row["current_path"], row["current_version"], row["current_sha256"], row["current_tier"]) == (source["relative_path"], source["version"], source["sha256"], source["current_local_tier"])
            assert row["final_disposition_record"] == evidence[source["atom_id"]]["evidence_record"]
            assert not any(t in row["review_state"].lower() for t in ("pending", "await", "blocked", "root go"))
    if args.check_batches:
        results = []
        for row in sorted(ledger["batch_registry"], key=lambda r: int(r["batch"])):
            batch = row["batch"]
            flag = "--check-applied-batch" if (HERE / ("CA-P-957-batch-" + batch + "-applied-source-delta.json")).exists() else "--check-batch"
            result = subprocess.run([sys.executable, str(HERE / "CA-P-957-evidence.py"), flag, batch], capture_output=True, text=True)
            assert result.returncode == 0, (batch, result.stdout, result.stderr)
            results.append(batch)
        summary["exact_batch_checks"] = results
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
