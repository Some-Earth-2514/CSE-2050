"""
Sumk function in recursion
Finds the sum of numbers from 1 to k
pg 91
"""


def f(k):
    if k > 0:
        return f(k - 1) + k
    return 0


print(f(5))
