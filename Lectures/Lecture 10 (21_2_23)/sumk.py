import timeit
import sys

sys.setrecursionlimit(5000)


# removes recursion error by manually changing it, has a limit of 1000 or less depending on code


def sumk(k):  # O(k)
    temp_sum = 0

    for i in range(1, k + 1):
        temp_sum += 1

    return temp_sum


# sum(k) = k + (k-1) + (k-2) + (k-3) + ... + 1
# sum(k) = sum(k) + sum(k-1)
#                   k-1 + sum(k-2)
#                         k-2 + sum(k-3)


def sumk_recr(k):
    if k == 0:
        return 0

    # base case - k == 1
    if k == 1:
        return 1

    return k + sumk_recr(k - 1)  # my function calls itself


assert sumk_recr(0) == 0
assert sumk_recr(1) == 1
assert sumk_recr(4) == 10

x = sumk_recr(10)

print(sumk_recr(998))  # 1000 gives error stack overflow for recursion

for func in [sumk, sumk_recr]:
    t = timeit.timeit(f'{func.__name__}(20)', globals=globals())
    print(f"{func.__name__}: {t:.3g} s")


# write a recursive factorial function
# factorial(n) = n * (n-1) * (n-2) * ... * 2 * 1
#              = n * factorial(n-1)


def factorial(n):
    # base case
    if n in {0, 1}:
        return 1

    return n * factorial(n - 1)


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120


# find the kth fibonacci number
# fibs - 1, 1, 2, 3, 5, 8, 13...
# each number is the sum of the 2 previous numbers
# base cases:
#       fib(1) = 1
#       fib(2) = 2

def fib(n):
    # base cases:
    if n in {1, 2}:
        return 1

    return fib(n - 1) + fib(n - 2)


assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
# O(2^n)


def fib_memo(n, solved=None):
    if solved is None:
        solved = {1: 1, 2: 1}

    # Memoized:
    # solved
    #       1 - 1
    #       2 - 1
    #       3 - 2
    #       4 - 3
    #       5 - 5
    #       6 - 8

    # base cases:
    if n in solved:
        return solved[n]

    solved[n] = fib_memo(n - 1, solved) + fib_memo(n - 2, solved)

    return solved[n]
    # old:
    # return fib(n-1) + fib(n-2)


assert fib_memo(1) == 1
assert fib_memo(2) == 1
assert fib_memo(3) == 2
assert fib_memo(4) == 3
assert fib_memo(5) == 5

for n in [10, 20, 30, 40, 50]:
    run_str = f"fib2({n})"
    t = timeit.timeit(f'{func.__name__}(20)', globals=globals())
    print(f"n = {n}")
