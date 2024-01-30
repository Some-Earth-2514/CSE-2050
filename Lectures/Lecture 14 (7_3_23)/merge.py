# L1 is a sorted list
# L2 is a sorted list
# how long to make L3, which is a sorted version of L1 + L2

def merge(L1, L2):
    """Return L3, which is a sorted version of L1 + L2"""
    # do not use list.sort()
    # assume L1 and L2 are sorted
    L3 = [None for i in range(len(L1) + len(L2))]

    i1, i2 = 0, 0
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L3[i1 + i2] = L1[i1]
            i1 += 1
        else:
            L3[i1 + i2] = L2[i2]
            i2 += 1

    return L3


def mergesort(L):
    n1 = len(L)

    # base case
    if n1 <= 1:
        return L

    # find median
    median = n1 // 2

    # recursively sort left half
    Lleft = mergesort(L[:median])  # does not include L[median]

    # recursively sort right half
    Lright = mergesort(L[median:])  # does not include L[median]

    # CONQUER
    return merge(Lleft, Lright)


def is_sorted(L):
    return not any(L[i] > L[i + 1] for i in range(len(L) - 1))


def bubble(L):
    n2 = len(L)
    for i in range(n2-1):
        keepgoing = False
        for j in range(n2-1-i):
            if L[j] > L[j + 1]:
                keepgoing = True
                L[j], L[j + 1] = L[j + 1], L[j]
        if not keepgoing:
            break


if __name__ == '__main__':
    n = 10
    import random
    L = [random.randint(0, n) for i in range(n)]

    L.append(-1)

    assert not is_sorted(L)
    L = mergesort(L)
    assert is_sorted(L)
    print("works")
