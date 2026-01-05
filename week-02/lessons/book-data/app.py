import csv
import os
import random

os.chdir(os.path.dirname(__file__))

file_path = "third_party_data.csv"


with open(file_path) as file:
    reader = csv.DictReader(file)
    data = [d for d in reader]

random.shuffle(data)

data = data[:100]

for _ in range(4):
    d = random.choice(data)
    d["project_id"] = ""
    d["customer_id"] = ""

for _ in range(4):
    d = random.choice(data)
    d["proj_desc"] = ""
    d["total"] = ""

data += [
    {
        "project_id": 72,
        "customer_id": 183,
        "proj_desc": "large retaining wall",
        "total": 16016.10,
    },
    {
        "project_id": 73,
        "customer_id": 78,
        "proj_desc": "small walkway",
        "total": 4116.00,
    },
    {
        "project_id": 2001,
        "customer_id": 1500,
        "proj_desc": "medium driveway",
        "total": 9436.00,
    },
    {
        "project_id": 2001,
        "customer_id": 1500,
        "proj_desc": "small walkway",
        "total": 3442.00,
    },
]

print(data)

random.shuffle(data)


with open(file_path, "w") as file:
    writer = csv.DictWriter(file, ["project_id", "customer_id", "proj_desc", "total"])
    writer.writeheader()
    writer.writerows(data)
