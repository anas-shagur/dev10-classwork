# Create a virtual environment and install packages.

1. We will need to create a virtual environment in the `week-04/exercises` directory, not `01-gravel-family-single-model-crud`. Some PyPI packages take up a lot of space, so it's better to use them sparingly. (If you have a lot of disk space, do what you want.)

2. Open a terminal either in VS Code or an app. Navigate (`cd`) to `week-04/exercises`. Execute this command:

    ```sh
    $ python -m venv .
    ```

3. Activate your virtual environment.

4. Install the [mysql-connector-python](https://pypi.org/project/mysql-connector-python/): `pip install mysql-connector-python`.

5. Install [dynaconf](https://pypi.org/project/dynaconf/): `pip install dynaconf`

6. Install [rich](https://pypi.org/project/rich/): `pip install rich`