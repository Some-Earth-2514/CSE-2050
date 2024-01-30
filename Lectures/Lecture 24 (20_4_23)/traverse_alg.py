"""traverse(start):
    # Initialize
    # 1) Initialize empty collections to_visit and tree
    # 2) Add (start, None) to to_visit

    # Traverse
    # 3) Until to_visit is empty:
        # 3.a) chd, par = to_visit.remove()
        # 3.b) add chd:par to tree
        # 3.c) add chd's nbrs to to_visit

    # Return

    # to_visit could be LIFO (stack) or FIFO (queue) - which gives each tree?
    # Depth-First Search (DFS) - to_visit is a stack
    # Breadth-First Search (BFS) - to_visit is a queue"""
