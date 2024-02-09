"""
Lecture vid - mod07b
"""


def is_sorted(L):
    return not any(L[i] > L[i + 1] for i in range(len(L) - 1))


def merge_sort(L):
    # 1) Divide into subproblems
    # 2) Solve our subproblems
    # 3) Combine sub-solutions into main solution

    # Base case: list with 1 or fewer items
    if len(L) <= 1:
        return L

    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    left = merge_sort(left)
    right = merge_sort(right)

    # Start zipping up subproblems
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i + j] = left[i]
            i += 1
        else:
            L[i + j] = right[j]
            j += 1

    L[i + j:] = left[i:] + right[j:]

    # Return list to next level of recursion
    return L


# Create an unsorted list, then sort it
if __name__ == '__main__':
    # Create an unsorted list
    import random
    L = [random.randint(0, 10) for i in range(10000)]
    L.append(-1)

    # Sort it
    assert (not is_sorted(L))
    merge_sort(L)
    assert(is_sorted(L))
