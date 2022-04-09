from math_calculations.math_2d import Point
from model.battle_ship import BattleShip

h_dimension = Point(0, 9)
v_dimension = Point(0, 9)


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
        # convert ship json to BattleShip object
        ships_list = []
        for ship in ships:
            ships_list.append(BattleShip(ship))
        self.ships = ships_list

    def end_game(self):
        self.__instance__ = None
        self.ships = []
        return True
