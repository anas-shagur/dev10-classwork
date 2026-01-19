from dataclasses import asdict

import requests

from models import Player

class PlayerAPI:
    resource = "player"

    def __init__(self, api_url):
        self._api_url = api_url

    def find_all(self):
        response = requests.get(f"{self._api_url}/{self.resource}")
        response.raise_for_status()
        return [Player(**player) for player in response.json()]

    def find_one(self, player_id):
        response = requests.get(f"{self._api_url}/{self.resource}/{player_id}")
        if response.status_code == 404:
            return None
        return Player(**response.json())

    def post(self, player):
        response = requests.post(
            f"{self._api_url}/{self.resource}",
            json=asdict(player),
        )
        response.raise_for_status()
        return Player(**response.json())

    def put(self, player):
        response = requests.put(
            f"{self._api_url}/{self.resource}/{player.id}",
            json=asdict(player),
        )
        return response.status_code == 204

    def delete(self, player_id):
        response = requests.delete(f"{self._api_url}/{self.resource}/{player_id}")
        return response.status_code == 204