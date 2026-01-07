# BORDER BOX
# 1. Use nested loops to print a box in the console with a different character for the border.
# One loop should represent rows and the other should represent columns.
# The border character should be different from the internal box character.
# 2. Change the row and column limit to change the shape of the box.

# Expected Output (5X5)
# *****
# *###*
# *###*
# *###*
# *****

# (3X4)
# ****
# *##*
# ****

# (2X2)
# **
# **

rows = 5
columns = 5

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end='')
        else:
            print("#", end='')
    print()

print()

rows = 3
columns = 4

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end='')
        else:
            print("#", end='')
    print()

print()

rows = 2
columns = 2

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end='')
        else:
            print("#", end='')
    print()


