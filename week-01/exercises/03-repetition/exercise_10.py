phrase = input("Enter a phrase: ")

# 1. Write a loop to determine if the letter `x` occurs in a user-entered phrase.
# 2. Don't use the `in` operator.
# 3. Print a message for both finding and not finding the `x`.

x_not_found = True

for i in range(len(phrase)):
    if phrase[i] == 'x':
        print("Found 'x', exiting out of loop.")
        x_not_found = False
        break

if x_not_found:
    print("Couldn't find x.")


        