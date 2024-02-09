# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    """Finds the first zero value in the list and makes it the left most index"""
    left = 0
    right = len(L) - 1

    while left <= right:
        mid = (left + right) // 2
        if L[mid] == 0:
            return mid
        elif L[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

    return None


def bubble(L, left, right):
    """Uses bubble sort to sort the range of values from
    left to right in ascending order"""
    for i in range(left, right - 1):
        for j in range(left, right - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


def selection(L, left, right):
    """Uses selection sort to sort the range of values from
    left to right in ascending order"""
    for i in range(left, right - 1):
        min = i
        for j in range(i + 1, right):
            if L[j] < L[min]:
                min = j
        L[i], L[min] = L[min], L[i]


def insertion(L, left, right):
    """Uses insertion sort to sort the range of values from
    left to right in ascending order"""
    for i in range(left + 1, right):
        j = i - 1
        while j >= left and L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            j -= 1


def sort_halfsorted(L, sort):
    """Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items

        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            L = [-1, -2, -3, 0, 3, 2, 1]
            sort_halfsorted(L, bubble)
            print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    """

    idx_zero = find_zero(L)
    sort(L, 0, idx_zero)
    sort(L, idx_zero, len(L))
