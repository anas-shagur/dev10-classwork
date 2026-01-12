values = [18, 42, 54, 93, 22]

# 1. Create a loop to calculate the sum of elements in `values`.
# 2. Print the result.

sum = 0

for i in range(len(values)):
    sum += values[i]

print(f"Sum is {sum}.")