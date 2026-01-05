# ETLProcessor.extract_sql

1. In `main.py`, change this code.

    ```py
     with engine.connect() as cnx, cnx.begin():
        processor = ETLProcessor(
            cnx,
            third_party_path,
            load_path,
            transformer,
        )
        processor.process()
    ```

2. In the `etl.py` module and `ETLProcessor.extract_sql` method, remove `pass`. Uncomment the `sql` variable and `pd.read_sql`. Copy and paste the SQL query from our first exercise.

3. In `ETLProcessor.extract`, remove the `pass` and uncomment `self.extract_sql`. Print the `DataFrame`.

    ```py
    def extract(self):
        df = self.extract_sql()
        print(df.head())
    ```

4. In `ETLProcessor.process`, remove the `pass` and uncomment `self.extract`.

5. Run `main.py`.