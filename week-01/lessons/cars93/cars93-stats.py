import csv
from math import sqrt
import statistics as stats
import os

# print(os.getcwd())
with open("cars93.csv", "rt") as f:
    reader = csv.DictReader(f)
    prices = [float(row["Price"]) for row in reader]

# average
mean = sum(prices) / len(prices)
# sort prices, grab the middle value
median = sorted(prices)[len(prices) // 2]
# find the most common price
# key=prices.count is a function that counts the number of times each price appears
mode = max(prices, key=prices.count)
# the difference between each price and mean
mean_diff = [price - mean for price in prices]
# square the differences
squares = [diff**2 for diff in mean_diff]
# sum the squares
sum_squares = sum(squares)
# divide sum_squares by sample size - 1
variance = sum_squares / (len(prices) - 1)
# square root of variance
std_dev = sqrt(variance)

# maths
print(mean)  # 19.50967741935484
print(median)  # 17.7
print(mode)  # 15.9
print(variance)  # 93.30457924263673
print(std_dev)  # 9.659429550580963


# statistics module
print(stats.mean(prices))  # 19.509677419354837
print(stats.median(prices))  # 17.7
print(stats.mode(prices))  # 15.9
print(stats.variance(prices))  # 93.30457924263675
print(stats.stdev(prices))  # 19.659429550580963
