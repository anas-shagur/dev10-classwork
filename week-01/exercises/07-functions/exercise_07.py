# 1. Create a function.
# Name: are_in_order
# Inputs: int, int, int, int
# Output: boolean
# Description: return True if the four parameters are in ascending order.
# Otherwise, returns False.

def are_in_order(a, b, c, d):
    return b > a and c > b and d > c

if __name__ == "__main__":
    # 2. Call your method in various ways to test it here.
    print(are_in_order(1,2,3,4))
    print(are_in_order(1,3,2,4))
    print(are_in_order(4,3,2,1))
    print(are_in_order(1,2,2,4))
    print(are_in_order(1,2,10,100))

    pass
