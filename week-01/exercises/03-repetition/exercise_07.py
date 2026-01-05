import string
# REMOVE WHITESPACE

phrase = input("Enter a phrase and I'll remove the whitespace: ")

# 1. Write code to remove whitespace from a user-entered phrase.
# Hint: the https://docs.python.org/3/library/string.html#string.whitespace may be useful
# using the `in` keyword.

result = ""
for char in phrase:
    result += char


print(f"Your phrase without whitespace is: {result}")
