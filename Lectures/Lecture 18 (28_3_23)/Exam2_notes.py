# Invariant - smth  that is always true at a certain point in our algo

def bubble(L):
    n = len(L)

    for i in range(n - 1):
        for j in range(n - 1 - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1],L[j]

# Invariant - at line 6, the ith biggest items are in their final, sorted position

# reason that this algo is correct:
# after n-1 loops, the n-1 biggest items are in their final, sorted positions
# the last item only has one position it can be
# therefore, the lise is sorted

# insertion invariant:
