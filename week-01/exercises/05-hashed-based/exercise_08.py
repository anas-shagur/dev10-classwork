from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)

# 1. Print the size of `vehicle_map`.
# 2. Remove VIN 2G4WD582061270646
# 3. Remove VIN 1M8GDM9AXKP042788
# 4. Print the size of `vehicle_map`. (Expected: 999)
# Warning: This could result in a KeyError if the key does not exist in the map.
# Hint: Use the `pop` method.
