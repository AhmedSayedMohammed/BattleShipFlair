from http import HTTPStatus
from flask import Flask, jsonify, request
from manager.game_manager import GameManager, game_border
from manager.mapper import convert_json_to_ships
from math_calculations import physics
from math_calculations.math_2d import Point

app = Flask(__name__)


@app.route('/battleship', methods=['POST'])
def create_battleship_game():

    ships = convert_json_to_ships(request.json['ships'])
    response = physics.check_ships_collision(ships, game_border)
    if not response:
        return jsonify({'code': HTTPStatus.BAD_REQUEST}), HTTPStatus.BAD_REQUEST
    gm = GameManager.get_instance()
    gm.start_game(ships)
    return jsonify({'code': HTTPStatus.OK}), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    shot_json = request.json
    shot_pint = Point(shot_json['x'], shot_json['y'])
    gm = GameManager.get_instance()
    response = physics.check_shot_hits_ship(shot_pint, gm.ships, game_border)
    if not response:
        return jsonify(HTTPStatus.BAD_REQUEST), HTTPStatus.BAD_REQUEST
    return jsonify(response), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    gm = GameManager.get_instance()
    gm.end_game()
    return jsonify({}), HTTPStatus.OK
