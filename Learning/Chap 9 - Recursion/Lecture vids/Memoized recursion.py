"""
Lecture vid - mod05e
"""


def naive_recr(amt, coins):
    n_opt = amt  # initialize optimal soln

    for c in coins:
        if c == amt:
            return 1  # guaranteed optimal!

        elif c < amt:
            n = naive_recr(amt - c, coins) + 1  # possibly better than current best

            if n < n_opt:  # update "optimal soln" if appropriate
                n_opt = n

    return n_opt


# memoization - keeps track of solved sub_problems
def memo_recr(amt, coins):
    solved = dict()
    return _memo_recr(amt, coins, solved)


def _memo_recr(amt, coins, solved):
    if amt in solved:
        return solved[amt]

    solved[amt] = amt  # initalize optimal soln with pennies

    for c in coins:
        if c == amt:
            solved[amt] = 1
            return 1

        elif c < amt:
            n = _memo_recr(amt - c, coins, solved) + 1

            if n < solved[amt]:
                solved[amt] = n
    return solved[amt]


if __name__ == '__main__':
    coins = [1, 5, 10, 21, 25]
    assert memo_recr(50, coins) == 2  # 2x $0.25
    assert memo_recr(27, coins) == 3  # 1x $0.25 + 2x $0.01

    coins = [1, 5, 10, 13, 17, 21, 25]
    assert memo_recr(63, coins) == 3  # 3x $0.21
    print("All done")
