# _______________________________________________________ #
# Problem: given an amount of cents and a list of coins,  #
# find the fewest number of coins necessary to make that  #
# amount.                                                 #
# _______________________________________________________ #

def greedy_fewest_coins(amt, coins=[1, 5, 10, 25]):
    # Sort and reverse coin list
    coins.sort(reverse=True)

    # Iterate through coin list, the biggest value first
    # Use as many largest coins as possible
    # deduct that value from the amount remaining

    # Return number of coins
    num_coins = 0

    for coin in coins:
        if coin <= amt:
            num_coins += amt // coin  # 63 // 25 = 2
            amt %= coin  # 63 % 25  = 13

    return num_coins


print("Fewest coins to make $0.63 using only:")
print("\tpennies: ", end='')
print(greedy_fewest_coins(63, [1]))

print("\tpennies and nickles: ", end='')
print(greedy_fewest_coins(63, [1, 5]))

print("\tpennies, nickles, and dimes: ", end='')
print(greedy_fewest_coins(63, [1, 5, 10]))

print("\tpennies, nickles, dimes, and quarters: ", end='')
print(greedy_fewest_coins(63, [1, 5, 10, 25]))


def recr_fewest_coins(amt, coins=([1, 5, 10, 25])):
    # Sort and reverse coin list
    coins.sort(reverse=True)

    # Iterate through coin list, the biggest value first
    # Use as many largest coins as possible
    # deduct that value from the amount remaining

    # base case:
    if amt in coins:
        return 1

    # initialize guess at "optimum" soln
    min_coins = amt  # use pennies

    # go through every valid path
    for coin in coins:
        if coin <= amt:
            path_optimum = 1 + recr_fewest_coins(amt - coin, coins)
        if path_optimum < min_coins:
            min_coins = path_optimum

        return min_coins

    # update optimum soln when a new one is found

    # return optimum soln at this lvl


print("Fewest coins to make $0.63 using only:")
print("\tpennies: ", end='')
print(recr_fewest_coins(63, [1]))

print("\tpennies and nickles: ", end='')
print(recr_fewest_coins(63, [1, 5]))

print("\tpennies, nickles, and dimes: ", end='')
print(recr_fewest_coins(63, [1, 5, 10]))

print("\tpennies, nickles, dimes, and quarters: ", end='')
print(recr_fewest_coins(63, [1, 5, 10, 25]))

# _________________________________Quiz___________________________________ #
# Will this give the correct answer (the fewest coins) for any amount and  #
# any list of coins?                                                       #
#    1) yes                                                                #
#    2) no                                                                 #
# ________________________________________________________________________ #


# print("\tpennies, $0.21 pieces, and quarters: ", end = '')
# print(greedy_fewest_coins(63, [1, 5, 10, 21, 25]))
