import random


def make_random_list():
    """
    Generates a list[int] of length between 50 and 150,
    whose elements are randomly generated between -500 and 500.

    Args:
        None

    Returns:
        list[int]: A list of random integers.
    """

    result = []
    for _ in range(random.randint(50, 150)):
        result.append(random.randint(-500, 500))
    return result


if __name__ == "__main__":
    values = make_random_list()

    # 1. Create a list[int] to hold the positive elements.
    # 2. Loop through `values` and add positive elements to the list.
    # 3. Confirm the positive list is properly populated either by debugging or printing its elements.
