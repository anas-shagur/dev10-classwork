# 1. Create a list of numbers from 1 to 100
# that are divisible by 2 and 3 using list comprehension.
# 2. Print the list to the console.
# Expected: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]


numbers = [i for i in range(1,101) if i % 2 == 0 and i % 3 == 0]

print(numbers)