import csv
import os

vehicle_map = {}

parent_dir = os.path.dirname(__file__)
file_path = os.path.join(parent_dir, "vehicles.csv")

# vin,make,model,year,color
with open(file_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        vehicle_map[row["vin"]] = (
            row["vin"],
            row["make"],
            row["model"],
            int(row["year"]),
            row["color"],
        )
