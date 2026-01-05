# ETLProcessor.extract_csv

1. In `ETLProcessor.extract_csv`, remove `pass` and uncomment our `pd.read_csv`.

2. In `ETLProcessor.extract`, remove `print(df.head())`. Uncomment `self.extract_csv`. Combine the `DataFrame`s using `pd.concat`.

3. In `ETLProcessor.process`, print the `DataFrame` head and tail. Print the count.

4. Run `main.py`.