def read_required_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("[ERR] value is required.")


def read_int(prompt):
    while True:
        try:
            return int(read_required_string(prompt))
        except ValueError:
            print("[ERR] value must be an integer.")
