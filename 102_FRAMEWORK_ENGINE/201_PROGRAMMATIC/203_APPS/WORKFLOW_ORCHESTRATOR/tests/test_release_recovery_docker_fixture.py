import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


TESTS = Path(__file__).resolve().parent
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from release_recovery_docker_fixture import (  # noqa: E402
    ReleaseRecoveryDockerFixture,
    ReleaseRecoveryFixtureError,
)


class ReleaseRecoveryDockerFixtureEnvironmentTest(unittest.TestCase):
    def fixture(self, name: str = "one") -> ReleaseRecoveryDockerFixture:
        return ReleaseRecoveryDockerFixture(
            root=Path(f"/private/release-recovery-{name}"),
            interpreter=Path("/private/interpreter"),
            fault_import_root=Path(f"/private/release-recovery-{name}/fault-import"),
            candidate=None,
        )

    def test_false_and_none_clear_an_inherited_fault_environment(self) -> None:
        fixture = self.fixture()
        inherited = {
            "CAPRMEDIO_TEST_RELEASE_RECORDING_FAULT": "effect-action-once",
            "CAPRMEDIO_TEST_RELEASE_FAULT_ROOT": "/private/inherited-fault-root",
        }
        with patch.dict(os.environ, inherited, clear=True):
            for fault in (False, None):
                with self.subTest(fault=fault):
                    environment = fixture.environment(fault=fault)
                    self.assertNotIn("CAPRMEDIO_TEST_RELEASE_RECORDING_FAULT", environment)
                    self.assertNotIn("CAPRMEDIO_TEST_RELEASE_FAULT_ROOT", environment)

    def test_true_maps_to_the_existing_post_effect_fault(self) -> None:
        fixture = self.fixture()
        environment = fixture.environment(fault=True)
        self.assertEqual(environment["CAPRMEDIO_TEST_RELEASE_RECORDING_FAULT"], "effect-action-once")
        self.assertEqual(
            environment["CAPRMEDIO_TEST_RELEASE_FAULT_ROOT"],
            str(fixture.fault_import_root),
        )

    def test_barrier_faults_use_each_fixture_private_fault_path(self) -> None:
        for fault in ("before-effect-admission-block", "durable-in-progress-block"):
            with self.subTest(fault=fault):
                fixture = self.fixture(fault)
                environment = fixture.environment(fault=fault)
                self.assertEqual(environment["CAPRMEDIO_TEST_RELEASE_RECORDING_FAULT"], fault)
                self.assertEqual(
                    environment["CAPRMEDIO_TEST_RELEASE_FAULT_ROOT"],
                    str(fixture.fault_import_root),
                )

    def test_unknown_literal_fault_is_refused(self) -> None:
        with self.assertRaisesRegex(ReleaseRecoveryFixtureError, "unsupported fixture fault: unknown-fault"):
            self.fixture().environment(fault="unknown-fault")


if __name__ == "__main__":
    unittest.main()
