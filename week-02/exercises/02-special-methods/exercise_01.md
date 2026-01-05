# Exercise 01

1. Find the `blues_music_data.csv` in this directory.

2. Create a module named `spotify_extractor.py`.

3. Create a function and use the `csv` module to read from file. Do not print the results. The function's return value should be a list that contains either a dictionary, `csv.DictReader`, or a list, `csv.reader`.

    Relative paths can be tricky. That's why our `__file__` -- the current source file -- can be used to navigate the parent directory and join our blues data file.

    ```py
    import csv
    import os

    file_path = os.path.join(os.path.dirname(__file__), "blues_music_data.csv")
    ```

4. Create a file, `exercise_01.py`, import the `spotify_extractor` function, and print the results.