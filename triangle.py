from point import Point

class Triangle():

    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.points = (point1, point2, point3)
        if not self.is_triangle():
            raise ValueError('Such a triangle does not exist')

    def is_triangle(self):
        vec1 = self.points[1] - self.points[0]
        vec2 = self.points[2] - self.points[0]
        if vec1.x / vec2.x == vec1.y / vec2.y:
            return False
        else:
            return True

    def perimeter(self):
        sides = []
        for i in range(3):
            sides.append(self.points[i].distance(self.points[i - 1]))
        return sum(sides)

    def area(self):
        vec1 = self.points[1] - self.points[0]
        vec2 = self.points[2] - self.points[0]
        return (vec1.x*vec2.y - vec1.y*vec2.x) / 2
