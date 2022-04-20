from math_calculations.math_2d import Point, Rectangle, Line
from model.battle_ship import BattleShip, ShipStatus

h_line1 = Line(Point(0, 0), Point(9, 0))
h_line2 = Line(Point(0, 9), Point(9, 9))
v_line1 = Line(Point(0, 0), Point(0, 9))
v_line2 = Line(Point(9, 0), Point(9, 9))
game_border = Rectangle(h_line1, h_line2, v_line1, v_line2)


class GameManager:
    __instance__ = None
    ships = []

    def __init__(self):
        if GameManager.__instance__ is None:
            GameManager.__instance__ = self
        else:
            raise Exception("You cannot create another GameManager class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not GameManager.__instance__:
            GameManager()
        return GameManager.__instance__

    def start_game(self, ships):
        self.ships = ships

    def end_game(self):
        self.__instance__ = None
        self.ships = []
        return True
