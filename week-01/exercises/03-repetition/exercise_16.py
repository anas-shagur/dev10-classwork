# CUT THE MIDDLE
phrase = input("Phrase: ")
start = int(input("Start: "))
end = int(input("End: "))

# 1. Write a loop to create a new string from a phrase by "cutting out" any characters from the start index
# to the end index.
# 2. Print the result.
# 3. Stretch goal: use a slice to accomplish the same task.


# Examples
# phrase, start, end -> result
# ========================
# "orange", 1, 2 -> "onge"
# "orange", 3, 3 -> "orage"
# "orange", 4, 3 -> "orange" (ignore when start is greater than end)
# "orange", 15, 25 -> "orange" (ignore when start and end are bigger than the length of the phrase)
# "one two three", 4, 7 -> "one three"
# "interrupting moooo cow", 12, 17 -> "interrupting cow"
