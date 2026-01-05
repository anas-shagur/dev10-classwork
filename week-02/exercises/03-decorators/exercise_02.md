# Exercise 02

1. Create a Python module named `commerce_decorators.py`.

2. Implement a `@log` decorator, though instead of printing logs to standard out, log to a file. The file name should be `products.log`. It's a text file. 

    The `log` decorator should capture:
    - a timestamp: `datetime.now().isoformat()`
    - the function's name: `func.__name__`
    - all positional arguments
    - all keyword arguments
    - the function's return value

    The format should be similar to this:

    ```py
    f"{datetime.now().isoformat()} {func.__name__} with args {args} and kwargs {kwargs} returned {result}\n"
    ```

3. Add `@log` decorators to the `console_io.py` functions. Run `main.py`.

4. Add `@log` decorators to our `ProductJsonSource` methods. Run `main.py`.

4. Add `@log` decorators to our `main.py` functions. Run `main.py`.

    Do not add `@log` to our `Product` methods (though maybe you play with it?). That would likely be a lot.