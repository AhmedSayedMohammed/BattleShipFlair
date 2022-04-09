from math_calculations.math_2d import Point


class BattleShip:
    point1 = Point(0, 0)
    point2 = Point(0, 0)
    size = int()
    direction = str()
    status = ""

    def __init__(self, ship_json):
        x = int(ship_json['x'])
        y = int(ship_json['y'])

        size = int(ship_json['size'])
        direction = ship_json['direction']
        self.size = ship_json['size']
        self.direction = ship_json['direction']
        if direction == "V":
            self.point1.x = x
            self.point1.y = y
            self.point2.x = x
            self.point2.y = y + size
        if direction == "H":
            self.point1.x = x
            self.point1.y = y
            self.point2.x = x + size
            self.point2.y = y
