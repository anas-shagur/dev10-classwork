# Existing EmployeeRepository Methods

We will use the `gravel_family` schema, specifically the `employee` table.

If you removed that schema, re-add it by executing `week-03/exercises/gravel-family-schema-data.sql` in MySQL Workbench.

1. In `settings.toml`, set your credentials to your local MySQL server.

2. Use existing `EmployeeRepository` methods: `find_by_id` and `update`.

3. In `main.py`, implement `find_by_id`.

    - Read an employee id.
    - Use the repository to fetch one `Employee`.
    - Determine if the employee exists or doesn't.
    - If they exist, use `print_employees([employee])` to render a rich table.
    - If they don't, print a message.

4. In `main.py`, implement `update_employee`.

    - Read an employee id.
    - Use the repository to fetch one `Employee`.
    - Determine if the employee exists or doesn't.
    - If they don't, print a message.
    - If they exist, update attributes with `console_io` methods.
    - Use the repository to update an `Employee`.
    - Our `repository.update` returns a row count. If the row count is 1, it's a success. If the row count is 0, it's a failure.