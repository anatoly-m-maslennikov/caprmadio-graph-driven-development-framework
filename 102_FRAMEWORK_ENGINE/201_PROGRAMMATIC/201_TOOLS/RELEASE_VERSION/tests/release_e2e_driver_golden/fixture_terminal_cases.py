import unittest


class TerminalCases(unittest.TestCase):
    def test_error(self):
        raise RuntimeError("fixture error")

    def test_failure(self):
        self.fail("fixture failure")

    @unittest.skip("fixture skip")
    def test_skip(self):
        pass

    def test_success(self):
        self.assertTrue(True)
