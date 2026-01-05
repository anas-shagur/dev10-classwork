import random


def make_random_ascending_list():
    result = []
    current = random.randint(0, 10)
    for _ in range(random.randint(50, 150)):
        result.append(current)
        current += random.randint(0, 3)
    return result


if __name__ == "__main__":
    # MERGE
    one = make_random_ascending_list()
    two = make_random_ascending_list()

    # make_random_ascending_list creates a random list with a capacity between 50 and 150.
    # Its elements are guaranteed to be sorted ascending.
    # 1. Create a new result list[int].
    # 2. Merge elements from `one` and `two` into the result list so that its values are sorted.

    # Pseudocode:
    # Create an integer index for `one` and `two` all starting at 0.
    # Use a while loop to iterate until both indexes are less than their respective lengths.
    #   if one_index >= len(one), there are no `one` elements remaining so use elements from two
    #   if two_index >= len(two), there are no `two` elements remaining so use elements from one
    #   if one[one_index] is less than or equal two[two_index], add it to the result and increment one_index.
    #   if two[two_index] is less than one[one_index], add it to the result and increment two_index.
