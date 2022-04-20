from math_calculations.math_2d import Point, Line, Rectangle
from enum import Enum


class ShipStatus(Enum):
    Floating = 1
    HIT = 2
    SINK = 3


class BattleShip:
    def __init__(self, x, y, direction, size, status: ShipStatus):
        self.x = x
        self.y = y
        self.size = size
        self.status = status
        self.direction = direction

    def get_current_ship_body_position(self) -> Line:
        if self.direction == "V":
            point1 = Point(self.x, self.y)
            point2 = Point(self.x, self.y + self.size)
            return Line(point1, point2)
        if self.direction == "H":
            point1 = Point(self.x, self.y)
            point2 = Point(self.x + self.size, self.y)
            return Line(point1, point2)


    def get_current_ship_body_positions(self) -> Rectangle:
        if self.direction == "V":
            point1 = Point(self.x+self.size, self.y+self.size)
            point2 = Point(self.x, self.y + self.size)
            return Line(point1, point2)
        if self.direction == "H":
            point1 = Point(self.x, self.y)
            point2 = Point(self.x + self.size, self.y)
            return Line(point1, point2)

    def set_status(self, status: ShipStatus):
        self.status = status
        pass

    def get_status(self) -> ShipStatus:
        return self.status
