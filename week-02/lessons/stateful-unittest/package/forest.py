class NationalForest:
    def __init__(self, name, location, acres):
        self._name = name
        self._location = location
        self._acres = acres

    @property
    def acres(self):
        return self._acres

    @acres.setter
    def acres(self, acres):
        if acres < 0:
            raise ValueError("Acres must be greater than 0")
        self._acres = acres

    def get_square_kilometers(self):
        return round(self._acres / 247.1, 2)


if __name__ == "__main__":
    forest = NationalForest("Dixie", "Utah", 123)
    print(forest.get_square_kilometers())  # 0.5

    forest.acres = 500000
    print(forest.get_square_kilometers())  # 2023.47

    forest.acres = 1885655
    print(forest.get_square_kilometers())  # 7631.14
