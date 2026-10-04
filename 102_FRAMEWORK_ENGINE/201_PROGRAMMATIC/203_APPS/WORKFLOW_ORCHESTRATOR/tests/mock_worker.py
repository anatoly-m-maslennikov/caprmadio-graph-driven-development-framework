"""Test-only worker; never launch a real model."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend import worker
from test_orchestrator import MockAgent

if __name__ == '__main__':
    worker(sys.argv[1], agent=MockAgent(issues=True), ready_file=sys.argv[2])
