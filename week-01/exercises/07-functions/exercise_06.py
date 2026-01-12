# 1. Create a function.
# Name: is_between
# Inputs: int, int, int
# Output: boolean
# Description: return True if the first parameter is between the second and third parameter.
# Otherwise, returns False.

def is_between(b, a, c):
    return (b > a and b < c) or (b > c and b < a)


if __name__ == "__main__":
    # 2. Call your method in various ways to test it here.
    print(is_between(5, 0, 10))
    print(is_between(5, 10, 0))
    print(is_between(5, 1, 1))
    print(is_between(5, 10, 10))
    print(is_between(5, 5, 5))

    pass
