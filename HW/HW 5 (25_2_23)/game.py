import maze


class Game:
    """Holds the game solving logic. Initialize with a fully initialized maze"""

    def __init__(self, maze):
        self._maze = maze

    # Creating simple methods (like the next two) to abstract core parts
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        """If (row, column) is already in the solved path then it is not available
        Returns if the move is available or not"""
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        """Is the given row,column the finish square?
        Returns is the puzzle is solved or not"""
        return self._maze.get_finish() == (row, col)

    def try_move(self, currow, curcol, curscore, curpath):
        """Finds possible moves and tries everything, returns one that has been tried"""
        if self._maze.is_move_in_maze(currow, curcol) and self._is_move_available(currow, curcol, curpath) and not self._maze.is_wall(currow, curcol):
            x = self._maze.make_move(currow, curcol, curpath)  # rename variable
            if self._is_puzzle_solved(currow, curcol):
                return curscore + x, curpath
            else:
                return self.find_route(currow, curcol, curscore + x, curpath)
            # Calculate the score for moving to the new position
        else:
            return -1, curpath

        # Base case: if we've reached the finish square, return the current score and path

    ########################################################
    # TODO - Main recursive method. Add your algorithm here.

    def find_route(self, currow, curcol, curscore, curpath={}):
        """Finds the path around the maze to get points and win game"""
        if self._maze.get_start() == (currow, curcol):
            curscore = self._maze.make_move(currow, curcol, curpath)
        best_score = -1
        best_path = []

        for i in range(4):
            if i == 0:  # up
                score, path = self.try_move(currow - 1, curcol, curscore, list(curpath))
            elif i == 1:  # down
                score, path = self.try_move(currow + 1, curcol, curscore, list(curpath))

            elif i == 2:  # right
                score, path = self.try_move(currow, curcol + 1, curscore, list(curpath))
            elif i == 3:  # left
                score, path = self.try_move(currow, curcol - 1, curscore, list(curpath))

            # Base case: if we've reached the finish square, return the current score and path
            if score > best_score:
                best_score = score
                best_path = path

        return best_score, best_path


# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(3, 6)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create
    #         different grids
    #     * But not easy to use in testcases because you cannot predictable
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid.init_random(0, 9)  # Initialize to a random board
    grid.add_random_walls(0.2)  # Make a certain percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing
    #   the Values and Walls, you must set the Start Finish locations.
    start = (0, 2)
    finish = (1, 1)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)  # Print the maze for visual starting reference

    # Now instantiate your Game algorithm class
    game = Game(grid)  # Pass in the fully initialize maze grid

    # Now initiate your recursive solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")
