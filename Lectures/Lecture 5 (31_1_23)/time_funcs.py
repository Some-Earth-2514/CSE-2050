# write a func that times how long a func takes
import time


def time_f(func, arg):
    """returns how long-running func(arg) takes"""
    start = time.time()  # gets current system time

    func(arg)

    end = time.time()

    return end - start


def create_list_a(n):
    """creates a list with n items"""
    L = []              # cost 1
    for i in range(n):  # cost n times
        L.append(i)     # cost 1

    return L            # cost 1
                        # total cost n + 3 (about)


def create_list_b(n):
    L = []              # cost 1
    for i in range(n):  # cost n times
        L.insert(0, n)  # cost n - i
    return L            # cost 1
                        # total cost n + 2 - i (about)


if __name__ == "__main__":
    print('=' * 40)
    print(f"{'n':<10}{'t_a (ms)':<10}{'t_b (ms)':<10}")
    print('-' * 40)

    for n in (100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000):
        t_a = 1000 * time_f(create_list_a, n)
        t_b = 1000 * time_f(create_list_b, n)

        print(f"{n:<10}{t_a:<10.3f}{t_b:<10.3f}")

    # table footer
    print('-' * 40)
