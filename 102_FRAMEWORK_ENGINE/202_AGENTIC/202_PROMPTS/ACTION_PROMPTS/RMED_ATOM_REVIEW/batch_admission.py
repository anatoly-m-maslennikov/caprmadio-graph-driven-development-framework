"""Admit a caller-selected batch only from current raw contract evaluations.

This is intentionally an aggregation boundary, not another evaluator.  It
does not infer missing checks, turn a preliminary summary into evidence, or
authorize a source repair.  Callers retain responsibility for selecting the
candidate bindings and for any later governed mutation.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
from typing import Any, Mapping, Sequence

from evaluation_contract import GROUPS, ReviewContext, merge_evaluations, summarize_evaluations


def _rejected(reason: str) -> dict[str, Any]:
    """Return a machine-readable rejection instead of disguising it as blocked."""
    return {
        "admission": "rejected",
        "reasons": [reason],
        "evaluations": [],
        "summary": None,
        "source_repair_authorized": False,
    }


def _candidate_paths(candidates: Sequence[dict[str, Any]]) -> list[str]:
    if not isinstance(candidates, Sequence) or isinstance(candidates, (str, bytes)) or not candidates:
        raise ValueError("candidate bindings must be a nonempty ordered sequence")
    paths: list[str] = []
    for binding in candidates:
        if not isinstance(binding, dict) or not isinstance(binding.get("path"), str) or not binding["path"]:
            raise ValueError("candidate binding needs a path")
        paths.append(binding["path"])
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate candidate binding path")
    return paths


def _context_for(contexts: ReviewContext | Mapping[str, ReviewContext], path: str) -> ReviewContext:
    context = contexts if isinstance(contexts, ReviewContext) else (contexts.get(path)
              if isinstance(contexts, Mapping) else None)
    if not isinstance(context, ReviewContext):
        raise ValueError(f"missing caller ReviewContext for candidate: {path}")
    return context


def _validate_current_sources(candidates: Sequence[dict[str, Any]],
                              contexts: ReviewContext | Mapping[str, ReviewContext],
                              current_source_texts: Mapping[str, str] | None) -> None:
    """Compare caller-supplied current bytes with the frozen selected bindings.

    Omitting this optional input does not pretend to prove filesystem
    freshness.  Supplying it makes every named source a strict verification
    input; it cannot be a casual unrelated file list.
    """
    if current_source_texts is None:
        return
    if not isinstance(current_source_texts, Mapping):
        raise ValueError("current_source_texts must map candidate paths to bytes")
    candidate_by_path = {binding["path"]: binding for binding in candidates}
    if set(current_source_texts) != set(candidate_by_path):
        raise ValueError("current source bytes must cover exactly every selected candidate")
    for path, current in current_source_texts.items():
        if not isinstance(current, str):
            raise ValueError("current source bytes must be text")
        binding = candidate_by_path[path]
        if hashlib.sha256(current.encode()).hexdigest() != binding.get("sha256"):
            raise ValueError("current source bytes do not match the selected source binding")
        if _context_for(contexts, path).candidate_text(binding) != current:
            raise ValueError("current source bytes do not match the caller context")


def _validate_prompt_bindings(parts_by_path: Mapping[str, Sequence[dict[str, Any]]], *,
                              prompt_bindings: Mapping[str, Mapping[str, str]] | None,
                              prompt_texts: Mapping[str, str] | None) -> None:
    """Optionally bind raw reports to caller-provided evaluator prompt bytes."""
    if prompt_bindings is None and prompt_texts is None:
        return
    if not isinstance(prompt_bindings, Mapping) or not isinstance(prompt_texts, Mapping):
        raise ValueError("prompt bindings and prompt texts must be supplied together")
    if set(prompt_bindings) != set(GROUPS):
        raise ValueError("prompt bindings must cover every evaluator exactly once")
    expected: dict[str, str] = {}
    for evaluator, binding in prompt_bindings.items():
        if not isinstance(binding, Mapping) or not isinstance(binding.get("path"), str):
            raise ValueError("prompt binding needs a path")
        digest = binding.get("sha256")
        prompt = prompt_texts.get(evaluator, prompt_texts.get(binding["path"]))
        if (not isinstance(digest, str) or len(digest) != 64
                or not isinstance(prompt, str)
                or hashlib.sha256(prompt.encode()).hexdigest() != digest):
            raise ValueError("caller prompt bytes do not match the prompt binding")
        expected[evaluator] = digest
    for parts in parts_by_path.values():
        for part in parts:
            evaluator = part.get("evaluator") if isinstance(part, dict) else None
            if evaluator not in expected or part.get("prompt_sha256") != expected[evaluator]:
                raise ValueError("raw report is missing or stale for the caller prompt binding")


def _combine_summaries(summaries: Sequence[dict[str, Any]]) -> dict[str, Any]:
    if not summaries:
        raise ValueError("batch summaries must be nonempty")
    # Each summary has already been validated under its caller's contract.
    # Preserve that profile instead of adding excluded legacy checks to a
    # local review, and never combine different coverage promises.
    profile = summaries[0].get("review_profile")
    checks = list(summaries[0]["check_counts"])
    if any(summary.get("review_profile") != profile
           or set(summary["check_counts"]) != set(checks) for summary in summaries):
        raise ValueError("batch summaries must use the same review profile and checks")
    combined: dict[str, Any] = {
        "atoms": 0,
        "fully_passed_atoms": 0,
        "atoms_with_confirmed_findings": 0,
        "atoms_with_coverage_gaps": 0,
        "check_counts": {check: {"passed": 0, "failed": 0, "blocked": 0,
                                  "atoms_with_findings": 0, "findings": 0}
                         for check in checks},
    }
    if profile is not None:
        combined["review_profile"] = profile
    for summary in summaries:
        for key in ("atoms", "fully_passed_atoms", "atoms_with_confirmed_findings",
                    "atoms_with_coverage_gaps"):
            combined[key] += summary[key]
        for check in checks:
            for key in combined["check_counts"][check]:
                combined["check_counts"][check][key] += summary["check_counts"][check][key]
    return combined


def admit_batch(candidates: Sequence[dict[str, Any]],
                raw_parts_by_candidate: Mapping[str, Sequence[dict[str, Any]]],
                contexts: ReviewContext | Mapping[str, ReviewContext], *,
                current_source_texts: Mapping[str, str] | None = None,
                prompt_bindings: Mapping[str, Mapping[str, str]] | None = None,
                prompt_texts: Mapping[str, str] | None = None,
                claimed_summary: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Validate and aggregate exact raw parts for exactly the selected candidates.

    ``raw_parts_by_candidate`` is deliberately keyed by selected source path,
    and each value must be the three raw evaluator records.  A merged report,
    a fresh-review template, or an aggregate summary has no place at this
    boundary.  The return value distinguishes invalid input (``rejected``)
    from valid complete evidence that reports ``failed`` or ``blocked``.
    """
    try:
        paths = _candidate_paths(candidates)
        if not isinstance(raw_parts_by_candidate, Mapping):
            raise ValueError("raw parts must map every candidate path to raw evaluator reports")
        actual_paths = set(raw_parts_by_candidate)
        expected_paths = set(paths)
        missing, extra = expected_paths - actual_paths, actual_paths - expected_paths
        if missing:
            raise ValueError("missing candidates in raw parts: " + ", ".join(sorted(missing)))
        if extra:
            raise ValueError("extra candidates in raw parts: " + ", ".join(sorted(extra)))
        _validate_current_sources(candidates, contexts, current_source_texts)
        _validate_prompt_bindings(raw_parts_by_candidate, prompt_bindings=prompt_bindings,
                                  prompt_texts=prompt_texts)

        merged_records: list[tuple[ReviewContext, dict[str, Any]]] = []
        for binding in candidates:
            path = binding["path"]
            context = _context_for(contexts, path)
            # candidate_text proves this exact caller selection occurs in its
            # supplied context before the existing contract reads raw parts.
            context.candidate_text(binding)
            parts = raw_parts_by_candidate[path]
            if not isinstance(parts, Sequence) or isinstance(parts, (str, bytes)):
                raise ValueError("candidate raw parts must be an ordered sequence")
            merged = merge_evaluations(list(parts), context=context)
            if merged["source"] != binding:
                raise ValueError("raw report bundle source does not match its selected candidate")
            merged_records.append((context, merged))

        grouped: dict[int, tuple[ReviewContext, list[dict[str, Any]]]] = {}
        for context, merged in merged_records:
            key = id(context)
            grouped.setdefault(key, (context, []))[1].append(merged)
        per_context = [summarize_evaluations(records, context=context)
                       for context, records in grouped.values()]
        summary = _combine_summaries(per_context)
        if claimed_summary is not None and dict(claimed_summary) != summary:
            raise ValueError("caller summary contradicts the validated raw reports")

        results = [record["result"] for _, record in merged_records]
        admission = "failed" if "failed" in results else "blocked" if "blocked" in results else "accepted"
        return {
            "admission": admission,
            "reasons": [],
            "evaluations": [deepcopy(record) for _, record in merged_records],
            "summary": summary,
            # This module is evidence admission only.  A later governed action
            # must obtain its own Journal/change-set authorization.
            "source_repair_authorized": False,
        }
    except (AttributeError, TypeError, ValueError, KeyError) as error:
        return _rejected(str(error))
