import unittest
from q2 import make_wave


def expected_wave(n, h):
    """Helper to build the expected wave string for comparison, matching README examples."""
    if h <= 0 or n <= 0:
        return ""
    one_cycle = []
    # Ascend 1..n
    for i in range(1, n + 1):
        one_cycle.append("  " * (i - 1) + str(i))
    # Descend n-1..2 (exclude 1 to avoid double '1' across cycles)
    for i in range(n - 1, 1, -1):
        one_cycle.append("  " * (i - 1) + str(i))

    # Special case: n == 1 -> cycle is just ["1"]
    if not one_cycle:
        one_cycle = ["1"]

    # Repeat to length h
    lines = []
    idx = 0
    while len(lines) < h:
        lines.append(one_cycle[idx])
        idx = (idx + 1) % len(one_cycle)
    return "\n".join(lines)


class TestMakeWave(unittest.TestCase):
    def test_example_n4_h9(self):
        expected = (
            "1\n"
            "  2\n"
            "    3\n"
            "      4\n"
            "    3\n"
            "  2\n"
            "1\n"
            "  2\n"
            "    3"
        )
        self.assertEqual(make_wave(4, 9), expected, "Should match the provided example for n=4, h=9")

    def test_example_n3_h7(self):
        expected = (
            "1\n"
            "  2\n"
            "    3\n"
            "  2\n"
            "1\n"
            "  2\n"
            "    3"
        )
        self.assertEqual(make_wave(3, 7), expected, "Should match the provided example for n=3, h=7")

    def test_zero_height(self):
        self.assertEqual(make_wave(5, 0), "", "h=0 should produce empty string")

    def test_n_equals_1(self):
        # For n=1, the cycle is just "1" repeated
        self.assertEqual(make_wave(1, 5), "1\n1\n1\n1\n1", "n=1 should repeat '1' h times without trailing newline")

    def test_repeats_cleanly(self):
        # Check a multi-cycle repeat with precise formatting
        n, h = 4, 12
        self.assertEqual(make_wave(n, h), expected_wave(n, h), "Repeated pattern should be correct for multiple cycles")

    def test_no_trailing_newline(self):
        out = make_wave(2, 3)
        self.assertFalse(out.endswith("\n"), "Output should not end with a trailing newline")
        self.assertEqual(out, "1\n  2\n1", "Exact formatting for n=2, h=3 should match")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeWave)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
