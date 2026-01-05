from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)

# 1. Instantiate a dictionary.
# 2. Add two vehicle tuples to the new dictionary.
# 3. Add items from the new dictionary to `vehicle_map` using the `update` method.
# 4. Print the new dictionary to standard out.
