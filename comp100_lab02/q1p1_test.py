import unittest
from q1p1 import find_next_prime_factor


class TestNextPrimeFactor(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_next_prime_factor(15, 2), 3, "Should be 3")

    def test_2(self):
        self.assertEqual(find_next_prime_factor(15, 4), 5, "Should be 5")

    def test_3(self):
        self.assertEqual(find_next_prime_factor(15, 6), 15, "Should be 15")

    def test_4(self):
        self.assertEqual(find_next_prime_factor(17, 2), 17, "Should be 17 as 17 is prime")

    def test_5(self):
        self.assertEqual(find_next_prime_factor(14, 3), 7, "Should be 7")

    def test_6(self):
        self.assertEqual(find_next_prime_factor(16, 2), 2, "Should be 2")

    def test_7(self):
        self.assertEqual(find_next_prime_factor(16, 3), 16, "Should be 16")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNextPrimeFactor)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
