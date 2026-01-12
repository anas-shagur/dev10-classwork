from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
# print(vehicle_map)

# 1. How many vehicles are Pink (ignore case)?
# Expected: 54

count = 0
for vehicle in vehicle_map.values():
    if vehicle[4].lower() == "pink":
        count += 1

print(count)
