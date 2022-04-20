# A Python3 program to find if 2 given line segments intersect or not
from math import fabs
from sys import float_info


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2


class Rectangle:
    def __init__(self, horizontal_line1: Line, horizontal_line2: Line, vertical_line1: Line, vertical_line2: Line):
        self.horizontal_line1 = horizontal_line1
        self.horizontal_line2 = horizontal_line2
        self.vertical_line1 = vertical_line1
        self.vertical_line2 = vertical_line2


# Given three collinear points p, q, r, the function checks if
# point q lies on line segment 'pr'
def onSegment(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if val > 0:

        # Clockwise orientation
        return 1
    elif val < 0:

        # Counterclockwise orientation
        return 2
    else:

        # Collinear orientation
        return 0


def do_intersect(line1: Line, line2: Line):
    # Find the 4 orientations required for
    p1 = line1.point1
    q1 = line1.point2
    p2 = line2.point1
    q2 = line2.point2
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases

    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if (o1 == 0) and onSegment(p1, p2, q1):
        return True

    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if (o2 == 0) and onSegment(p1, q2, q1):
        return True

    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if (o3 == 0) and onSegment(p2, p1, q2):
        return True

    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if (o4 == 0) and onSegment(p2, q1, q2):
        return True

    # If none of the cases
    return False


def is_point_on_line(linePointA, linePointB, point):
    print(linePointA.x, linePointB.x, point.x)
    a = (linePointB.y - linePointA.y) / (linePointB.x - linePointB.x)
    b = linePointA.y - a * linePointA.x
    if fabs(point.y - (a * point.x + b)) < float_info.epsilon:
        return True
    return False


def is_between(a, b, c):
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > float_info.epsilon:
        return False

    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y) * (b.y - a.y)
    if dotproduct < 0:
        return False

    squaredlengthba = (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y)
    if dotproduct > squaredlengthba:
        return False

    return True


def point_regards_line(point: Point, line: Line):
    v1 = (line.point2.x - line.point1.x, line.point2.y - line.point1.y)  # Vector 1
    v2 = (line.point2.x - point.x, line.point2.y - point.y)  # Vector 2
    xp = v1[0] * v2[1] - v1[1] * v2[0]  # Cross product
    if xp > 0:
        return 1
    elif xp < 0:
        return -1
    else:
        return 0


def is_equal_point(point1, point2):
    if point1.x == point2.x and point1.y == point2.y:
        return True
    return False


def line_inside_rectangle(line: Line, rect: Rectangle):
    if point_inside_rectangle(line.point1, rect) and point_inside_rectangle(line.point2, rect):
        return True
    return False


def point_inside_rectangle(point: Point, rect: Rectangle):
    if rect.horizontal_line1.point1.x < point.x < rect.horizontal_line2.point2.x:
        if rect.vertical_line1.point1.y < point.y < rect.vertical_line2.point2.y:
            return True
    return False
