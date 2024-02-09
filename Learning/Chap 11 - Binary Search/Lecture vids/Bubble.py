"""
Lecture vid - mod06e
"""


def is_sorted(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True


# Invariant
#   After j loops, the j biggest items are in their final sorted positions
# Challenge: Stop early if list is sorted
def bubble_sort(L):
    for j in range(len(L) - 1):
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                # We only enter this block if 2 items are out of place - Challenge
                L[i], L[i + 1] = L[i + 1], L[i]


if __name__ == '__main__':
    import random

    L = [random.randint(0, 10) for i in range(1000)]
    L.append(-1)

    assert (not is_sorted(L))
    bubble_sort(L)
    assert (is_sorted(L))
    print("All done")
