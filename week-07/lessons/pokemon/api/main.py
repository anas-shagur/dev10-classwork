from dataclasses import asdict

from flask import Flask, jsonify, request
from models import find_all

app = Flask(__name__)


@app.route("/pokemon", methods=["GET"])
def handle_resource():
    page = 1
    if "page" in request.args:
        try:
            page = int(request.args["page"])
        except ValueError:
            pass

    if request.method == "GET":
        pokemons = find_all(page)

        if len(pokemons) == 0:
            return "", 204

        result = [asdict(pokemon) for pokemon in pokemons]
        return jsonify(result)

    return "Method not allowed", 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
