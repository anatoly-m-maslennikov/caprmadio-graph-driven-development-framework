"""Deterministic scheduling regressions; fixtures do not simulate LLM judgment."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from continuation import checkpoint_sha256, next_action, progress_sha256


def pin(path, text="bytes"):
    return {"path": path, "sha256": hashlib.sha256(text.encode()).hexdigest()}


def source(ordinal, text="initial"):
    return dict(pin(f"atoms/{ordinal}.md", text), atom_id=f"CA-R-{ordinal}", version=1)


def checkpoint(count=2):
    return {
        "schema_version": 1, "request_id": "original-request",
        "selection": [{"ordinal": n, "source": source(n)} for n in range(1, count + 1)],
        "items": [{"ordinal": n, "stage": "queued", "source": source(n),
                   "bindings": {"authority": [pin("rule.md")],
                                "settings": [pin("settings.toml")],
                                "prompts": [pin("review.prompt.md")]},
                   "evidence": [], "completed_effects": [],
                   "retries_used": 0, "retry_limit": 2}
                  for n in range(1, count + 1)],
        "resume_ordinal": None, "handoffs": [],
        "max_handoffs_without_progress": 2, "blocker": None,
    }


def route(state, slots=1, active=()):
    return next_action(state, durable_sha256=checkpoint_sha256(state),
                       available_slots=slots, active_ordinals=active)


def acknowledge(result, slots=1):
    # Simulate the caller's acknowledged canonical JSON, not filesystem durability.
    state = json.loads(json.dumps(result["checkpoint"]))
    return next_action(state, durable_sha256=result["checkpoint_sha256"],
                       available_slots=slots)


def verify(item):
    # Trusted caller fixture only: the router must still request real closure gates.
    item.update(stage="verified", evidence=[pin(f"reports/{item['ordinal']}.json")])


class ContinuationTests(unittest.TestCase):
    def test_checkpoint_is_required_before_first_spawn(self):
        state = checkpoint()
        result = next_action(state, available_slots=1)
        self.assertEqual(result["action"], "checkpoint_required")
        self.assertEqual(result["checkpoint"], state)
        spawned = acknowledge(result)
        self.assertEqual((spawned["action"], spawned["ordinal"], spawned["stage"]),
                         ("spawn_subagent", 1, "review"))
        self.assertEqual(spawned["model"], "gpt-5.6-terra")
        self.assertEqual(spawned["reasoning_effort"], "high")
        self.assertTrue(spawned["fresh_context"])

    def test_changed_checkpoint_must_be_repersisted(self):
        state = checkpoint()
        old_digest = checkpoint_sha256(state)
        state["items"][0]["evidence"].append(pin("partial.json"))
        self.assertEqual(next_action(state, available_slots=1,
                                    durable_sha256=old_digest)["action"], "checkpoint_required")

    def test_context_capacity_resumes_exact_pending_stage_automatically(self):
        for stage in ("review", "propose_repair", "verify_proposal", "verify_saved"):
            state = checkpoint()
            state["items"][1].update(stage=stage, evidence=[pin("partial.json")])
            state["resume_ordinal"] = 2
            state["blocker"] = {"kind": "context_capacity", "reason": "worker headroom reached"}
            before = deepcopy(state)
            result = route(state)
            with self.subTest(stage=stage):
                self.assertEqual(result["action"], "checkpoint_required")
                self.assertIsNone(result["checkpoint"]["blocker"])
                self.assertEqual(result["checkpoint"]["continuation_reason"], state["blocker"])
                spawned = acknowledge(result)
                self.assertEqual((spawned["action"], spawned["ordinal"], spawned["stage"]),
                                 ("spawn_subagent", 2, stage))
                self.assertEqual(state, before)
                self.assertEqual(result["checkpoint"]["items"][1], before["items"][1])

    def test_capacity_handoff_without_exact_ordinal_fails_closed(self):
        state = checkpoint()
        state["blocker"] = {"kind": "context_capacity", "reason": "headroom reached"}
        self.assertEqual(route(state)["reason"]["kind"], "invalid_state")

    def test_full_concurrency_waits_then_automatically_dispatches(self):
        state = checkpoint()
        waiting = route(state, slots=0, active=(1,))
        self.assertEqual(waiting["action"], "wait_for_slot")
        self.assertEqual(waiting["pending_ordinals"], [1, 2])
        spawned = route(state, slots=1, active=(1,))
        self.assertEqual((spawned["action"], spawned["ordinal"]), ("spawn_subagent", 2))

    def test_active_atom_is_never_dispatched_again(self):
        state = checkpoint(1)
        state["resume_ordinal"] = 1
        self.assertEqual(route(state, slots=1, active=(1,))["action"], "wait_for_slot")

    def test_dispatch_identity_is_stable_for_caller_deduplication(self):
        state = checkpoint()
        self.assertEqual(route(state)["dispatch_id"], route(state)["dispatch_id"])

    def test_host_spawn_denial_is_durable_and_not_capacity_handoff(self):
        for kind in ("host_spawn_denied", "host_spawn_refused", "missing_permission"):
            state = checkpoint()
            state["blocker"] = {"kind": kind, "reason": "actual host response"}
            result = next_action(state, available_slots=4)
            with self.subTest(kind=kind):
                self.assertEqual(result["action"], "checkpoint_required")
                blocked = acknowledge(result, slots=4)
                self.assertEqual(blocked["action"], "blocked")
                self.assertEqual(blocked["reason"], state["blocker"])
                self.assertFalse(blocked["completion_verified"])

    def test_repeated_handoffs_without_progress_persist_blocker(self):
        state = checkpoint(1)
        for n in range(2):
            state["handoffs"].append({"ordinal": 1, "progress_sha256": progress_sha256(state["items"][0]),
                                      "dispatch_id": f"dispatch-{n}"})
        result = route(state)
        self.assertEqual(result["action"], "checkpoint_required")
        self.assertEqual(result["checkpoint"]["blocker"]["kind"], "no_progress")
        self.assertEqual(acknowledge(result)["action"], "blocked")

    def test_host_refusal_waits_for_active_workers_then_retries_after_observed_change(self):
        for kind in ("host_spawn_denied", "host_spawn_refused"):
            state = checkpoint()
            state["blocker"] = {"kind": kind, "reason": "agent thread limit reached"}
            with self.subTest(kind=kind):
                waiting = route(state, slots=0, active=(1,))
                self.assertEqual(waiting["action"], "wait_for_slot")
                self.assertEqual(waiting["reason"], state["blocker"])
                self.assertEqual(route(state)["action"], "blocked")
                # The caller records actual worker completion before clearing refusal.
                state["host_events"] = [{"kind": "worker_completed", "ordinal": 1,
                                         "previous_denial": deepcopy(state["blocker"])}]
                verify(state["items"][0])
                state["blocker"] = None
                required = next_action(state, available_slots=1)
                self.assertEqual(required["action"], "checkpoint_required")
                self.assertEqual(acknowledge(required)["ordinal"], 2)

    def test_retry_counts_are_neither_consumed_nor_counted_as_progress(self):
        state = checkpoint(1)
        progress = progress_sha256(state["items"][0])
        for n in range(2):
            state["handoffs"].append({"ordinal": 1, "progress_sha256": progress,
                                      "dispatch_id": f"dispatch-{n}"})
        state["items"][0]["retries_used"] = 1
        before = deepcopy(state)
        result = route(state)
        self.assertEqual(result["checkpoint"]["blocker"]["kind"], "no_progress")
        self.assertEqual(result["checkpoint"]["items"][0]["retries_used"], 1)
        self.assertEqual(state, before)

    def test_saved_progress_permits_successor_within_bound(self):
        state = checkpoint(1)
        state["handoffs"] = [{"ordinal": 1, "progress_sha256": progress_sha256(state["items"][0]),
                               "dispatch_id": f"dispatch-{n}"} for n in range(2)]
        state["items"][0]["evidence"] = [pin("new-partial-report.json")]
        self.assertEqual(route(state)["action"], "spawn_subagent")

    def test_already_applied_effect_routes_to_independent_verification(self):
        state = checkpoint(1)
        item = state["items"][0]
        item.update(stage="apply_repair", pending_effect_id="repair-1", source=source(1, "saved"))
        item["completed_effects"] = [{"effect_id": "repair-1", "before_source": source(1),
                                      "after_source": source(1, "saved"),
                                      "evidence": [pin("history/repair-1.json")]}]
        before = deepcopy(state)
        result = route(state)
        self.assertEqual(result["stage"], "verify_saved")
        self.assertTrue(result["independent"])
        self.assertFalse(result["source_mutation_authorized"])
        self.assertEqual(state, before)

    def test_unapplied_effect_preserves_exact_stage_and_retries(self):
        state = checkpoint(1)
        state["items"][0].update(stage="apply_repair", pending_effect_id="repair-1", retries_used=1)
        self.assertEqual(route(state)["stage"], "apply_repair")
        self.assertEqual(state["items"][0]["retries_used"], 1)

    def test_unreconciled_applied_effect_blocks_before_dispatch(self):
        state = checkpoint(1)
        item = state["items"][0]
        item.update(stage="apply_repair", pending_effect_id="repair-1")
        item["completed_effects"] = [{"effect_id": "repair-1", "before_source": source(1),
                                      "after_source": source(1, "different"),
                                      "evidence": [pin("history/repair-1.json")]}]
        result = route(state)
        self.assertEqual(result["checkpoint"]["blocker"]["kind"], "effect_reconciliation")
        self.assertEqual(acknowledge(result)["action"], "blocked")

    def test_deferred_member_survives_current_batch_completion(self):
        state = checkpoint()
        verify(state["items"][0])
        result = route(state)
        self.assertEqual((result["action"], result["ordinal"]), ("spawn_subagent", 2))
        self.assertEqual(state["items"][1]["stage"], "queued")

    def test_all_original_members_are_needed_before_closure_checks(self):
        state = checkpoint()
        for item in state["items"]:
            verify(item)
        result = route(state)
        self.assertEqual(result["action"], "validate_completion")
        self.assertEqual(result["ordinals"], [1, 2])
        self.assertFalse(result["completion_verified"])
        self.assertFalse(result["source_mutation_authorized"])

    def test_flags_and_empty_current_batch_do_not_prove_semantic_completion(self):
        state = checkpoint()
        state.update(completed=True, current_batch=[], verified=True)
        for item in state["items"]:
            item["verified"] = True
        self.assertEqual(route(state)["action"], "spawn_subagent")
        for item in state["items"]:
            verify(item)
        self.assertEqual(route(state)["action"], "validate_completion")
        self.assertFalse(route(state)["completion_verified"])

    def test_truly_empty_request_still_needs_caller_completion_check(self):
        self.assertEqual(route(checkpoint(0))["action"], "validate_completion")

    def test_incomplete_or_malformed_state_fails_closed(self):
        mutations = {
            "lost_deferred_member": lambda s: s["items"].pop(),
            "duplicate_member": lambda s: s["items"].append(deepcopy(s["items"][0])),
            "missing_rules": lambda s: s["items"][0]["bindings"].pop("authority"),
            "missing_prompts": lambda s: s["items"][0]["bindings"].pop("prompts"),
            "missing_source_identity": lambda s: s["items"][0]["source"].pop("atom_id"),
            "negative_retries": lambda s: s["items"][0].update(retries_used=-1),
            "retry_overflow": lambda s: s["items"][0].update(retries_used=3),
            "no_progress_bound_missing": lambda s: s.pop("max_handoffs_without_progress"),
            "missing_effect_identity": lambda s: s["items"][0].update(stage="apply_repair"),
            "verified_without_evidence": lambda s: s["items"][0].update(stage="verified"),
        }
        for name, mutate in mutations.items():
            state = checkpoint()
            mutate(state)
            with self.subTest(name=name):
                result = route(state)
                self.assertEqual(result["action"], "blocked")
                self.assertEqual(result["reason"]["kind"], "invalid_state")

    def test_default_prompts_preserve_bounded_handoff_without_recheck_loop(self):
        root = Path(__file__).resolve().parents[1]
        for name in ("CA-O-108", "CA-O-109", "CA-O-110"):
            text = (root / f"{name}.prompt.md").read_text()
            with self.subTest(name=name):
                self.assertLessEqual(len(text.split()), 300)
        self.assertIn("fixed_not_rechecked", (root / "CA-O-110.prompt.md").read_text())
        readme = " ".join((root / "README.md").read_text().split())
        for phrase in ("gather scope", "check selected", "fix confirmed", "progress list",
                       "no recheck loop", "same-stage handoff", "fresh agent"):
            self.assertIn(phrase, readme)


if __name__ == "__main__":
    unittest.main()
