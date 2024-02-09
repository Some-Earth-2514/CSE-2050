"""
Lecture vid - mod5c
"""


def greedy_fc(amt, coins):
    coins.sort(reverse=True)

    n = 0
    for c in coins:
        while c <= amt:
            amt -= c
            n += 1
    return n


def naive_recr(amt, coins):
    n_opt = amt  # assume we have pennies

    for c in coins:
        if c == amt:
            return 1
        elif c < amt:
            n = naive_recr(amt - c, coins) + 1

            if n < n_opt:  # update "optimal soln" if appropriate
                n_opt = n

    return n_opt


if __name__ == '__main__':
    coins = [1, 10, 25]
    assert naive_recr(50, coins) == 2  # 2x $0.25
    assert naive_recr(27, coins) == 3  # 1x $0.25 + 2x $0.01
    print("All done")

    coins = [1, 5, 21, 25]
    assert naive_recr(63, coins) == 3  # 3x $0.21
    print("All done")
