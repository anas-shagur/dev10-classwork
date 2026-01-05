import decimal


def print_header(title):
    print(f"\n{title}")
    print("=" * len(title))


def read_required_string(prompt):
    while True:
        result = input(prompt).strip()
        if result:
            return result
        print("[ERR] Value is required.")


def read_int(prompt, min=-100_000, max=100_000):
    while True:
        try:
            result = int(read_required_string(prompt))
            if min <= result <= max:
                return result
            print(f"[ERR] Value must be between {min} and {max}.")
        except ValueError:
            print("[ERR] Value must be an integer.")


def read_decimal(prompt):
    while True:
        try:
            return decimal.Decimal(read_required_string(prompt))
        except decimal.InvalidOperation:
            print("[ERR] Value must be a decimal.")
