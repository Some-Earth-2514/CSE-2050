import unittest
import game
import maze


class TestGame(unittest.TestCase):

    def test_maze(self):
        """An example test that shows all the steps to initialize and invoke the solution algorithm"""

        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1, "*", 1, 1],
                        [2, 5, "*", "*", 2],
                        [3, "*", "*", "*", 8],
                        [9, "*", 4, 7, 3],
                        [1, 3, 1, "*", 2]])
        start = (0, 1)
        end = (0, 3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4),
                                (2, 4), (1, 4), (0, 4), (0, 3)])

    #############################################
    # TODO - add the rest of your test cases here

    def test_long_path(self):
        """Test a maze where the longest path is taken"""
        grid = maze.Maze(3, 3)
        grid._set_maze([[0, 1, 1],
                        [0, 0, 1],
                        [0, 1, 0]])
        start = (0, 0)
        end = (2, 2)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())
        self.assertEqual(score, 4)
        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2)])

    def test_smallmaze(self):
        """Test a maze of small size"""
        grid = maze.Maze(2, 2)
        grid._set_maze([[0, 1],
                        [2, 4]])
        start = (0, 0)
        finish = (1, 0)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        self.assertEqual(score, 5)
        self.assertEqual(path, [(0, 0), (0, 1), (1, 1), (1, 0)])

    def test_big_maze(self):
        """Test a maze of big size"""
        grid = maze.Maze(5, 7)
        grid._set_maze([[0, "*", 3, "*", 8, 9, 11],
                        [10, 4, 3, 9, 2, 4, "*"],
                        [9, 2, 1, 0, "*", 8, 4],
                        ["*", 3, "*", 7, 3, 6, 9],
                        [11, 6, 3, 5, "*", 8, 4]])
        start = (0, 6)
        finish = (4, 3)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        self.assertEqual(score, 121)
        self.assertEqual(path, [(0, 6), (0, 5), (0, 4), (1, 4), (1, 5), (2, 5), (2, 6), (3, 6), (4, 6),
                                (4, 5), (3, 5), (3, 4), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0),
                                (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)])

    def test_no_path(self):
        """Test a maze that has no path"""
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1, "*", 1, 1],
                        [2, 5, "*", "*", 2],
                        [3, "*", "*", "*", 8],
                        [9, "*", 4, 7, 3],
                        [1, 3, 1, "*", 2]])
        start = (0, 1)
        end = (0, 4)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)

    def test_walls(self):
        """Test a maze's walls"""
        grid = maze.Maze(2, 3)
        grid._set_maze([[0, "*", "*"],
                        ["*", "*", 2]])

        start = (0, 0)
        finish = (0, 2)
        grid.set_start_finish(start, finish)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        self.assertEqual(score, -1)
        self.assertEqual(path, [])


if __name__ == '__main__':
    unittest.main()
