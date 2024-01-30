class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __eq__(self, other):
        pass
    # return self.x == other.x and self.y == other.y

    def distance(self, other):
        # return euclidean distance btw 2 points
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)
