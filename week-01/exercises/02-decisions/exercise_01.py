# 1. Run the code and press [Enter] without typing a value.
# (It results in an IndexError: string index out of range)
value = input("Enter a value: ")
print(value)

# 2. Change the if condition to check for a string length greater than 0.
if value[0] == "1":
    # 3. Replace the current message with the value variable.
    print("Value starts with the number 1.")
