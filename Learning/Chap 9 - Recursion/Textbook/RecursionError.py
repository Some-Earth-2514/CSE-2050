"""
RecursionError
pg 93
"""


def a(k):
    if k == 0:
        return 0
    return b(k)


def b(k):
    return c(k)


def c(k):
    return a(k-1)


print(a(340))
