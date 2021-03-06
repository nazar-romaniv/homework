'''
The module realises the class Point and defines operations on the objects of the class, which correspond to
similar operations for vectors.
'''

from math import radians, cos, sin

class Point:
    """
    Represents a point in two-dimensional geometric coordinates and defines operations on points
    similar to those on vectors.
    """

    def __init__(self, x=0, y=0):
        """
        Initialize the position of a new point. The x and y coordinates can
        be specified. If they are not, the point defaults to the origin.
        """

        self.move(x, y)

    def move(self, x, y):
        """
        Move the point to a new location in 2D space.
        """

        self.x = x
        self.y = y

    def rotate(self, beta, other):
        """
        Rotate point around other point
        """

        dx = self.x - other.x
        dy = self.y - other.y
        beta = radians(beta)
        x_point3 = dx*cos(beta) - dy*sin(beta)
        y_point3 = dy*cos(beta) + dx*sin(beta)
        x_point3 = x_point3 + other.x
        y_point3 = y_point3 + other.y
        self.move(x_point3, y_point3)

    def __add__(self, other):
        '''
        Vector sum of two vectors.
        '''
        return Point(x=self.x + other.x, y=self.y + other.y)

    def __iadd__(self, other):
        self.move(self.x + other.x, self.y + other.y)
        return self

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)

    def __isub__(self, other):
        self.move(self.x - other.x, self.y - other.y)
        return self

    def __mul__(self, other):
        '''
        Operation similar to vector multiplication with a constant.
        '''
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):
        self.move(self.x * other, self.y * other)
        return self

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):
        self.move(self.x / other, self.y / other)
        return self

    def __floordiv__(self, other):
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):
        self.move(self.x // other, self.y // other)
        return self

    def __abs__(self):
        '''
        Returns the absolute value of the respective vector.
        '''
        return self.x ** 2 + self.y ** 2

    def distance(self, other):
        '''
        Returns the distance between two points.
        '''
        return abs(self - other)
