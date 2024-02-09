import time


def find_pairs_naive(lst, target):
    """Iterates over the entire list using two nested loops to check for pairs that add up to the target"""
    lst_set_naive = set()                       # 1

    for i in range(len(lst)):                   # n
        for j in range(i + 1, len(lst)):        # n
            if lst[i] + lst[j] == target:       # 1 + 1
                temp_tuple = (lst[i], lst[j])   # 1
                lst_set_naive.add(temp_tuple)   # 1
    return lst_set_naive                        # 1
                                                # O(1 + n(n (1 + 1 + 1 + 1)) + 1) = O(2 + n(n(4)))


def find_pairs_optimized(lst, target):
    """Uses a data structure to improve the time complexity of the algorithm"""

    lst_set_optimized = set(lst)                                    # 1
    output = set()                                                  # 1
    for i in lst:                                                   # n
        compliment = target - i                                     # 1
        if compliment in lst_set_optimized and compliment != i:     # 1
            if i < compliment:                                      # 1
                output.add((i, compliment))                         # 1
                lst.pop(lst.index(i))                               # 1
                lst_set_optimized.remove(compliment)                # 1
            elif compliment < i:                                    # 1
                output.add((compliment, i))                         # 1
                lst.pop(lst.index(i))                               # 1
                lst_set_optimized.remove(compliment)                # 1
    return output                                                   # 1
                                                                    # O(1 + 1 + n(1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) + 1) = O(3 + n(10))

# O(13n)


def measure_min_time(fn, args):
    """Measures the minimum time of 10 runs for both functions using the time module"""
    min_time = float('inf')
    for t in range(10):
        start_t = time.time()  # gets current system time
        fn(*args)
        end_t = time.time()
        min_time = min(min_time, end_t - start_t)
    return min_time


if __name__ == "__main__":

    print('=' * 40)
    print(f"{'n':<10}{'naive':<10}{'optimized':<10}")
    print('-' * 40)

    for n in (10, 50, 100, 150, 200, 300, 500):
        v = [1, 2, 3, 4, 5] * n
        naive = 1000 * measure_min_time(find_pairs_naive, (v, 1))
        optimized = 1000 * measure_min_time(find_pairs_optimized, (v, 1))

        print(f"{n:<10}{naive:<10.4f}{optimized:<10.4f}")

    # table footer
    print('-' * 40)
