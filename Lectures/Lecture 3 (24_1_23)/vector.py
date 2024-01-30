"""
v1 = Vector()
v1.x = 3 # add x to v1's namespace
v1.y = 4 # add y to v1's namespace
v1.magnitude() look for 'magnitude()' in v1's namespace
5.0
"""


class Vector:

    # constructor method
    # called when an instance is created
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2))

    def __repr__(self):
        return f'Vector : x={self.x} y={self.y}'