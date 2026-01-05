from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)

# 1. Retrieve the vehicle tuple with the VIN: 1M8GDM9AXKP042788 from `vehicle_map`. Store the vehicle in a variable.
# 2. Print it to stdout. Confirm it's None. (The key does not exist in the map.)
# Expected: None
