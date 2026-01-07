# MATCH OPPOSITES
# Given a word, print its opposite using a match statement.

word = input("Enter a word: ")
opposite = None
word = word.lower()

# 1. Re-implement exercise_08 using a match statement.

match word:
    case "hot":
        opposite = "cold"
    case "yes":
        opposite = "no"
    case "in":
        opposite = "out"
    case "up":
        opposite = "down"
    case "wrong":
        opposite = "right"
    case "black":
        opposite = "white"

if opposite is None:
    print(f"I don't have an opposite for {word}.")
else:
    print(f"The opposite of {word} is {opposite}.")