# 1. Rewrite the following loop as a `for` statement.
# Run the code before you make changes to better understand current behavior.
# The transformation from `while` to `for` should not change behavior.

index = 5
while index <= 100:
    print(index)
    index += 5

index = 5
rng = range(5, 101, 5)
for i in rng:
    print(index)
    index += 5
    
