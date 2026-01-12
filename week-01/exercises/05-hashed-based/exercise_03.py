from vehicles import vehicle_map

# `vehicle_map` is a dictionary that holds 1000 vehicles.
# The key is the VIN (https:#en.wikipedia.org/wiki/Vehicle_identification_number) as a string.
# The value is a tuple with (vin: str, make: str, model: str, year: int, color: str).
print(vehicle_map)


# 1. Create a new vehicle tuple. Use a VIN that's easy to remember.
# 2. Assign a `vehicle_map` key (VIN) to the new vehicle tuple.
# 3. Confirm the Vehicle was added by retrieving it and printing it to the console.

# You can also use the https://docs.python.org/3/library/stdtypes.html#dict.setdefault
# method to add a new vehicle tuple to the map.

vin = "1"
vehicle = (vin, "Kia", "Sportage", 2026, "White")

vehicle_map[vin] = vehicle

print(vehicle_map[vin])