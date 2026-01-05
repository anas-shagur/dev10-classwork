from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)


# 1. Replace the vehicle tuple with VIN 2G4WD582061270646 with a new Orange 1994 Chrysler School Bus.
# 2. Retrieve the new vehicle from `vehicle_map` and print it to confirm it was updated.
