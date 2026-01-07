# USER-DEFINED BOX
# 1. Collect the following from a user: rows, columns, box character, border character.
# 2. Use nested loops to print a user-defined box in the console.
# (See Exercise 14.)

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
box = input("Enter box character: ")
border = input("Enter border character: ")

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print(box, end='')
        else:
            print(border, end='')
    print()