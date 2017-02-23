'''
Realises the class Triangle to represent triangles and calculate their properties.
'''

from point import Point

class Triangle():
    '''
    Class to represent triangles.
    '''

    def __init__(self, point1: Point, point2: Point, point3: Point):
        '''
        Initialises the three points of the triangle.
        Raises ValueError if the points do not form a triangle.
        '''
        self.points = (point1, point2, point3)
        if not self.is_triangle():
            raise ValueError('Such a triangle does not exist')

    def is_triangle(self):
        '''
        Returns True if the points lie on the same straight line and are thus unsuitable.
        '''
        vec1 = self.points[1] - self.points[0]
        vec2 = self.points[2] - self.points[0]
        if vec1.x / vec2.x == vec1.y / vec2.y:
            return False
        else:
            return True

    def perimeter(self):
        '''
        Returns the perimeter of the triangle.
        '''
        sides = []
        for i in range(3):
            sides.append(self.points[i].distance(self.points[i - 1]))
        return sum(sides)

    def area(self):
        '''
        Calculates the area of the triangle as the cross product of the respective vectors divided by two.
        '''
        vec1 = self.points[1] - self.points[0]
        vec2 = self.points[2] - self.points[0]
        return abs(vec1.x*vec2.y - vec1.y*vec2.x) / 2
