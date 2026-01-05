class Product:
    def __init__(self, name, price, id=0):
        self._name = name
        self._price = price
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return f"{self._id} {self._name} {self._price:.2f}"

    def __repr__(self):
        return f"Product({self._id}, {self._name}, {self._price:.2f})"

    def __eq__(self, other):
        return (
            self._id == other._id
            and self._name == other._name
            and self._price == other._price
        )

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": float(self._price),
        }
