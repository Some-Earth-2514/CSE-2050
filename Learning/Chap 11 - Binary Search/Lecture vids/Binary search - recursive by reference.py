"""
Lecture vid - mod06d
Binary search using recursion without using slices of list
"""


def bs(L, item, left=0, right=None):
    if right is None:
        right = len(L) - 1

    median = (right + left) // 2

    # base cases
    if L[median] == item:
        return True
    if (right - left) <= 1:
        return L[right] == item

    if item < L[median]:
        return bs(L, item, left, median)
    elif item > L[median]:
        return bs(L, item, median, right)


if __name__ == '__main__':
    n = 128
    L = [i for i in range(n)]

    for i in range(n):
        assert bs(L, i)

    assert not bs(L, -1)
    print("All done")
