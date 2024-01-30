import random
import sys
import timeit


def is_sorted(L): return not any(L[i] > L[i + 1] for i in range(len(L) - 1))


def quicksort(L, left=0, right=None, depth=0):
    """Sorts L in-place using quicksort"""
    depth += 1
    global max_depth
    if depth > max_depth:
        max_depth = depth
    depth += 1
    if right is None:
        right = len(L)

    # Base case
    if right - left <= 1:
        return

    # Divide
    median = partition(L, left, right)

    quicksort(L, left, median, depth)
    quicksort(L, median + 1, right, depth)


def partition(L, left, right):
    """Partitions L[left:right] around L[right-1]
            Input
            -----
                L: list[int]
                    list of integers
                left: int
                    index of leftmost item to be considered
                right: int
                    index of rightmost item to be considered + 1

            Output
            ------
                pivot: int
                    index of the pivot element after partitioning (where L[right-1] ends up)
    """

    # Init some counters
    i = left  # index of 1st item
    j = right - 2  # index of 2nd last item
    pivot = right - 1  # index of last item

    # i, j, pivot = lef, right - 2, right - 1

    while i < j:
        # find first big item on left
        while L[i] < L[pivot]:
            i += 1

        # find first small item on right
        while i < j and L[j] >= L[pivot]:
            j -= 1

        if i < j:
            L[i], L[j] = L[i], L[j]

    # this can give errors in lists of len <= 2
    if L[pivot] <= L[i]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    return pivot


def shitty_partition(L, left, right):
    Llow = []
    Lhigh = []
    for i in range(len(L) - 1):
        if L[i] < L[-1]:
            Llow.append(L[i])
        else:
            Lhigh.append(L[i])

    L = Llow + [L[-1]] + Lhigh


def mergesort(L, depth=0):
    """sorts L using mergesort"""
    depth += 1
    global max_depth
    if depth > max_depth:
        max_depth = depth
    # base case
    if len(L) <= 1:
        return L

    # divide
    median = len(L) // 2
    Lleft = mergesort(L[:median])
    Lright = mergesort(L[median:])

    # conquer
    merge(L, Lleft, Lright)

    return L


def merge(L, Lleft, Lright):
    """merges sorted sublists Lleft and Lright into L"""
    i, j = 0, 0
    while i < len(Lleft) and j < len(Lright):
        if Lleft[i] < Lright[j]:
            L[i + j] = Lleft[i]
            i += 1
        else:
            L[i + j] = Lright[j]
            j += 1

    L[i + j:] = Lleft[i:] + Lright[j:]

    return L


if __name__ == '__main__':
    # test our algs work
    sys.setrecursionlimit(10000)
    n = 10000
    # ceil(log2(n)) + 1

    L = [random.randint(0, n) for i in range(n)]
    Lmerge = L[:]
    Lquick = L[:]

    # mergesort(Lmerge)
    # assert is_sorted(Lmerge)
    #
    # quicksort(Lquick)
    # assert is_sorted(Lquick)W


    ### Times mergesort
    max_depth = 0
    t_merge = 1000*timeit.timeit("mergesort(L)", setup=f"L={Lmerge}", globals=globals(), number=1) 
    print(f"t_merge: {t_merge:.3f} ms")
    print(f"max_depth = {max_depth}") 
    print()

    ### Times quicksort
    max_depth = 0
    t_quick = 1000*timeit.timeit("quicksort(L)", setup=f"L={Lquick}", globals=globals(), number=1)
    print(f"t_quick: {t_quick:.3f} ms")
    print(f"max_depth = {max_depth}")
    print()
