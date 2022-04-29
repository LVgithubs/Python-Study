# python -m pip install flask
# 환경변수 설정하지 않았을때 이용하기.
from distutils.log import debug

from flask import Flask, request, jsonify
import member_dao as dao
flask = Flask(__name__)


@flask.route("/my-member")
def list():
    return jsonify(dao.select_all)


@flask.route("/my-member/<id>")
def detail(id):
    return jsonify(dao.select_one(id=id))


@flask.route("/my-member/<id>", methods=['DELETE'])
def delete(id):
    return dao.delete_one(id=id)


@flask.route("/my-member/<id>", methods=['PUT'])
def update(id):
    # data = request.data  # x-www-form-urlencoded
    data = request.get_json()  # application/json
    return dao.update_one(id=id, username=data["username"], password=data["password"])


@flask.route("/my-member", methods=['POST'])
def save():
    data = request.get_json()
    return dao.insert_one(id=id, username=data["username"], password=data["password"])


flask.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)
