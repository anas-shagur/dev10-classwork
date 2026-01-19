def print_header(header):
    print()
    print(header)
    print("=" * len(header))


def read_string(prompt):
    return input(prompt).strip()


def read_required_string(prompt):
    while True:
        value = read_string(prompt)
        if value:
            return value
        print("[ERR] Value is required.")


def read_int(prompt, min_val, max_val):
    while True:
        value = read_required_string(prompt)
        if value.isdigit():
            value = int(value)
            if min_val <= value <= max_val:
                return value
        print(f"[ERR] Value must be between {min_val} and {max_val}.")


def read_positive_float(prompt):
    while True:
        value = read_required_string(prompt)
        try:
            value = float(value)
            if value > 0:
                return value
        except ValueError:
            pass
        print("[ERR] Value must be a positive number.")


def read_positive_int(prompt):
    while True:
        value = read_required_string(prompt)
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
        print("[ERR] Value must be a positive integer.")