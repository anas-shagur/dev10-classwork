from dataclasses import asdict

import requests

from books import BookData


class BookAPI:
    resource = "book"

    def __init__(self, api_url):
        self._api_url = api_url

    def get_all(self):
        response = requests.get(f"{self._api_url}/{self.resource}")
        response.raise_for_status()
        return [BookData(**book) for book in response.json()]

    def get_one(self, book_id):
        response = requests.get(f"{self._api_url}/{self.resource}/{book_id}")
        if response.status_code == 404:
            return None
        return BookData(**response.json())

    def post(self, book):
        response = requests.post(
            f"{self._api_url}/{self.resource}",
            json=asdict(book),
        )
        response.raise_for_status()
        return BookData(**response.json())

    def put(self, book):
        response = requests.put(
            f"{self._api_url}/{self.resource}/{book.id}",
            json=asdict(book),
        )
        return response.status_code == 204

    def delete(self, book_id):
        response = requests.delete(f"{self._api_url}/{self.resource}/{book_id}")
        return response.status_code == 204
