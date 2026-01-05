import json
from pathlib import Path


class JsonDB:
    """
    This class only supports dictionaries.
    """

    def __init__(self, db_file_path):
        self._db_file_path = db_file_path
        self._data = {}
        self.load()

    def load(self):
        if Path(self._db_file_path).exists():
            with open(self._db_file_path, "r") as f:
                self._data = json.load(f)
        else:
            self.write()

    def write(self):
        with open(self._db_file_path, "w") as f:
            json.dump(self._data, f, indent=2)

    def save(self, resource, item):
        # add
        if "id" not in item or item["id"] is None or item["id"] == 0:
            if resource not in self._data:
                self._data[resource] = []
                item["id"] = 1
            else:
                item["id"] = self._data[resource][-1]["id"] + 1

            self._data[resource].append(item)
        else:  # update
            found = False

            if resource not in self._data:
                return False

            for i, elem in enumerate(self._data[resource]):
                if elem["id"] == item["id"]:
                    found = True
                    self._data[resource][i] = item
                    break

            if not found:
                return False

        self.write()
        return True

    def find_all(self, resource):
        if resource not in self._data:
            return []
        return self._data.get(resource)

    def find_one(self, resource, id):
        if resource not in self._data:
            return None
        return next((item for item in self._data[resource] if item["id"] == id), None)

    def delete(self, resource, id):
        if resource not in self._data:
            return False

        found = False
        for i, elem in enumerate(self._data[resource]):
            if elem["id"] == id:
                del self._data[resource][i]
                found = True
                if len(self._data[resource]) == 0:
                    del self._data[resource]
                break

        if found:
            self.write()
            return True
        else:
            return False
