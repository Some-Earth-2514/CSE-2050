def factorial(x):
    """Returns factorial of x"""
    # is x an int?
    if not isinstance(x, int):
        raise ValueError("Can only calculate factorials of integers")

    # is x >= 1?
    if x < 1:
        raise ValueError("Can only calculate factorial if x >= 1")

    product = 1
    while x > 1:
        product *= x
        x -= 1

    return product

    pass


print("testing factorial(5)")
assert factorial(5) == 120

print("testing factorial(1.3)")
# test that the code raises and exception in certain cases

try:
    factorial(1.3)
    raise AssertionError("factorial(1.3) did not raise value error")

except ValueError:
    pass

print("testing factorial(-1)")
try:
    factorial(-1)
    raise AssertionError("factorial(-10 did not raise a ValueError")
except ValueError:
    pass

# use TDD to write a sum_k(k) method
# return sum of first k integers
# sum_k(1) = 1
# sum_k(2) = 1 + 2
# sum_k(3) = 1 + 2 + 3

def sum_k(k):
    temp_sum = 0

    while k > 0:
        temp_sum += k
        k -= 1

    return temp_sum


# unit test 1
print(sum_k(1))
assert sum_k(1) == 1
assert sum_k(2) == 3
assert sum_k(3) == 6

# unit test 2
# try/except blocks for input validation

print(sum_k(3))
