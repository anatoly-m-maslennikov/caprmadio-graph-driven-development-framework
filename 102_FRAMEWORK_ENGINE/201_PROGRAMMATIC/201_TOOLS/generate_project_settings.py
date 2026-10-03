#!/usr/bin/env python3
"""Retired compatibility entry point for the former settings Projection.

Use the selected installed ``GENERATE_PROJECT_GRAPH_STATE`` Tool instead. It
generates the Project Scope Unit Graph and Sources Projections and never writes
the retired Project Settings outputs.
"""

from __future__ import annotations


def main() -> None:
    raise SystemExit(
        "generate_project_settings.py is retired; use the installed "
        "GENERATE_PROJECT_GRAPH_STATE Tool"
    )


if __name__ == "__main__":
    main()
