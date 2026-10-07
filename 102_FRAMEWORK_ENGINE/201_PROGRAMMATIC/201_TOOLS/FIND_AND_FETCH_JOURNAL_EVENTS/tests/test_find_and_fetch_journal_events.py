import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
JOURNAL_TOOL = TOOLS / "FIND_AND_FETCH_JOURNAL_EVENTS"
ARTIFACT_TOOL = TOOLS / "FIND_AND_FETCH_ARTIFACTS"
sys.path[:0] = [str(JOURNAL_TOOL), str(ARTIFACT_TOOL)]

from find_and_fetch_journal_events import (  # noqa: E402
    JournalQueryError,
    capture_snapshot,
    query,
)
from query_filter import QueryFilterError, parse_filter_with_stats  # noqa: E402


class JournalQueryGoldenTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.temp.name)
        self.control = self.root / ".caprmedio_fixture"
        journal = self.control / "_journal"
        journal.mkdir(parents=True)
        bootstrap = self.root / ".caprmedio_caprmedio"
        bootstrap.mkdir()
        (bootstrap / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_fixture\"\n", encoding="utf-8"
        )
        defaults = self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        defaults.mkdir(parents=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_text(
            "[query]\n"
            "max_request_bytes = 4096\nmax_grammar_depth = 16\n"
            "max_filter_tokens = 128\nmax_in_members = 16\n"
            "max_selected_fields = 8\nmax_page_size = 2\n"
            "max_snapshot_members = 8\nmax_file_bytes = 4096\n"
            "max_total_read_bytes = 16384\ntimeout_seconds = 10\nmax_findings = 8\n",
            encoding="utf-8",
        )
        self.journal = journal

    def tearDown(self):
        self.temp.cleanup()

    def write_events(self, name, *events):
        path = self.journal / name
        path.write_bytes(b"".join(json.dumps(event, separators=(",", ":")).encode() + b"\n" for event in events))
        return path

    def test_e575_typed_pointer_filtering_missing_vs_null_and_rejections(self):
        path = self.write_events(
            "events.ndjson",
            {"event_id": "E-2", "optional": None, "nested": {"a/b": [False, {"~key": 2}]}, "flag": True},
            {"event_id": "E-1", "nested": {"a/b": [True, {"~key": 1}]}, "a.b": "literal", "flag": 1},
            {"event_id": "E-3", "phase": None, "flag": False},
        )
        snapshot = capture_snapshot(self.root)
        before = path.read_bytes()
        matched = query(snapshot, {"filter": '"event:/optional" = null'})
        self.assertEqual(matched["results"], ["E-2"])
        nested = query(snapshot, {"filter": '"event:/nested/a~1b/1/~0key" = 2'})
        self.assertEqual(nested["results"], ["E-2"])
        structural = query(
            snapshot,
            {"filter": '"event:/nested/a~1b" = [false,{"~key":2}]'},
        )
        self.assertEqual(structural["results"], ["E-2"])
        self.assertEqual(
            query(snapshot, {"filter": '"event:/nested" = {"a/b":[false,{"~key":2}]}'})["results"],
            ["E-2"],
        )
        self.assertEqual(query(snapshot, {"filter": '"event:/flag" = true'})["results"], ["E-2"])
        self.assertEqual(query(snapshot, {"filter": '"event:/a.b" = "literal"'})["results"], ["E-1"])
        literal = query(snapshot, {"mode": "fields", "select": ["event:/a.b"]})
        self.assertEqual(literal["results"][0]["event:/a.b"], "literal")
        self.assertEqual(query(snapshot, {"filter": '"event:/flag" != true'})["results"], ["E-1", "E-3"])
        self.assertEqual(query(snapshot, {"filter": '"event:/flag" IN (true, 1)'})["results"], ["E-1", "E-2"])
        self.assertEqual(
            query(snapshot, {"filter": '"event:/flag" = true AND "event:/optional" = null'})["results"],
            ["E-2"],
        )
        self.assertEqual(
            query(snapshot, {"filter": '"event:/flag" = true OR "event:/phase" = null'})["results"],
            ["E-2", "E-3"],
        )
        self.assertEqual(query(snapshot, {"filter": 'NOT ("event:/flag" = true)'})["results"], ["E-1", "E-3"])
        for expression in ('"event:flag" = 1', '"event:a.b" = "literal"', '"event:/bad~2key" = 1', '"event:/flag" = __import__("os")'):
            outcome = query(snapshot, {"filter": expression})
            self.assertEqual(outcome["status"], "invalid")
            self.assertEqual(outcome["results"], [])
        self.assertEqual(path.read_bytes(), before)

    def test_e576_default_selected_and_full_fetches(self):
        self.write_events("events.ndjson", {"event_id": "E-1", "name": "one", "nullable": None})
        snapshot = capture_snapshot(self.root)
        self.assertEqual(query(snapshot, {})["results"], ["E-1"])
        selected = query(snapshot, {"mode": "fields", "select": ["event:/nullable", "event:/missing", "event:/name"]})
        self.assertEqual(list(selected["results"][0]), ["event_id", "event:/nullable", "event:/missing", "event:/name"])
        self.assertIsNone(selected["results"][0]["event:/nullable"])
        self.assertEqual(selected["results"][0]["event:/missing"], {"state": "missing"})
        full = query(snapshot, {"mode": "full_events"})
        self.assertEqual(full["results"][0]["event"]["name"], "one")

    def test_e577_pagination_cursor_context_and_frontier_failures(self):
        path = self.write_events("events.ndjson", {"event_id": "E-3"}, {"event_id": "E-1"}, {"event_id": "E-2"})
        snapshot = capture_snapshot(self.root)
        first = query(snapshot, {"limit": 1})
        self.assertEqual(first["results"], ["E-1"])
        second = query(snapshot, {"limit": 1, "cursor": first["next_cursor"]})
        self.assertEqual(second["results"], ["E-2"])
        invalid = query(snapshot, {"limit": 2, "cursor": first["next_cursor"]})
        self.assertEqual(invalid["status"], "invalid")
        path.write_bytes(path.read_bytes().replace(b"E-3", b"X-3"))
        changed = query(snapshot, {"limit": 1, "cursor": first["next_cursor"]})
        self.assertEqual(changed["status"], "blocked")
        self.assertEqual(changed["findings"][0]["code"], "changed-member")
        path.write_bytes(b'{"event_id":"E-3"}\n{"event_id":"E-1"}\n{"event_id":"E-2"}\n')
        (self.journal / "later.ndjson").write_bytes(b'{"event_id":"E-later"}\n')
        self.assertEqual(query(snapshot, {})["results"], ["E-1", "E-2"])
        fresh = capture_snapshot(self.root)
        path.write_bytes(path.read_bytes()[:5])
        self.assertEqual(query(fresh, {})["findings"][0]["code"], "truncated-member")
        path.write_bytes(b'{"event_id":"E-3"}\n{"event_id":"E-1"}\n{"event_id":"E-2"}\n')
        fresh = capture_snapshot(self.root)
        path.unlink()
        self.assertEqual(query(fresh, {})["findings"][0]["code"], "deleted-member")

    def test_e578_presealed_snapshot_allows_append_and_excludes_later_and_own_events(self):
        path = self.write_events("events.ndjson", {"event_id": "E-before"})
        before = hashlib.sha256(path.read_bytes()).hexdigest()
        snapshot = capture_snapshot(self.root)
        path.write_bytes(path.read_bytes() + b'{"event_id":"E-after"}\n')
        result = query(snapshot, {})
        self.assertEqual(result["status"], "complete")
        self.assertEqual(result["results"], ["E-before"])
        self.assertEqual(result["snapshot"]["prefix_digest"], before)
        self.assertEqual(result["snapshot"]["event_ids"], ["E-before"])

    def test_e579_secret_and_mutation_boundaries_do_not_leak_or_change_bytes(self):
        path = self.write_events("events.ndjson", {"event_id": "E-1", "details": {"api_key": "never-return"}})
        snapshot = capture_snapshot(self.root)
        before = path.read_bytes()
        for request in (
            {"select": ["event:/details/api_key"]},
            {"select": ["event:/details"]},
            {"mode": "full_events"},
            {"mutation": "delete"},
            {"filter": '"event:/details" = {"api_key":"never-return"}'},
        ):
            outcome = query(snapshot, request)
            self.assertEqual(outcome["status"], "invalid")
            self.assertNotIn("never-return", json.dumps(outcome))
        self.assertEqual(path.read_bytes(), before)

    def test_e580_query_does_not_create_a_run_or_its_own_event(self):
        path = self.write_events("events.ndjson", {"event_id": "E-before"})
        snapshot = capture_snapshot(self.root)
        before = path.read_bytes()
        result = query(snapshot, {})
        self.assertEqual(result["results"], ["E-before"])
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(result["snapshot"]["event_ids"], ["E-before"])

    def test_caller_rehashed_snapshot_cannot_inject_records_or_retarget_root(self):
        snapshot = capture_snapshot(self.root)
        forged = dict(snapshot)
        self.assertEqual(
            set(snapshot),
            {"snapshot_handle", "id", "source_root", "prefix_bytes", "prefix_digest", "event_ids"},
        )
        self.assertNotIn("records", snapshot)
        self.assertNotIn("members", snapshot)
        self.assertNotIn("limits", snapshot)
        forged["source_root"] = "."
        outcome = query(forged, {})
        self.assertEqual(outcome["status"], "invalid")
        self.assertNotIn("INJECTED", outcome["results"])
        forged = {**snapshot, "members": [], "records": [{"event_id": "INJECTED"}]}
        self.assertEqual(query(forged, {})["status"], "invalid")
        unknown = dict(snapshot)
        unknown["snapshot_handle"] = "not-a-retained-server-handle"
        self.assertEqual(query(unknown, {})["findings"][0]["code"], "unknown-snapshot")

    def test_current_configured_canonical_journal_boundary_is_rechecked(self):
        self.write_events("events.ndjson", {"event_id": "E-1"})
        snapshot = capture_snapshot(self.root)
        other = self.root / ".caprmedio_other"
        (other / "_journal").mkdir(parents=True)
        defaults = other / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        defaults.mkdir(parents=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_text(
            (self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_other\"\n", encoding="utf-8"
        )
        outcome = query(snapshot, {})
        self.assertEqual(outcome["status"], "blocked")
        self.assertEqual(outcome["findings"][0]["code"], "changed-source")

    def test_malformed_missing_id_unreadable_and_secret_sentinel_are_bounded(self):
        path = self.write_events("events.ndjson", {"event_id": "E-1"})
        path.write_bytes(b"not-json\n")
        with self.assertRaisesRegex(JournalQueryError, "malformed-event"):
            capture_snapshot(self.root)
        path.write_bytes(b'{"name":"no-id"}\n')
        with self.assertRaisesRegex(JournalQueryError, "missing-event-id"):
            capture_snapshot(self.root)
        path.write_bytes(b'{"event_id":"E-1"}\n')
        with patch.object(Path, "read_bytes", side_effect=PermissionError):
            with self.assertRaisesRegex(JournalQueryError, "unreadable-member"):
                capture_snapshot(self.root)
        sentinel = self.journal / "credentials.json"
        sentinel.write_text('{"api_key":"do-not-open"}', encoding="utf-8")
        reads = []
        original = Path.read_bytes

        def guarded_read(candidate):
            if candidate == sentinel:
                reads.append(candidate)
                raise AssertionError("secret sentinel must not be read")
            return original(candidate)

        with patch.object(Path, "read_bytes", guarded_read):
            snapshot = capture_snapshot(self.root)
            self.assertEqual(query(snapshot, {})["results"], ["E-1"])
        self.assertEqual(reads, [])

    def test_all_configured_query_bounds_are_enforced_without_code_defaults(self):
        self.write_events("one.ndjson", {"event_id": "E-1", "value": 1})
        self.write_events("two.ndjson", {"event_id": "E-2", "value": 2})
        with self.assertRaisesRegex(JournalQueryError, "snapshot-member-limit-exceeded"):
            capture_snapshot(self.root, limits={"max_snapshot_members": 1})
        (self.journal / "two.ndjson").unlink()
        with self.assertRaisesRegex(JournalQueryError, "file-limit-exceeded"):
            capture_snapshot(self.root, limits={"max_file_bytes": 1})
        with self.assertRaisesRegex(JournalQueryError, "total-read-limit-exceeded"):
            capture_snapshot(self.root, limits={"max_total_read_bytes": 1})
        with patch("find_and_fetch_journal_events.time.monotonic", side_effect=(0, 2)):
            with self.assertRaisesRegex(JournalQueryError, "timeout-exceeded"):
                capture_snapshot(self.root, limits={"timeout_seconds": 1})
        snapshot = capture_snapshot(self.root)
        cases = (
            ({"limits": {"max_request_bytes": 1}}, "request-limit-exceeded", "max_request_bytes", 1, "invalid"),
            ({"filter": 'NOT NOT "event:/value" = 1', "limits": {"max_grammar_depth": 1}}, "grammar-depth-limit-exceeded", "max_grammar_depth", 2, "incomplete"),
            ({"filter": '"event:/value" = 1', "limits": {"max_filter_tokens": 1}}, "filter-token-limit-exceeded", "max_filter_tokens", 2, "incomplete"),
            ({"filter": '"event:/value" IN (1, 2)', "limits": {"max_in_members": 1}}, "in-members-limit-exceeded", "max_in_members", 2, "incomplete"),
            ({"mode": "fields", "select": ["event:/value", "event:/missing"], "limits": {"max_selected_fields": 1}}, "selected-fields-limit-exceeded", "max_selected_fields", 2, "invalid"),
            ({"limit": 2, "limits": {"max_page_size": 1}}, "page-limit-exceeded", "max_page_size", 2, "invalid"),
        )
        for request, code, limit_name, minimum_consumed, status in cases:
            with self.subTest(code=code):
                outcome = query(snapshot, request)
                self.assertEqual(outcome["findings"][0]["code"], code)
                self.assertEqual(outcome["status"], status)
                self.assertEqual(
                    outcome["coverage"], {"scanned": 0, "matched": 0, "returned": 0, "complete": False},
                )
                self.assertEqual(outcome["results"], [])
                self.assertTrue(all("configured" in value and "consumed" in value for value in outcome["limits"].values()))
                self.assertGreaterEqual(outcome["limits"][limit_name]["consumed"], minimum_consumed)
                self.assertTrue(outcome["limits"][limit_name]["exhausted"])

    def test_parser_consumption_is_the_shared_parser_observation(self):
        self.write_events("events.ndjson", {"event_id": "E-1", "value": [[1], [2]]})
        snapshot = capture_snapshot(self.root)
        expression = 'NOT ("event:/value" IN ([[0]], [[1], [2]]))'
        _, expected = parse_filter_with_stats(
            expression,
            max_depth=16,
            max_tokens=128,
            max_in_members=16,
        )
        outcome = query(snapshot, {"filter": expression})
        self.assertEqual(outcome["status"], "complete")
        self.assertEqual(outcome["limits"]["max_filter_tokens"]["consumed"], expected["tokens"])
        self.assertEqual(outcome["limits"]["max_grammar_depth"]["consumed"], expected["grammar_depth"])
        self.assertEqual(outcome["limits"]["max_in_members"]["consumed"], expected["in_members"])
        with self.assertRaises(QueryFilterError) as rejected:
            parse_filter_with_stats(
                expression,
                max_depth=1,
                max_tokens=128,
                max_in_members=16,
            )
        rejected_statistics = rejected.exception.statistics
        bounded = query(snapshot, {"filter": expression, "limits": {"max_grammar_depth": 1}})
        self.assertEqual(bounded["findings"][0]["code"], "grammar-depth-limit-exceeded")
        self.assertEqual(
            bounded["limits"]["max_grammar_depth"]["consumed"],
            rejected_statistics["grammar_depth"],
        )

    def test_rejected_selector_admission_retains_successful_parser_consumption(self):
        self.write_events("events.ndjson", {"event_id": "E-1", "details": {"api_key": "do-not-leak"}, "api.key": "do-not-leak"})
        snapshot = capture_snapshot(self.root)
        cases = (
            ('"event:bad" = 1', "invalid-event-selector"),
            ('"event:/details" = {}', "protected-selector"),
            ('"event:/api.key" = "do-not-leak"', "protected-selector"),
        )
        for expression, code in cases:
            with self.subTest(code=code):
                _, statistics = parse_filter_with_stats(
                    expression,
                    max_depth=16,
                    max_tokens=128,
                    max_in_members=16,
                )
                outcome = query(snapshot, {"filter": expression})
                self.assertEqual(outcome["findings"][0]["code"], code)
                self.assertEqual(outcome["limits"]["max_filter_tokens"]["consumed"], statistics["tokens"])
                self.assertEqual(outcome["limits"]["max_grammar_depth"]["consumed"], statistics["grammar_depth"])
                self.assertEqual(outcome["limits"]["max_in_members"]["consumed"], statistics["in_members"])
        fetched = query(snapshot, {"mode": "fields", "select": ["event:/api.key"]})
        self.assertEqual(fetched["findings"][0]["code"], "protected-selector")

    def test_limit_provenance_survives_snapshot_and_request_override(self):
        self.write_events("events.ndjson", {"event_id": "E-1"})
        instance = self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION"
        instance.mkdir(parents=True)
        (instance / "caprmedio_framework_settings.toml").write_text(
            "[query]\nmax_page_size = 1\n", encoding="utf-8"
        )
        snapshot = capture_snapshot(self.root)
        captured = query(snapshot, {})
        self.assertEqual(captured["limits"]["max_page_size"], {"configured": 1, "source": "instance", "consumed": 1, "exhausted": False})
        overridden = query(snapshot, {"limits": {"max_page_size": 2}})
        self.assertEqual(overridden["limits"]["max_page_size"]["configured"], 2)
        self.assertEqual(overridden["limits"]["max_page_size"]["source"], "request")

    def test_malformed_duplicate_ids_duplicate_keys_and_limits_fail_closed(self):
        self.write_events("duplicate-keys.ndjson", {"event_id": "E-1"})
        (self.journal / "duplicate-keys.ndjson").write_bytes(b'{"event_id":"E-1","event_id":"E-2"}\n')
        with self.assertRaisesRegex(JournalQueryError, "duplicate-json-key"):
            capture_snapshot(self.root)
        (self.journal / "duplicate-keys.ndjson").unlink()
        self.write_events("one.ndjson", {"event_id": "E-1"})
        self.write_events("two.ndjson", {"event_id": "E-1"})
        with self.assertRaisesRegex(JournalQueryError, "duplicate-event-id"):
            capture_snapshot(self.root)
        (self.journal / "two.ndjson").unlink()
        snapshot = capture_snapshot(self.root)
        outcome = query(snapshot, {"limit": 3})
        self.assertEqual(outcome["status"], "invalid")
        self.assertEqual(outcome["findings"][0]["code"], "page-limit-exceeded")
        self.assertIn("max_page_size", outcome["limits"])


if __name__ == "__main__":
    unittest.main()
