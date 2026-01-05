import numpy as np
import scipy.stats as stats
from requests.exceptions import HTTPError
from rich.console import Console
from rich.table import Table

import console_io as cio
from book_api import BookAPI
from books import BookData

api = BookAPI("http://127.0.0.1:5000")


def choose_format():
    cio.print_header("Format")
    print("1. Hardcover")
    print("2. Paperback")
    print("3. eBook")
    match cio.read_int("Select [1-3]: ", 1, 3):
        case 1:
            return "Hardcover"
        case 2:
            return "Paperback"
        case 3:
            return "eBook"
        case _:
            return "Unknown"


def choose_menu():
    cio.print_header("Main Menu")
    print("0. Exit")
    print("1. List Books")
    print("2. Add Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Calculate Central Tendencies")

    return cio.read_int("Select [0-5]: ", 0, 5)


def add_book():
    cio.print_header("Add a Book")

    bd = BookData(
        author_name=cio.read_required_string("Author Name: "),
        title=cio.read_required_string("Book Title: "),
        publish_date=cio.read_required_string("Publish Date: "),
        format=choose_format(),
        price=cio.read_positive_float("Price: "),
    )

    created = api.post(bd)
    print(f"Book ID {created.id} created.")


def update_book():
    cio.print_header("Update a Book")
    book_id = cio.read_int("Book ID: ", 1, 1000000)
    book = api.get_one(book_id)
    if not book:
        print(f"Book ID {book_id} not found.")
        return

    book.author_name = (
        cio.read_string(f"Author Name [{book.author_name}]: ") or book.author_name
    )
    book.title = cio.read_string(f"Book Title [{book.title}]: ") or book.title
    book.publish_date = (
        cio.read_string(f"Publish Date [{book.publish_date}]: ") or book.publish_date
    )
    book.format = choose_format()
    book.price = cio.read_positive_float(f"Price [{book.price}]: ")

    success = api.put(book)
    if success:
        print(f"Book ID {book_id} updated.")
    else:
        print(f"Book ID {book_id} not updated.")


def delete_book():
    cio.print_header("Delete a Book")
    book_id = cio.read_int("Book ID: ", 1, 1000000)
    success = api.delete(book_id)
    if success:
        print(f"Book ID {book_id} deleted.")
    else:
        print(f"Book ID {book_id} not deleted.")


def print_books():
    table = Table(show_header=True, header_style="bold magenta", title="Books")
    table.add_column("ID", style="dim")
    table.add_column("Author")
    table.add_column("Title")
    table.add_column("Publish Date")
    table.add_column("Format")
    table.add_column("Price", justify="right")

    for book in api.get_all():
        table.add_row(
            str(book.id),
            book.author_name,
            f"[dark_orange]{book.title}[/dark_orange]",
            book.publish_date,
            book.format,
            f"[yellow1]${book.price:.2f}[/yellow1]",
        )

    console = Console()
    console.print(table)


def calculate_central_tendencies():
    cio.print_header("Central Tendencies")

    books = api.get_all()
    prices = [book.price for book in books]

    result = stats.describe(prices)

    print(f"Sample Size: {result.nobs}")
    print(f"Mean Price: {result.mean}")
    print(f"Median Price: {np.median(prices)}")
    print(f"Mode Price: {stats.mode(prices).mode}")
    print(f"Min Price: {result.minmax[0]}")
    print(f"Max Price: {result.minmax[1]}")
    print(f"Variance: {result.variance}")
    print(f"Skewness: {result.skewness}")
    print(f"Kurtosis: {result.kurtosis}")


def choose(choice):
    match choice:
        case 1:
            print_books()
        case 2:
            add_book()
        case 3:
            update_book()
        case 4:
            delete_book()
        case 5:
            calculate_central_tendencies()
        case _:
            print("Invalid choice. Please try again.")


def main():
    choice = choose_menu()
    while choice != 0:
        try:
            choose(choice)
        except HTTPError as e:
            print(f"HTTP Error: {e}")

        choice = choose_menu()

    cio.print_header("Goodbye")


if __name__ == "__main__":
    main()
