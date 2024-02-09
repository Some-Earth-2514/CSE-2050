"""
Lecture vid - mod06c
To see the running time of a binary search recursive implementation can be as bad as a linear search if we use slices
instead of indices
We don't want to use slices as it takes too long and has a O(n) run time
"""


def bin_search_slice(L, item):
    # Initialize limits
    left, right = 0, len(L)
    median = (left + right) // 2

    # Check for base cases
    if L[median] == item:
        return True
    elif len(L) == 1:
        return False

    # Recursively search
    if L[median] < item:
        return bin_search_slice(L[median + 1: right], item)
    if L[median] > item:
        return bin_search_slice(L[left:median], item)
