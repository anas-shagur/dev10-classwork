# Exercise08

1. Add a new module named `string_functions`.

2. Add a function

    ```
    Name: starts_with_day_of_week
    Inputs: str
    Output: bool
    Description: return True if the parameters starts with a day of week abbreviation:
    Mon, Tues, Weds, Thurs, Fri, Sat, Sun
    or False if it doesn't
    ```

3. Create tests for starts_with_day_of_week and confirm the function is correct.

4. Add a function

    ```
    Name: contains_day_of_week
    Inputs: str
    Output: bool
    Description: return True if a day of week abbreviation occurs anywhere in the string
    or False if it doesn't
    ```

5. Create tests for contains_day_of_week and confirm the function is correct.

6. Add a function (stretch goal)

    ```
    Name: remove_vowel_from_between_x
    Inputs: str
    Output: str
    Description: Look for the pattern "x[any vowel]x" in a string. If you find it, remove the vowel.
    Return a new string with all the vowels between x removed.

    Examples:
    xox -> xx
    onexexx -> onexxx
    xerrex -> xerrex
    xuxxuxxux -> xxxxxx
    ```

 7. Create tests for remove_vowel_from_between_x and confirm the function is correct.