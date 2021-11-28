from flask import jsonify, request, Response

from app import app
from app import db
from database import DataObject


@app.route("/", methods = ["GET"])
def index():
  if request.method == "GET":
    items = db.get_all()
    return jsonify({"items": items})

  else:
    Response("Method is not allowed", status = 400)


@app.route("/add", methods = ["POST"])
def add():
  if request.method == "POST":
    try:
      data = request.get_json()
      obj = DataObject(data = data)
      db.add(obj)
      
      return Response("Data has been added", status = 200)

    except:
      return Response("Error occured", status = 500)

  else:
    return Response("Method not allowed", status = 400)


@app.route("/update", methods = ["POST"])
def update():
  if request.method == "POST":
    try:
      data = request.get_json()
      index = data["index"]
      new_data = data["new-data"]
      
      db.update(index = index, new_data = new_data)
      
      return Response("Data successfully updated", status = 200)
    
    except:
      return Response("Error occured", status = 500)

  else:
    Response("Method not allowed", status = 400)


@app.route("/delete", methods = ["POST"])
def delete():
  if request.method == "POST":
    try:
      data = request.get_json()
      index = data["index"]
      
      db.update(index = index)
      
      return Response("Data successfully deleted", status = 200)
    
    except:
      return Response("Error occured", status = 500)

  else:
    Response("Method not allowed", status = 400)