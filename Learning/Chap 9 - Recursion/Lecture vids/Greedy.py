"""
Lecture vid - mod05b
"""


def greedy_fc(amt, coins):
    coins.sort(reverse=True)

    n = 0
    for c in coins:
        while c <= amt:
            amt -= c
            n += 1
    return n


if __name__ == '__main__':
    coins = [1, 5, 10, 25]
    assert greedy_fc(50, coins) == 2
    assert greedy_fc(28, coins) == 4
    print("All done")

    coins = [1, 5, 10, 21, 25]
    assert greedy_fc(63, coins) == 3
