# Student `DataFrame`

You can choose. 

1. Use the Python REPL. Walk through `exercise_03.py` comments/instructions step by step.

    Benefits: we can noodle with things, be playful. Our REPL doesn't require `print`. It prints it for us.

    ```sh
    (exercises) 03-pandas-students % python
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pandas as pd
    >>> import ast
    >>> from collections import namedtuple
    >>> from datetime import datetime
    >>> df = pd.read_csv("students.csv")
    >>> df["registrations"] = df["registrations"].apply(ast.literal_eval)
    >>> df.info()
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1005 entries, 0 to 1004
    Data columns (total 9 columns):
    #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
    0   first_name     1000 non-null   object 
    1   last_name      1000 non-null   object 
    2   email          1000 non-null   object 
    3   birth_date     1003 non-null   object 
    4   country        1003 non-null   object 
    5   gpa            1003 non-null   float64
    6   major          1005 non-null   object 
    7   iq             1005 non-null   int64  
    8   registrations  1005 non-null   object 
    dtypes: float64(1), int64(1), object(7)
    memory usage: 70.8+ KB
    >>> 
    ```

2. Use VS Code. _File_ -&gt; _Open Folder_, `week-04/exercises/03-pandas-students`, and run `exercise_03.py`. Write code for comments/instructions step by step. Use the `print` function to display results.

    Benefits: we can debug and confirm results.

## Complex Exercises

You don't need to go through absolutely every exercise. The examples in the lessons don't map to the exercises. [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html) is complex and we don't need to know everything about it.

But... if you're up for it, try to solve a problem with a new Pandas method. Github Copilot might be of use.