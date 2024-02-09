"""
Binary search - looking for an item in a sorted list, break the list in half and repeat the search on whichever side
could contain the missing element, which can be found by comparing with the median element
Has a single recursive call to repeat on a smaller list
pg 105
"""


def bs(L, item):
    if len(L) == 0:
        return False
    median = len(L) // 2
    if item == L[median]:
        return True
    elif item < L[median]:
        return bs(L[:median], item)
    else:
        return bs(L[median + 1:], item)
