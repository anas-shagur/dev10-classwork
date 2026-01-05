from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)

# 1. Loop over each vehicle in `vehicle_map` and print vehicles with a Dodge make.
# 2. Loop three times with three different techniques: .items(), .keys(), .values().
