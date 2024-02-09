"""
Lecture vid - mod05f
"""


def greedy_fc(amt, coins):
    coins.sort(reverse=True)

    n = 0
    for c in coins:
        while c <= amt:
            amt -= c
            n += 1
    return n


def dyn_fc(amt, coins):
    solved = {i: i for i in range(1, amt + 1)}  # 'optimal soln' assuming pennies

    for a in range(1, amt + 1):
        for c in coins:
            if c == a:
                solved[a] = 1
                break
            elif c < a:
                n = 1 + solved[a-c]
                if n < solved[a]:
                    solved[a] = n
    return solved[amt]


if __name__ == '__main__':
    coins = [1, 5, 10, 21, 25]
    assert dyn_fc(50, coins) == 2  # 2x $0.25
    assert dyn_fc(27, coins) == 3  # 1x $0.25 + 2x $0.01

    coins = [1, 5, 10, 13, 17, 21, 25]
    assert dyn_fc(63, coins) == 3  # 3x $0.21
    print("All done")
