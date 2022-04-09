import http
from manager.game_manager import h_dimension, v_dimension
from math_calculations.math_2d import doIntersect, is_between, is_equal_point, Point


def check_ships_collision(ships=None):
    for ship in ships:
        if check_collision_with_other_ships(ship, ships):
            return http.HTTPStatus.BAD_REQUEST
        # check border collision
        if doIntersect(ship.point1, ship.point2, h_dimension, v_dimension):
            return http.HTTPStatus.BAD_REQUEST
    return http.HTTPStatus.OK


def check_collision_with_other_ships(current_ship, all_ships):
    for ship in all_ships:
        if ship == current_ship:
            continue

        collided = check_collision_another_ship(current_ship, ship)
        if collided:
            return True

    return False


def check_collision_another_ship(current_ship, other_ship):
    if doIntersect(current_ship.point1, current_ship.point2, other_ship.point1, other_ship.point2):
        return True
    return False


def check_shot_hits_ship(shot, all_ships):
    for ship in all_ships:
        # check if it hits last piece of the ship
        shot_point = Point(shot['x'], shot['y'])
        if is_equal_point(shot_point, ship.point1) or is_equal_point(shot_point, ship.point2):
            ship.status = "SINK"
            return {"result": "SINK"}

        if is_between(shot_point, ship.point1, ship.point2):
            return {"result": "HIT"}
    return {"result": "WATER"}
