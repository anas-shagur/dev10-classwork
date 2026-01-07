# CRUISE SHIP ACTIVITIES
# ======================
# When the cruise ship docks at a port, passengers can choose from one of two activities: snorkeling and shopping.
# Snorkelers must always have an even number since they use the buddy system.
# Use if/else statements to apply the following rules:
# If the number of snorkelers is even, all is well. Everyone gets their preferred activity.
# If it's not, add the snorkeler count to the shopper count and set snorkelers to 0.
# Print the total snorkelers and shoppers.

value = input("# of Snorkelers: ")
snorkeler_count = int(value)

value = input("# of Shoppers: ")
shopper_count = int(value)

# 1. Apply if/else here.
if snorkeler_count % 2 == 1:
    shopper_count += snorkeler_count
    snorkeler_count = 0

print("Number of snorkelers: {}".format(snorkeler_count))
print("Number of shoppers: {}".format(shopper_count))
