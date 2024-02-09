"""
Lecture vid - mod06a
"""


def contains(L, item):
    n = len(L)  # 1

    # can replace this with python's any() func
    # loops over a whole list and as soon as a condition is met, returns True, else False
    for obj in L:  # nx
        if obj == item:  # 1
            return True  # 1

    return False  # 1
    # 1 + n(1) + 1 = O(n)


def contains_2(L, item):
    return any(obj == item for obj in L)


if __name__ == '__main__':
    n = 100
    L = [i for i in range(n)]

    for i in range(n):
        assert contains_2(L, i)

    assert not contains_2(L, n)
