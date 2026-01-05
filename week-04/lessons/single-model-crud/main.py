import console_io as cio
import mysql.connector
from data import CustomerRepository
from dynaconf import Dynaconf
from models import Customer
from rich.console import Console
from rich.table import Table


def build_connection():
    settings = Dynaconf(envvar_prefix="DB", load_dotenv=True)
    return mysql.connector.connect(
        host=settings.HOST,
        port=settings.PORT,
        user=settings.USER,
        password=settings.PASSWORD,
        database=settings.DATABASE,
    )


def print_customers(customers):
    table = Table(title="Customers")
    table.add_column("First Name", style="magenta")
    table.add_column("Last Name", style="green")
    table.add_column("Street Address", style="cyan")
    table.add_column("City", style="blue")
    table.add_column("State", style="yellow")
    table.add_column("Email", style="red")
    table.add_column("Phone", style="salmon1")

    for customer in customers:
        table.add_row(
            customer.first_name,
            customer.last_name,
            customer.street_address,
            customer.city,
            customer.state,
            customer.email_address,
            customer.phone,
        )

    console = Console()
    console.print(table)


def list_customers(repository):
    print_customers(repository.find_all())


def find_by_last_name_prefix(repository):
    print("Find by Last Name Prefix")
    prefix = cio.read_required_string("Enter last name prefix: ")
    print_customers(repository.find_by_last_name_begins_with(prefix))


def find_customer_by_id(repository):
    print("Find Customer by ID")
    customer_id = cio.read_required_string("Enter customer ID: ")
    customer = repository.find_by_id(customer_id)
    if customer:
        print_customers([customer])
    else:
        print(f"Customer with ID {customer_id} not found.")


def find_customer_by_email(repository):
    print("Find Customer by Email")
    email = cio.read_required_string("Enter customer email: ")
    customer = repository.find_by_email(email)
    if customer:
        print_customers([customer])
    else:
        print(f"Customer with email {email} not found.")


def add_customer(repository):
    print("Add Customer")
    first_name = cio.read_required_string("First name: ")
    last_name = cio.read_required_string("Last name: ")
    street_address = cio.read_required_string("Street address: ")
    city = cio.read_required_string("City: ")
    state = cio.read_required_string("State: ")
    zip_code = cio.read_required_string("Zip code: ")
    email_address = cio.read_required_string("Email address: ")
    phone = cio.read_required_string("Phone: ")
    date_added = cio.read_date("Date added: ")
    reward_points = cio.read_int("Reward points: ", 0)

    customer = Customer(
        None,
        first_name,
        last_name,
        street_address,
        city,
        state,
        zip_code,
        email_address,
        phone,
        date_added,
        reward_points,
    )

    repository.insert(customer)


def update_customer(repository):
    print("Update Customer")
    email = cio.read_required_string("Enter customer email: ")
    customer = repository.find_by_email(email)
    if not customer:
        print(f"Customer with email {email} not found.")
        return

    customer.first_name = (
        cio.read_string(f"First name [{customer.first_name}]: ") or customer.first_name
    )
    customer.last_name = (
        cio.read_string(f"Last name [{customer.last_name}]: ") or customer.last_name
    )
    customer.street_address = (
        cio.read_string(f"Street address [{customer.street_address}]: ")
        or customer.street_address
    )
    customer.city = cio.read_string(f"City [{customer.city}]: ") or customer.city
    customer.state = cio.read_string(f"State [{customer.state}]: ") or customer.state
    customer.zip_code = (
        cio.read_string(f"Zip code [{customer.zip_code}]: ") or customer.zip_code
    )
    customer.phone = cio.read_string(f"Phone [{customer.phone}]: ") or customer.phone
    customer.reward_points = cio.read_int(
        f"Reward points [{customer.reward_points}]: ", 0
    )

    result = repository.update(customer)
    print(f"Customer updated: {result}")


def delete_customer(repository):
    print("Delete Customer")
    email = cio.read_required_string("Enter customer email: ")
    result = repository.delete_by_email(email)
    if result:
        print("Customer deleted.")
    else:
        print(f"Customer with email {email} not found.")


def main():
    print("Bowls Customers")
    with CustomerRepository(build_connection()) as repository:
        while True:
            print("0. Exit")
            print("1. List customers")
            print("2. Find by last name prefix")
            print("3. Find customer by ID")
            print("4. Find customer by email")
            print("5. Add a customer")
            print("6. Update a customer")
            print("7. Delete a customer")
            choice = cio.read_int("Select [0-7]: ", 0, 7)
            match choice:
                case 1:
                    list_customers(repository)
                case 2:
                    find_by_last_name_prefix(repository)
                case 3:
                    find_customer_by_id(repository)
                case 4:
                    find_customer_by_email(repository)
                case 5:
                    add_customer(repository)
                case 6:
                    update_customer(repository)
                case 7:
                    delete_customer(repository)
                case _:
                    break


if __name__ == "__main__":
    main()
