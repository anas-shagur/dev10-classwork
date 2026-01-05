# Create and Delete

1. Add a create or insert method to `EmployeeRepository`. Use `DatabaseContext.insert` to send a query and parameters. We don't want to set the `employee_id`. The auto-generated id will be returned to us.

    ```py
    sql = """
    INSERT INTO employee (first_name, last_name, start_date, end_date)
    VALUES (%s, %s, %s, %s);
    """
    ```

2. In `main.py`, implement `add_employee`.

    - Read the first name, last name, and start date. We don't need the end date since our employee is recently employed.
    - Instantiate an `Employee`.
    - Create/insert an `Employee` to the `EmployeeRepository`.
    - Return the last id. Is the last id accurate?

3. Add a delete method to `EmployeeRepository`. Use `DatabaseContext.update`. We can either use an employee id or first AND last name to delete a record.

    Warning: If there's an existing employee with projects, things might go poorly. We could delete the many-to-many bridge table `project_employee` or we could check that a project exists and then reject the delete. (That's the same as an `Integrity` exception, which we could handle...)

4. In `main.py`, implement `delete_employee`.

    - Read either an employee id or first name AND last name.
    - Use the repository to delete.
    - If you chose deleting `project_employee`, don't handle the exception. If you focused on only deleting an employee, handle the `mysql.connector.IntegrityError`.
    - If the row count is 1, it's a success. If the row count is 0, it's a failure.