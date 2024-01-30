from Shapes import Point
import unittest


# Create 1 unittest.TestCase class per you are testing
class TestPoint(unittest.TestCase):
    """All unitest for Point class"""

    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(3, 4)
        self.p3 = Point(3, 4)

    def test_init(self):
        # p1 = Point(3, 4)
        print('test_init')
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)

    def test_distance(self):
        self.assertEqual(self.p1.distance(self.p2), 0)
        self.assertAlmostEqual(self.p1.distance(self.p3), 1.414, 5)

    def test_eq(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        p3 = Point(4, 5)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

        # self.assertLess(p1, p2)
        # self.assertGreater(p2, p1)

    class TestRectangle(unittest.TestCase):
        def test_init(self):
            pass

        def test_perimeter(self):
            pass


print('hello')
unittest.main()
