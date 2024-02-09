import unittest
from matplotlib._path import is_sorted
from MagicSort import linear_scan, reverse_list, insertion_sort, quicksort, mergesort, magic_sort


class Test_linear_scan(unittest.TestCase):
    def test_already_sorted(self):
        L = [1, 2, 3, 4, 5]
        self.assertEqual(linear_scan(L), "already sorted")

    def test_insertion_sort(self):
        L = [1, 3, 2, 4, 5]
        self.assertEqual(linear_scan(L), "insertion sort")

    def test_reverse_list(self):  # doesnt work - is supposed to be 'reverse list', but instead is 'insertion sort'
        L = [5, 4, 3, 2, 1]
        self.assertEqual(linear_scan(L), "reverse list")

    def test_quicksort(self):  # doesnt work - is supposed to be 'quicksort', but instead is 'insertion sort'
        L = [5, 4, 3, 2, 1, 0]
        self.assertEqual(linear_scan(L), "quicksort")


class Test_reverse_list(unittest.TestCase):
    def test_empty_list(self):
        L = []
        reverse_list(L)
        self.assertEqual(L, [])

    def test_single_item(self):
        L = [1]
        reverse_list(L)
        self.assertEqual(L, [1])

    def test_multiple_items(self):
        L = [1, 2, 3, 4, 5]
        reverse_list(L)
        self.assertEqual(L, [5, 4, 3, 2, 1])


class Test_insertionsort(unittest.TestCase):
    def test_empty_list(self):
        L = []
        insertion_sort(L, 0, -1)
        self.assertEqual(L, [])

    def test_single_item(self):
        L = [1]
        insertion_sort(L, 0, 0)
        self.assertEqual(L, [1])

    def test_multiple_items(self):
        L = [5, 2, 4, 6, 1, 3]
        insertion_sort(L, 0, len(L) - 1)
        self.assertEqual(L, [1, 2, 3, 4, 5, 6])


class Test_quicksort(unittest.TestCase):
    def test_empty_list(self):
        L = []
        quicksort(L, 0, -1)
        self.assertEqual(L, [])

    def test_single_item(self):
        L = [1]
        quicksort(L, 0, 0)
        self.assertEqual(L, [1])

    def test_multiple_items(self):
        L = [5, 2, 4, 6, 1, 3]
        quicksort(L, 0, len(L) - 1)
        self.assertEqual(L, [1, 2, 3, 4, 5, 6])


class Test_mergesort(unittest.TestCase):
    def test_empty_list(self):
        L = []
        mergesort(L, 0, -1)
        self.assertEqual(L, [])

    def test_single_item(self):
        L = [1]
        mergesort(L, 0, 0)
        self.assertEqual(L, [1])

    def test_multiple_items(self):  # doesnt work
        L = [5, 2, 4, 6, 1, 3]
        mergesort(L, 0, len(L) - 1)
        self.assertEqual(L, [1, 2, 3, 4, 5, 6])


class Test_magicsort(unittest.TestCase):
    """
    Tests that magic sort function
    """
    print("Testing magicsort")

    def test_use_reverse(self):
        """
        Makes sure magic sort returns a set with reverse_list in it
        """
        # A list with some negative numbers
        L = [20, 15, 13, 11, 10, 5, 2, -1, -3]
        # An all negative list
        L1 = [-1, -3, -7, -8]
        L0 = [L, L1]
        for list in L0:
            self.assertEqual(magic_sort(list), {"reverse_list"})
            self.assertTrue(is_sorted(list))

    def test_insertion_only(self):
        """
        Check that magic sort returns a set with insertion_sort where only use
        insertion sort on it
        """
        # A small list
        L = [19, 3, 1, 7]
        # List with some negative numbers

        L1 = [0, -2, 3, 6, 8, -1]
        # Random list less than or equal to the length of 16
        L2 = [10, 5, 1, 3, 6, 2, -4, -1, 0]
        L0 = [L, L1, L2]
        for list in L0:
            self.assertEqual(magic_sort(list), {"insertionsort"})
            self.assertTrue(is_sorted(list))

    def test_quick_insertion_merge(self):
        """
        Check that magic sort returns a set with quicksort, insertionsort, mergesort
        when only those edge cases are hit
        """
        # A list where reverse sorted except 1
        L = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 18, 19, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,
             1]
        self.assertEqual(magic_sort(L), {"quicksort", "insertionsort", "mergesort"})
        self.assertTrue(is_sorted(L))

    def test_quick_insertion(self):
        """
        Check that magic sort returns a set with only quicksort and insertionsort
        since it only hits the insertionsort edge case
        """
        # List with negative
        L = [-5, 1, 6, 2, 7, 1, 0, 9, 2, -1, 0, 3, 2, 1, 7, 2, 4, 6, 2]
        # Small list all positive
        L1 = [20, 19, 2, 5, 1, 6, 3, 2, 6, 1, 8, 3, 2, 6, 2, 11, 13]
        L0 = [L, L1]
        for list in L0:
            self.assertEqual(magic_sort(list), {"quicksort", "insertionsort"})
            self.assertTrue(is_sorted(list))


unittest.main()
