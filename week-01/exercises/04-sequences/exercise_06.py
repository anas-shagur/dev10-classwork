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

    # 1. Create a loop to calculate the sum of elements in `values`.
    # 2. Print the result.
    # Since the list is random, your result will vary during each run.
    # 3. Print the length of the list.

sum = 0

for i in range(len(values)):
    sum += values[i]

print(f"Sum is {sum}.")
print(f"Length of the list is {len(values)}.")