from model.battle_ship import BattleShip, ShipStatus


def convert_json_to_ships(ships):
    # convert ship json to BattleShip object
    ships_list = []
    for ship in ships:
        ships_list.append(BattleShip(ship['x'], ship['y'], ship['direction'], ship['size'], ShipStatus.Floating))
    return ships_list
