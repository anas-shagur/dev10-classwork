# Exercise 01

1. Run the `main.py` Python script. Play around with the menu and select options:

    ```
    Main Menu
    =========
    0. Exit
    1. Add Product
    2. List Products
    3. Delete Product
    Select [0-3]: 
    ```

2. Inspect the `commerce` module (contains the `Product` class). Inspect the `console_io` module (contains standard input functions). 

3. Inspect the `data_sources` module. The `ProductJsonSource` class is flexible. It can use any file path and reads and writes `Product`s from a JSON file. The `Product` class can't read and write JSON on its own. We need a JSON encoder and decoder to do it for us.

4. Inspect the `main` module. It contains a `Controller` class. The controller (https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) mediates between the user interface and data storage.

5. Debug!