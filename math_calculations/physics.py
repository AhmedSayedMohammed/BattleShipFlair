from math_calculations.math_2d import do_intersect, is_between, is_equal_point, Point, line_inside_rectangle, Rectangle, \
    point_inside_rectangle, point_regards_line
from model.battle_ship import BattleShip, ShipStatus


def check_ships_collision(ships, border):
    for ship in ships:
        # check border collision
        if not check_ship_inside_border(ship, border):
            return False
        if check_collision_with_other_ships(ship, ships):
            return False
    return True


def check_collision_with_other_ships(current_ship, all_ships):
    for ship in all_ships:
        if ship == current_ship:
            continue

        collided = check_collision_another_ship(current_ship, ship)
        if collided:
            return True

    return False


def check_collision_another_ship(current_ship: BattleShip, other_ship: BattleShip):
    if do_intersect(current_ship.get_current_ship_body_position(), other_ship.get_current_ship_body_position()):
        return True
    return False


def check_shot_hits_ship(point: Point, all_ships, game_border):
    shot_point = point
    for ship in all_ships:
        # check shot out of bounds
        if not point_inside_rectangle(point, game_border):
            return False
        # check if it hits last piece of the ship
        if is_equal_point(shot_point, ship.get_current_ship_body_position().point2):
            if ship.get_status() == ShipStatus.SINK:
                return {"result": "HIT"}
            ship.set_status(ShipStatus.SINK)
            return {"result": "SINK"}
        if point_regards_line(shot_point, ship.get_current_ship_body_position()) == 0:
            return {"result": "HIT"}
    return {"result": "WATER"}


def check_ship_inside_border(ship: BattleShip, border: Rectangle):
    return line_inside_rectangle(ship.get_current_ship_body_position(), border)
