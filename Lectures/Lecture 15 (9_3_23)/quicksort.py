def partition(L, left, right):
    # partition L about L[right - 1]
    partition([7, 6, 5, 4, 3, 2, 1], 0, 7)
    # partition L about L[6]

    # get everything smaller to the left
    # everything equal or bigger to the right
    # swap your pivot
    # return new index of pivot


def quickselect(L, k):
    """return the kth biggest item in L



    Examples
    --------
    L = [2, 5, 6, 8, 3, 4, 6, 6]
    quickselect(L, 3) # find 3rd biggest item
    """

    # in a sorted list, the third smallest item is at index 2
    # the nth smalled item is at index n-1

    # kth biggest item is at index n-k

    # 1) pivot = partition(L, left, right)
    # 2) Is k > pivot or < pivot?.

    # find biggest
    # O(n) memory overhead
