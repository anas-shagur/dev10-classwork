# Exercise 09

# 1. Add a Python script, `exercise_09.py`, to this directory.
# 2. Collect three pieces of data from the user: a minimum value, a maximum value, and an actual value.
# 3. Add `if/else` statements to determine if the actual value is between the min and max.
# 4. Print messages for both true and false cases.

min_value = input("Enter minimum value: ")
max_value = input("Enter maximum value: ")
actual_value = input("Enter actual value: ")

if actual_value > min_value and actual_value < max_value:
    print("Value is in between the min and max.")
else:
    print("Value is NOT between the min and max.") 
