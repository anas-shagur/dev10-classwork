# ARE ORDERED
# Determine if three numbers are in order.

first = int(input("Enter the first value: "))
second = int(input("Enter the second value: "))
third = int(input("Enter the third value: "))

# 1. Add decisions statements to determine if first, second, and third are in order.
# 2. Print messages for both ordered and unordered cases.

if second > first and third > second:
    print("It is ordered")
else:
    print("It is not ordered")