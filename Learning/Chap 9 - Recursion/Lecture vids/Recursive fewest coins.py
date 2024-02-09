"""
Lecture vid - mod5d
"""


def fewest_coins(amt, coins):
    if amt in coins:
        return 1

    valid_coins = (for c in coins if c < amt)

    min_coins = amt

    for coin in valid_coins:
        num_coins = 1 + fewest_coins(amt - coins, coins)

        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins
