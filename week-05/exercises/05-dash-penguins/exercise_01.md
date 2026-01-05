# Create a virtual environment

1. Create a virtual environment inside `05-dash-penguins`.

    ```sh
    $ python -m venv .
    ```

2. Activate it.

3. Install.

    ```sh
    (05-dash-penguins) $ pip install pandas dash dash_daq statsmodels
    ```

    We won't use our database drivers since it's only file-based.

4. In VS Code, open `05-dash-penguins`.

5. Select our `('05-dash-penguins': venv)`.

6. Run `app.py`.