import random

MAX_INT = 100000

random_number = random.randint(0, MAX_INT)
was_found = False

for i in range(0, MAX_INT // 2):
    if i == random_number:
        was_found = True
        break

if was_found:
    print("Random number was found!")
else:
    print("Random number was not found!")
