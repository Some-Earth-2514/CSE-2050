"""
Euclid's algorithm
pg 95
"""


def fib(k):
    a, b = 0, 1
    for i in range(k):
        a, b = b, a + b
    return a


print(fib(400))
