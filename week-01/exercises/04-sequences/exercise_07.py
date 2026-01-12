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

def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

# 1. Create a method.
# Name: sum_list
# Inputs: list[int]
# Output: int
# Description: calculates the sum of the parameter's elements and returns it.

if __name__ == "__main__":
    values = make_random_list()
    # 2. Uncomment the code below and make it work.

    sum = sum_list(values)
    print(sum)
    print(sum_list(make_random_list()))
    print(sum_list(make_random_list()))
