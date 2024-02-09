def solve_puzzle(board, tile=0, memo=None):  # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    if memo is None:
        memo = set()

    # 1) Base case: have you found a valid solution?
    if tile == len(board) - 1:
        return True

    memo.add(tile)  # memoization

    # 2) Find all valid next-steps
    next_moves = set()
    for move in [tile + board[tile], tile - board[tile]]:
        move %= len(board)  # scaled move (changes neg. numbers)
        if move not in memo:
            next_moves.add(move)

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    # for move in next_moves:
    #     return any(solve_puzzle(L, move, memo))

    return any(solve_puzzle(board, move, memo) for move in next_moves)
