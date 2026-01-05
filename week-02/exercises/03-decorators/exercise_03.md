# Exercise 03

1. In `commerce_decorators.py`, add a validation decorator, `@validate_positive_result`, that validates positive `Decimal`s. It should focus exclusively on the `console_io.read_decimal` function.

    (I know, I know. We should just validate inside the `read_decimal` function, but this is for demonstration purposes only.)

2. We don't need to call the function only once. If the result is zero or less, we print an error:

    ```
    [ERR] Decimal should be a positive value.
    ```

    Then loop again.