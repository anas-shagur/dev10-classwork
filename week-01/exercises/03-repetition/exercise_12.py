# 1. Collect a phrase from a user via the standard in.
# 2. Count the number of digits in the phrase.
# Hint: https://docs.python.org/3/library/stdtypes.html#str.isdigit
# 3. Print the result.

phrase = input("Enter a phrase: ")

count = 0
for i in range(len(phrase)):
    if phrase[i].isdigit():
        print(f"{phrase[i]} is a digit.")
        count += 1

print(f"Phrase has {count} digits.")