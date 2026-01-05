# Create a SQLAlchemy Engine

1. In `02-gravel-family-alchemy/.env`, set your local MySQL credentials to the appropriate values.

2. In `main.py`, use Dynaconf settings.

3. In `main.py`, create a SQLAlchemy engine with the `create_engine` function, passing in the settings ENGINE_URL.

4. Print the engine: `print(engine)`. The output should look similar to this:

    ```sh
    Engine(mysql+mysqlconnector://username:***@localhost:3306/gravel_family)
    ```

5. Shut down the engine with: `engine.dispose()`.