from flask import Flask, jsonify, request

from database import JsonDB

app = Flask(__name__)

# Initialize JSON database
db = JsonDB("db.json")


@app.route("/<resource>", methods=["GET", "POST"])
@app.route("/<resource>/<id>", methods=["GET", "PUT", "DELETE"])
def handle_resource(resource, id=None):
    if id is None:
        if request.method == "GET":
            return jsonify(db.find_all(resource))

        elif request.method == "POST":
            item = request.json
            if db.save(resource, item):
                return jsonify(item), 201
            return "Cannot create with an id.", 400

    else:
        try:
            id = int(id)
        except ValueError:
            return "Invalid path.", 404

        if request.method == "GET":
            result = db.find_one(resource, id)
            if result is None:
                return "", 404
            return jsonify(result)

        elif request.method == "PUT":
            item = request.json

            if "id" in item and item["id"] != id:
                return "ids do not match.", 400

            if db.save(resource, item):
                return "", 204

            return "", 404

        elif request.method == "DELETE":
            if db.delete(resource, id):
                return "", 204
            return "", 404

    return "Method not allowed", 405


if __name__ == "__main__":
    app.run(debug=True)
