import json
from decimal import Decimal

from commerce import Product


class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return obj.to_dict()
        return super().default(obj)


def product_decoder_hook(obj):
    if "id" in obj and "name" in obj and "price" in obj:
        return Product(obj["name"], Decimal(obj["price"]), int(obj["id"]))
    return obj


class ProductJsonSource:
    def __init__(self, file_path):
        self._file_path = file_path

    def grab_max_id(self, products):
        id = 0
        if len(products) > 0:
            id = max([product.id for product in products])
        return id + 1

    def find_products(self):
        try:
            with open(self._file_path, "r") as file:
                return json.load(file, object_hook=product_decoder_hook)
        except FileNotFoundError:
            return []

    def add(self, product):
        products = self.find_products()
        product.id = self.grab_max_id(products)
        products.append(product)
        self._write(products)

    def delete_by_id(self, id):
        products = self.find_products()
        original_length = len(products)

        products = [p for p in products if p.id != id]
        deleted_length = len(products)

        if original_length != deleted_length:
            self._write(products)
        return original_length != deleted_length

    # "protected" / weak private method
    def _write(self, products):
        with open(self._file_path, "w") as file:
            json.dump(products, file, cls=ProductEncoder)
