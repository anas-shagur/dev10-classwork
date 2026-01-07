start = int(input("Start: "))
end = int(input("End: "))

# 1. Write a loop to sum all numbers between start and end.
# 2. Print the result.
sum = 0
for i in range(start, end):
    # print(i)
    sum += i

print(sum)
