import unittest


class RepeatedCaseTests(unittest.TestCase):
    def test_repeated_case(self):
        self.assertTrue(True)


def load_tests(loader, tests, pattern):
    case = RepeatedCaseTests("test_repeated_case")
    return unittest.TestSuite((case, case))
