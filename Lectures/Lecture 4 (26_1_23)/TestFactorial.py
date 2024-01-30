import unittest
from factorial import factorial, sum_k


class TestFactorial(unittest.TestCase):
    def test_expected_inputs(self):
        self.assertEqual(factorial(5), 120)


class TestSumk(unittest.TestCase):
    def test_expected_inputs(self):
        self.assertEqual(sum_k(4), 5)


unittest.main(verbosity=2)
