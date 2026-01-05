import os
import sqlite3

from flask import Flask, g, jsonify, request

app = Flask(__name__)
DATABASE = "people.db"

FAVORITE_FOOD = os.environ.get("FAVORITE_FOOD")


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route("/person", methods=["GET", "POST"])
@app.route("/person/<id>", methods=["GET", "PUT", "DELETE"])
def handle_resource(id=None):
    if id is None:
        if request.method == "GET":
            cursor = get_db().cursor()
            cursor.execute("SELECT * FROM person")
            result = cursor.fetchall()

            if len(result) == 0:
                cursor.close()
                return "", 204

            result = [
                dict(zip([key[0] for key in cursor.description], row)) for row in result
            ]

            if FAVORITE_FOOD:
                result = [
                    {**person, "favorite_food": FAVORITE_FOOD} for person in result
                ]

            cursor.close()

            return jsonify(result)

        elif request.method == "POST":
            person = request.json
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO person
                (username, email, name)
                VALUES (?, ?, ?)""",
                (
                    person["username"],
                    person["email"],
                    person["name"],
                ),
            )

            conn.commit()
            last_id = cursor.lastrowid
            cursor.close()

            person["person_id"] = last_id

            if last_id:
                return jsonify(person), 201
            return "Cannot create with an id.", 400

    else:
        try:
            id = int(id)
        except ValueError:
            return "Invalid path.", 404

        if request.method == "GET":
            cursor = get_db().cursor()
            cursor.execute("SELECT * FROM person WHERE person_id = ?", (id,))
            result = cursor.fetchone()

            if result is None:
                cursor.close()
                return "", 404

            result = dict(zip([key[0] for key in cursor.description], result))

            if FAVORITE_FOOD:
                result = {**result, "favorite_food": FAVORITE_FOOD}

            cursor.close()

            return jsonify(result)

        elif request.method == "PUT":
            person = request.json

            if "person_id" in person and person["person_id"] != id:
                return "ids do not match.", 400

            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE person SET 
                username = ?, email = ?, name = ?
                WHERE person_id = ?""",
                (
                    person["username"],
                    person["email"],
                    person["name"],
                    person["person_id"],
                ),
            )
            conn.commit()
            row_count = cursor.rowcount
            cursor.close()

            if row_count > 0:
                return "", 204

            return "", 404

        elif request.method == "DELETE":
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM person WHERE person_id = ?", (id,))
            conn.commit()
            row_count = cursor.rowcount
            cursor.close()
            if row_count > 0:
                return "", 204
            return "", 404

    return "Method not allowed", 405


@app.teardown_appcontext
def close_connection(_):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
