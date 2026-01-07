# 1. Display the following menu and collect an integer choice from the user.
# (See exercise_14 for a menu example.)

print("""
Menu
1. Print the name of an animal.
2. Print the name of a state.
3. Print the name of a beetle.
4. Print the name of a mineral.
""")

choice = int(input("Select [1-4]: "))

match choice:
    case 1:
        print("Deer")
    case 2:
        print("MN")
    case 3:
        print("Scarab")
    case 4:
        print("Diamond")
    case _:
        print("Invalid selection.")

# 2. Use a `match` to cover cases 1-4 as well as a default.
# For 1-4, print an animal, state, beetle, or mineral respectively.
# For the default case, print "Unknown Menu Option".


