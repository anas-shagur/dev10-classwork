import console_io as cio
import mysql.connector
from data import EmployeeRepository
from dynaconf import Dynaconf
from rich.console import Console
from rich.table import Table


def build_connection():
    settings = Dynaconf(
        envvar_prefix=False,
        settings_files=["settings.toml"],
    )
    return mysql.connector.connect(**settings.db)


def print_employees(employees):
    table = Table(title="Employees")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("First Name", style="magenta")
    table.add_column("Last Name", style="green")
    table.add_column("Start Date", style="yellow")
    table.add_column("End Date", style="yellow")

    for employee in employees:
        table.add_row(
            str(employee.employee_id),
            employee.first_name,
            employee.last_name,
            str(employee.start_date),
            str(employee.end_date),
        )

    console = Console()
    console.print(table)


def find_all(repository):
    employees = repository.find_all()
    print_employees(employees)


def find_by_id(repository):
    pass


def find_by_first_and_last_name(repository):
    pass


def find_by_last_name_contains(repository):
    pass


def add_employee(repository):
    pass


def update_employee(repository):
    pass


def delete_employee(repository):
    pass


def main():
    print("Gravel Family Employees")
    with EmployeeRepository(build_connection()) as repository:
        while True:
            print("0. Exit")
            print("1. Find All Employees")
            print("2. Find Employee by ID")
            print("3. Find Employee By First AND Last Name")
            print("4. Find Employee By Last Name Contains")
            print("5. Add Employee")
            print("6. Update Employee")
            print("7. Delete Employee")
            choice = cio.read_int("Select [0-7]: ", 0, 7)
            match choice:
                case 0:
                    break
                case 1:
                    find_all(repository)
                case 2:
                    find_by_id(repository)
                case 3:
                    find_by_first_and_last_name(repository)
                case 4:
                    find_by_last_name_contains(repository)
                case 5:
                    add_employee(repository)
                case 6:
                    update_employee(repository)
                case 7:
                    delete_employee(repository)
                case _:
                    print("I don't understand that selection.")


if __name__ == "__main__":
    main()
