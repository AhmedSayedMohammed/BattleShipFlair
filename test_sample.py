import http
import unittest
from unittest import mock
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
shot = {
    "x": 6,
    "y": 7
}


class TestSampleClass(unittest.TestCase):
    gm = None
    physics = None

    def setUp(self):
        from manager.game_manager import GameManager
        from math_calculations import physics
        self.gm = GameManager.get_instance()
        self.physics = physics
        print("test started")

    def tearDown(self):
        self.gm = None
        print("test ended")

    def test_create_battleship_game(self):
        self.gm.start_game(ships)
        response = self.physics.check_ships_collision(self.gm.ships)
        self.assertEqual(response, http.HTTPStatus.BAD_REQUEST)

    def test_shot(self):
        response = self.physics.check_shot_hits_ship(shot, self.gm.ships)
        self.assertEqual(response, {"result": "WATER"})

    def test_delete_battleship_game(self):
        response = self.gm.end_game()
        self.assertTrue(response)


if __name__ == "__main__":
    unittest.main()
