from datetime import date

# (national forest name, state, established date, acres)
superior_forest = ("Superior", "Minnesota", date.fromisoformat("1909-02-13"), 2_093_590)


# 1. Print the national forest's name.
# Expected: Superior

# 2. Print the national forest's established date.
# Expected: 1909-02-13

# Slicing syntax: sequence[start:end:step]

# 3. Use a slice to print the national forest's state and acres.
# Hint: Use a step of 2.
# Expected: ('Minnesota', 2093590)

# 4. Existence check: Check if acres value 2_220_0222 is in superior_forest.
# Expected: False

# 5. Existence check: Check if acres value 2_093_590 is in superior_forest.
# Expected: True

# Stretch goal: Unpack the national forest tuple focusing on forest_name.
(forest_name, _, _, _) = superior_forest
print(forest_name)

# 6. Unpack the national forest tuple focusing on state and acres.
# Print the state and acres.

# 7. Grab the established date year and print it.
# Expected: 1909
