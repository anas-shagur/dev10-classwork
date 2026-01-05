# Create Notebook

1. You can either:

    - Create a Jupyter notebook in https://colab.research.google.com/.
    - or
    - Create a virtual environment, activate it, install Jupyter lab, Pandas, Matplotlib, etc, create a notebook in your virtual environment, and run `jupyter lab`.

    I recommend the prior.

    If something breaks, we can fix it, just like every notebook.

2. Upload `penguins.csv` from `04-matplotlib-penguins` to our Colab Files. (If you created a virtual environment, place it there.)

3. Add a code cell to import packages.

    ```py
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    ```

4. Add a code cell that loads `penguins.csv` as a DataFrame.

5. Confirm that it is working.

6. Remove na rows except for "sex".