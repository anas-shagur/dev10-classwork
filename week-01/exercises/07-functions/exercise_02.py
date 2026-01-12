# multiply_three accepts threes ints or floats and multiplies them together.
# 1. Finish implementing the multiply_three method.
def multiply_three(a, b, c):
    return a * b * c


if __name__ == "__main__":
    result = multiply_three(2, 2, 2)
    print(result)  # Expected: 8.0
    print(multiply_three(-1, 1, -1))  # Expected: 1.0
    print(multiply_three(12, 0.5, 0.5))  # Expected: 3.0

