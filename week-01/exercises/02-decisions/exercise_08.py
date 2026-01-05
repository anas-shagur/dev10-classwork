# OPPOSITES
# Given a word, print its opposite.

word = input("Enter a word: ")
opposite = None

# 1. Add at least two more opposites by adding `else if` clauses.
word = word.lower()
if word == "high":
    opposite = "low"
elif word == "cold":
    opposite = "hot"
elif word == "little":
    opposite = "big"

if opposite is None:
    print(f"I don't have an opposite for {word}.")
else:
    print(f"The opposite of {word} is {opposite}.")
