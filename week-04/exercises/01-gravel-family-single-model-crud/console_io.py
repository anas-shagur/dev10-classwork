from datetime import datetime


def read_string(prompt):
    return input(prompt).strip()


def read_required_string(prompt):
    while True:
        value = read_string(prompt)
        if value:
            return value
        print("[ERR] Value is required.")


def read_int(prompt, min=-100_000, max=100_000):
    while True:
        try:
            value = int(read_required_string(prompt))
            if value < min or value > max:
                print(f"[ERR] Value must be between {min} and {max}.")
            return value
        except ValueError:
            print("[ERR] Value must be an integer.")


def read_date(prompt):
    while True:
        value = read_required_string(prompt)
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            print("[ERR] Date must be in the format YYYY-MM-DD.")
