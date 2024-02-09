"""
Euclid's algorithm for gdc (greatest common divisor)
pg 96
"""


def gcd(a, b):
    if a == b:
        return a
    if a > b:
        a, b = b, a
    return gcd(a, b - a)


print(gcd(19, 513))


def gcd_revised(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(a, b % a)


print("GCD of 12 and 513 is", gcd_revised(12, 513))
print("GCD of 19 and 513 is", gcd_revised(19, 513))  # RecursionError
print("GCD of 19 and 515 is", gcd_revised(515, 19))
