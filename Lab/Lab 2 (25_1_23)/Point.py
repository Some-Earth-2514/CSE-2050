class Point:
    def __init__(self, x, y):
        """Constructs all necessary information of a point"""
        self.x = x
        self.y = y

    def __lt__(self, test):
        """Finds which point is less than the other with respect to the origin"""
        return self.dist_from_origin() < test.dist_from_origin()

    def __gt__(self, test):
        """Finds which point is greater than the other with respect to the origin"""
        return self.dist_from_origin() > test.dist_from_origin()

    def __eq__(self, test):
        """Finds if the points are equidistant from the origin"""
        return self.dist_from_origin() == test.dist_from_origin()

    def __str__(self):
        """Converts the point into a string"""
        return f'Point({self.x}, {self.y})'

    def dist_from_origin(self):
        """Calculates the distant from the origin"""
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


# ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below

if __name__ == '__main__':
    # All tests should use `assert`, not `print`

    # test init
    # assert correct x
    # assert correct y
    p1 = Point(3, 4)
    assert p1.x == 3
    assert p1.y == 4
    p2 = Point(5, 6)
    assert p2.x == 5
    assert p2.y == 6

    # test lt #
    # Expected True (e.g `p1 < p2`)
    # Expected False (e.g. `not p1 < p2`)
    assert p1 < p2
    assert not p2 < p1

    # test gt #
    # Expected True (e.g `p1 > p2`)
    # Expected False (e.g. `not p1 > p2`)
    assert p2 > p1
    assert not p1 > p2

    # test eq #
    # Expected True (e.g `p1 == p2`)
    # Expected False (e.g. `not p1 == p2`)
    p3 = Point(4, 3)
    assert p1 == p3
    assert not p1 == p2

    # test str #
    # assert str(some_point) == expected_string
    assert str(p1)

    # test dist_from_origin() #
    assert p1.dist_from_origin() == 5

    print("All tests completed")
