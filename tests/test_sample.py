import http
import unittest

from manager.game_manager import GameManager
from math_calculations import physics

ships = [
    {
        "x": 2,
        "y": 1,
        "size": 4,
        "direction": "H"
    },
    {
        "x": 7,
        "y": 4,
        "size": 3,
        "direction": "V"
    },
    {
        "x": 3,
        "y": 5,
        "size": 2,
        "direction": "V"
    },
    {
        "x": 6,
        "y": 8,
        "size": 1,
        "direction": "H"
    }
]


class TestSampleClass(unittest.TestCase):

    def test_should_fail(self):
        self.fail('You should remove this test')

    def test_create_game(self):
        gm = GameManager.get_instance()
        gm.start_game(ships)
        response = physics.check_ships_collision(gm.ships)
        self.assertEqual(response, http.HTTPStatus.OK)

    def test_shot(self):
        shot = {
            "x": 6,
            "y": 7
        }
        gm = GameManager.get_instance()
        response = physics.check_shot_hits_ship(shot, gm.ships)
        self.assertEqual(response, {"result": "WATER"})

    def test_delete_game(self):
        gm = GameManager.get_instance()
        response = gm.end_game()
        self.assertEqual(response, True)


if __name__ == "__main__":
    print("hhhhh")
    unittest.main()
