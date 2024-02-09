"""
Binary search tail recursion - function directly returns the result of the recursive function call
pg 106
"""


def bs(L, item):
    left, right = 0, len(L)
    while right - left > 1:
        median = (right + left) // 2
    if item < L[median]:
        right = median
    else:
        left = median
    return right > left and L[left] == item
