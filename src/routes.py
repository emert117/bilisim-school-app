from flask import jsonify

from app import app
from app import db


@app.route("/", methods = ["GET"])
def index():
  return jsonify({"msg": "Hello world"})