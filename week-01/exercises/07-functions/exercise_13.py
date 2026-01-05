# 1. Create a function.
# Name: are_in_order
# Inputs: int, int, int
# Output: boolean
# Description: return True if the three parameters are in ascending order.
# Otherwise, returns False.
# (See Exercise 07.)


# 2. Create a function.
# Name: are_contiguous
# Inputs: int, int, int
# Output: boolean
# Description: return True if a parameter is one step away from the next parameter.
# That is, they're "next to" one another.
# A step can be either a step up or a step down.
# Otherwise, returns False.
# Examples
# 1, 2, 3 -> True
# 1, 1, 2 -> False (first param must be either one less or one more than the second)
# 1, 2, 1 -> True
# 1, 5, 7 -> False
# 0, 1, 2 -> True
# 7, 6, 5 -> True
# 7, 5, 6 -> False
# 1, 0, 1 -> True


# 3. Create a function.
# Name: is_ascending_contiguous
# Inputs: int, int, int
# Output: boolean
# Description: return True if the three parameters are in ascending order and are contiguous
# Otherwise, returns False.
# Hint: call are_in_order and are_contiguous. Neither method can guarantee the result alone, but together they solve
# the problem.


if __name__ == "__main__":
    # 4. Uncomment the code below and confirm it works.
    # print(is_ascending_contiguous(3, 4, 5))  # True
    # print(is_ascending_contiguous(-10, 4, 100))  # False
    # print(is_ascending_contiguous(2, 1, 2))  # False
    # print(is_ascending_contiguous(5, 4, 3))  # False, not ascending
    pass
