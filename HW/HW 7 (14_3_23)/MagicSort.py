import math


def linear_scan(L):
    """
    Perform a linear scan on the list L and return a value that denotes which (if any) edge cases apply.
    """
    # Is the list already sorted?
    if all(L[i] <= L[i + 1] for i in range(len(L) - 1)):
        return "already sorted"

    # Are there at most 5 items out of place?
    if sum(1 for i in range(len(L) - 1) if L[i] > L[i + 1]) <= 5:
        return "insertion sort"

    # Is the list reverse sorted?
    if all(L[i] >= L[i + 1] for i in range(len(L) - 1)):
        return "reverse list"

    return "quicksort"


def reverse_list(L):
    """
    Reverse the list L in linear time.
    """
    left = 0
    right = len(L) - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def insertion_sort(L, left, right):
    """
    Sort the sublist L[left:right+1] in-place using insertion sort.
    """
    for i in range(left + 1, right + 1):
        key_item = L[i]
        j = i - 1
        while j >= left and L[j] > key_item:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key_item


def quicksort(L, left, right, depth=0, max_depth=None):
    """
    Sort the sublist L[left:right+1] in-place using quicksort, using the last item as the pivot element.
    """
    if max_depth is None:
        if len(L) > 0:
            max_depth = math.log2(len(L)) + 1

    if left >= right:
        return

    if depth >= 2 * max_depth:
        mergesort(L, left, right)
        return

    pivot_index = right
    i = left - 1
    for j in range(left, right):
        if L[j] <= L[pivot_index]:
            i += 1
            L[i], L[j] = L[j], L[i]
    i += 1
    L[i], L[pivot_index] = L[pivot_index], L[i]

    quicksort(L, left, i - 1, depth + 1, max_depth)
    quicksort(L, i + 1, right, depth + 1, max_depth)


def mergesort(L, left, right):
    """
    Sort the sublist L[left:right+1] in-place using mergesort.
    """
    if left < right:
        mid = (left + right) // 2
        mergesort(L, left, mid)
        mergesort(L, mid + 1, right)
        merge(L, left, mid, right)


def merge(L, left, mid, right):
    """
    Merge the two sublists L[left:mid+1] and L[mid+1:right+1] in-place.
    """
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if L[i] <= L[j]:
            temp.append(L[i])
            i += 1
        else:
            temp.append(L[j])
            j += 1
    while i <= mid:
        temp.append(L[i])
        i += 1
    while j <= right:
        temp.append(L[j])
        j += 1
        L[left:right + 1] = temp


def magic_sort(L):
    """
    This sorts in place using a variety of different sorting algorithms to achieve the
    optimal running time for sorting a list.
    Keeps tracks of the sorting algorithms used and returns them as a set
    """
    # Create an empty set to keep the algorithms in
    algorithms = set()
    # Use linearscan method to check for edge cases
    x = linear_scan(L)
    # See if any of the edge cases are hit and if so, use them and return that sorting method
    if x == "Use reverse sort":
        reverse_list(L, algorithms)
        return algorithms
    elif x == "Use insertion":
        insertion_sort(L, None, None, algorithms)
        return algorithms
    # If none of the edge cases are detected, use quicksort where the pivot is the last number
    else:
        quicksort(L, 0, None, 0, algorithms)
        return algorithms
