import time


def time_function(func, args, n_trials=10):
    """Returns the minimum number of seconds to run func with args"""
    min_time = float('inf')
    for t in range(n_trials):
        start_t = time.time()  # gets current system time
        func(args)
        end_t = time.time()
        min_time = min(min_time, end_t - start_t)
    return min_time


def time_function_flexible(f, args, n_trials=10):
    """Returns the minimum number of seconds to run func with args with more flexibility for time functions"""
    min_time = float('inf')
    for t in range(n_trials):
        start_t = time.time()  # gets current system time
        f(*args)
        end_t = time.time()
        min_time = min(min_time, end_t - start_t)
    return min_time


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        """Iterates through every item in the list"""
        for item in L:
            item *= 2


    L1 = [i for i in range(10 ** 5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10 ** 6)]  # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1 * 1000))
    print("t(L2) = {:.3g} ms".format(t2 * 1000))
