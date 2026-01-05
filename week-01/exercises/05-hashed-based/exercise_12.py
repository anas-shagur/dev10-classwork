# Powerball

# https://en.wikipedia.org/wiki/Powerball#Basic_game
# "In each game, players select five numbers from a set of 69 white balls and one number from 26 red Powerballs;
# the red ball number can be the same as one of the white balls.
# The drawing order of the five white balls is irrelevant;"
#
# Summary:
# 5 white balls numbered 1-69, each unique
# 1 red Powerball numbered 1-26 (ignored)

# 1. Create a set for the white balls.
# 2. Collect user input, balls 1-5 values 1-69, and add them to the set.
# 3. Validate that the set does not have duplicates (len == 5).
#   Goals:
# - Use an internal `for` loop to collect the five white balls.
# - Use an external `while` loop with a condition, `while message != "exit":`, to exit the loop.
