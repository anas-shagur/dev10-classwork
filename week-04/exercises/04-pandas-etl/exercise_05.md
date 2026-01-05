# Testing

100% Optional!

1. Activate your `dev10-classwork/week-04/exercises/` virtual environment.

2. Install [pytest](https://pypi.org/project/pytest/): `pip install pytest`.

3. Add a test module, `/04-pandas-etl/test_etl.py`, and include this code.

    ```py
    def test_func():
        assert 33 == 42

    class TestClass:
        def test_method(self):
            assert 33 == 42

        def test_other_method(self):
            assert "one" == "one"
    ```

4. Browse to `week-04/exercises/04-pandas-etl` and run `pytest` in the terminal.

    ```sh
    (exercises) $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
    rootdir: /week-04/exercises/04-pandas-etl
    collected 3 items                                                              

    test_etl.py FF.                                                          [100%]

    =================================== FAILURES ===================================
    __________________________________ test_func ___________________________________

        def test_func():
    >       assert 33 == 42
    E       assert 33 == 42

    test_etl.py:2: AssertionError
    ____________________________ TestClass.test_method _____________________________

    self = <test_etl.TestClass object at 0x103460910>

        def test_method(self):
    >       assert 33 == 42
    E       assert 33 == 42

    test_etl.py:7: AssertionError
    =========================== short test summary info ============================
    FAILED test_etl.py::test_func - assert 33 == 42
    FAILED test_etl.py::TestClass::test_method - assert 33 == 42
    ========================= 2 failed, 1 passed in 0.03s ==========================
    ```

5. Remove the `test_func` and `TestClass`.

6. Create limited test data and keep it simple. Confirm the data with transformation steps.

7. Instantiate an `ETLProcessor`. Use `MagicMock` to mock the `extract_sql` and `extract_csv` methods.

8. Add a test class that tests the `Transformer` and confirms its methods.

9. Add a test class that tests the `ETLProcessor` and confirms its methods.