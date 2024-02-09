"""
Recursively defined fibonacci function
pg 94
"""


def fib(k):
    if k in [0, 1]:
        return k
    return fib(k-1) + fib(k-2)


print([fib(i) for i in range(15)])

# takes too long even for small numbers of "k"
