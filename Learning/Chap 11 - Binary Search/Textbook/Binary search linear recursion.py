"""
Binary search linear recursion - tree of function calls in a single chain
pg 106
"""


def bs(L, item, left=0, right=None):
    if right is None:
        right = len(L)
    if right - left == 0:
        return False
    if right - left == 1:
        return L[left] == item
    median = (right + left) // 2
    if item < L[median]:
        return bs(L, item, left, median)
    else:
        return bs(L, item, median, right)
