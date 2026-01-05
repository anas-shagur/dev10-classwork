# Session Reads

Ponder the `models.py` module. The `gravel_family` schema largely maps to SQLAlchemy models. The only difference is that there's a bridge table,

```py
project_employee = Table(
    "project_employee",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("project.project_id"), primary_key=True),
    Column(
        "employee_id", Integer, ForeignKey("employee.employee_id"), primary_key=True
    ),
)
```

that connects `Project.employees` and `Employee.projects`.

1. In `main.py`, between engine creation and disposal, use a `with` statement and `Session`.

2. Print all employees. Prefer `session.scalars(stmt)` over `session.execute(stmt)`. The `scalars` method iterates through `Employee` objects. The `execute` method iterates through a tuple of employees: `(Employee,)`.

3. Print customers whose last name starts with "Gr".

4. Print all project whose start date is in July 2019. (We can't use an `and` for that, we need to use `sqlalchemy.and_`.)

    ```py
    stmt = select(Project).where(
        and_(
            Project.start_date >= date(2019, 7, 1),
            Project.start_date <= date(2019, 7, 31),
        )
    )
    ```

5. Print all items whose unit's name is "Cubic Yard". We'll need to use `join`.

    ```py
    stmt = select(Item).join(Unit).where(Unit.name == "Cubic Yard")
    ```

6. Print all projects whose customer first name starts with "Je". (We can't directly access the project's customer. We need the `has` method to generate our SQL.)

    ```py
    stmt = select(Project).where(
        Project.customer.has(Customer.first_name.startswith("Je"))
    )
    ```

## Additional Selects

If you're up for it, choose some additional selects. Make a decision. Experiment.