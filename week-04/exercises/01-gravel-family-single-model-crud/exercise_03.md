# Implement `find` methods.

1. Add `find_by_first_and_last_name` to our `EmployeeRepository`. Use `DatabaseContext.find_one`. Our SQL query should use `first_name = %s AND last_name = %s` to find a single employee.

2. In `main.py`, implement `find_by_first_and_last_name`.

    - Read the first name.
    - Read the last name.
    - Use `repository.find_by_first_and_last_name` to fetch one `Employee`.
    - Determine if the employee exists or doesn't.
    - If they exist, use `print_employees([employee])` to render a rich table.
    - If they don't, print a message.

3. Add `find_by_last_name_contains` to our `EmployeeRepository`. Use `DatabaseContext.find`. Our SQL query should use the `LIKE` condition: `last_name LIKE %s`. Though we'll need to inject wild cards in the front and back, like this: `f"%{last_snippet}%"`.

4. In `main.py`, implement `find_by_last_name_contains`.

    - Read the last name snippet.
    - Use the `repository.find_by_last_name_contains` to fetch multiple employees.
    - If `list[Employee]` is empty, print a message.
    - Otherwise, `print_employees(employees)`.