from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
# print(vehicle_map)

# 1. Retrieve the vehicle tuple with the key, VIN: 2G4WD582061270646, from `vehicle_map`. 
# Store the tuple in a variable.
vehicle = vehicle_map.get("2G4WD582061270646")
# 2. Print it to standard out. Confirm it's a Khaki 1989 Buick LeSabre.
print(vehicle)
# Expected: ('2G4WD582061270646', 'Buick', 'LeSabre', 1989, 'Khaki')