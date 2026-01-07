colors = "red orange yellow green blue indigo violet"
print(colors[0:3])
color_list = colors.split(" ")
# range(len(color_list))
# enumerate(color_list)

for i in range(1, len(color_list)):
    print(color_list[i])

# 1. Use string slicing to print each color on its own line.
# "red" is already complete.

# Expected Output:
# red
# orange
# yellow
# green
# blue
# indigo
# violet
