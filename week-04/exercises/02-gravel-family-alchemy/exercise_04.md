# Session Create, Update, Delete

1. In `main.py`, between engine creation and disposal, use a `with` statement and `Session`.

2. Add an employee. Confirm that the employee_id was auto-generated.

3. Select from projects with a project_id of 1. Use `session.scalars(stmt).one()`.

    Add that fresh employee to the project. 
    
    Confirm with `print(project)` and `print(project.employees)`.

4. Update that employee. If the employee is still in the session, set their attributes, and `session.commit()`. If they're not in the session, fetch them, set their attributes, and `session.commit()`.

5. Fetch project id 1. Remove that employee from `Project.employees`. Commit.

    That removes the `project_employee` bridge table. Confirm by printing `Project.employees`.

6. Delete that employee.

## Additional Create, Update, Delete

If you're up for it, choose some additional creates, updates, and deletes. Make a decision. Experiment.