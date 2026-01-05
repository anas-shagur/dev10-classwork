import os

import console_io as cio
from commerce import Product
from data_sources import ProductJsonSource

file_path = os.path.join(os.path.dirname(__file__), "products.json")


class Controller:
    def __init__(self, file_path):
        self._source = ProductJsonSource(file_path)

    def add_product(self):
        cio.print_header("Add Product")
        name = cio.read_required_string("Product name: ")
        price = cio.read_decimal("Product price: ")
        product = Product(name, price)
        self._source.add(product)
        print("Success!")

    def delete_product(self):
        cio.print_header("Delete Product")
        id = cio.read_int("Product Id: ")
        if self._source.delete_by_id(id):
            print("Success!")
        else:
            print("Product not found.")

    def print_products(self):
        cio.print_header("Products")
        for product in self._source.find_products():
            print(product)

    def run(self):
        choice = -1
        while choice != 0:
            choice = self.choose_menu()
            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.print_products()
            elif choice == 3:
                self.delete_product()
            elif choice == 0:
                pass
            else:
                print("Invalid choice.")

        cio.print_header("Goodbye!")

    def choose_menu(self):
        cio.print_header("Main Menu")
        print("0. Exit")
        print("1. Add Product")
        print("2. List Products")
        print("3. Delete Product")
        return cio.read_int("Select [0-3]: ", 0, 3)


def main():
    controller = Controller(file_path)
    controller.run()


if __name__ == "__main__":
    main()
