# DAYS OF THE WEEK

print("1. Monday")
print("2. Tuesday")
print("3. Wednesday")
print("4. Thursday")
print("5. Friday")
print("6. Saturday")
print("7. Sunday")
day = int(input("Select a day [1-7]: "))


# 1. Add cases for days 2-7. Print a tired cliché for each day.
match day:
    case 1:
        print('I refuse to say "a case of the Mondays".')
    case _:
        print("I don't recognize that day.")
