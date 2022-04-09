from http import HTTPStatus
from flask import Flask, jsonify, request
from manager.game_manager import GameManager
from math_calculations import physics

app = Flask(__name__)


@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    gm = GameManager.get_instance()
    gm.start_game(request.json['ships'])
    response = physics.check_ships_collision(gm.ships)
    return jsonify({'code': response}), response


@app.route('/battleship', methods=['PUT'])
def shot():
    shot_json = request.json
    gm = GameManager.get_instance()
    response = physics.check_shot_hits_ship(shot_json, gm.ships)
    return jsonify(response), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    gm = GameManager.get_instance()
    gm.end_game()
    return jsonify({}), HTTPStatus.OK
