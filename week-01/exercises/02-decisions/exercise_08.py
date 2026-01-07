# OPPOSITES
# Given a word, print its opposite.

word = input("Enter a word: ")
opposite = None

# 1. Add at least two more opposites by adding `else if` clauses.
word = word.lower()
if word == "high":
    opposite = "low"
elif word == "hot":
    opposite = "cold"
elif word == "little":
    opposite = "big"
elif word == "yes":
    opposite = "no"
elif word == "in":
    opposite = "out"
elif word == "up":
    opposite = "down"

if opposite is None:
    print(f"I don't have an opposite for {word}.")
else:
    print(f"The opposite of {word} is {opposite}.")
