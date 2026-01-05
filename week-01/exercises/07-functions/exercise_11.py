def read_string(prompt):
    return input(prompt).strip()


# 1. Create a function.
# Name: read_int
# Inputs: string
# Output: int
# Description: prompts a user to enter a whole number and returns their input as an int.
# The parameter is the message displayed to the user.
#
# Requirements:
# read_int must use the read_string method.
# Don't use the `input` function call inside read_int.
# Pass the prompt along to read_string.
# Parse the output from read_string into an int.


if __name__ == "__main__":
    pillow_count = 0

    name = read_string("What's your name?: ")
    # 2. Uncomment the line below and confirm read_int works.
    # pillowCount = read_int("How many pillows do you sleep with?: ");

    print(f"{name} sleeps with {pillow_count} pillows.")
