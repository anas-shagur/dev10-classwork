from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)

# 1. Instantiate a dictionary named `two_thousand_six`.
# 2. Loop through `vehicle_map` and all 2006 vehicles and assign them to `two_thousand_six`;
# 3. Loop through `two_thousand_six` and display all vehicles.
# 4. How many 2006 vehicles are there? (Expected: 50)
