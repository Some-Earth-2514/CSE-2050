import unittest
from hw3 import find_pairs_naive, find_pairs_optimized, measure_min_time


class TestHw3(unittest.TestCase):
    """Test cases for finding pairs"""

    def test_find_pairs_naive(self):
        """Testing find_pairs_naive(): creating lists and target value with their expected output list"""
        self.assertEqual(find_pairs_naive([3, 4, 5], 0), set())  # list with target 0
        self.assertEqual(find_pairs_naive([1, 2, 3, 4, 5], 10), set())  # target is too big so return empty list
        self.assertEqual(find_pairs_naive([1, 2, 3, 4, 5], 6), {(1, 5), (2, 4)})  #
        self.assertNotEqual(find_pairs_naive([1, 2, 3, 4, 5], 6), {(1, 2), (3, 4)})  #

    def test_find_pairs_optimized(self):
        """Testing find_pairs_optimized(): creating lists and target value with their expected output list"""
        self.assertEqual(find_pairs_optimized([1, 2, 3, 4, 5], 0), set())  # list with target 0-
        self.assertEqual(find_pairs_optimized([1, 2, 3, 4, 5], 10), set())  # target is too big so return empty list
        self.assertEqual(find_pairs_optimized([1, 2, 3, 4, 5], 6), {(1, 5), (2, 4)})  #
        self.assertNotEqual(find_pairs_optimized([1, 2, 3, 4, 5], 6), {(1, 2), (3, 4)})  #

    if __name__ == "__main__":
        unittest.main()
