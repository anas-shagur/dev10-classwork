import os

import mysql.connector
from dotenv import dotenv_values, load_dotenv

load_dotenv()  # load from .env file

# use os.getenv to resolve environment variables
print(os.getenv("DB_HOST"))
print(os.getenv("DB_PORT"))
print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))
print(os.getenv("DB_NAME"))

# API stuff
print(os.getenv("API_KEY"))

# Our 'USER' doesn't get replaced.
# It's always tracking the current user.
print(os.getenv("USER"))  # corbinmarch (yours will be different)

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")


config = dotenv_values(dotenv_path)
for key, value in config.items():
    print(f"{key}: {value}")

with mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute(
            "SELECT first_name, last_name, email_address FROM customer LIMIT 5;"
        )
        for row in cursor:
            print(row)

with mysql.connector.connect(
    host=config["DB_HOST"],
    port=config["DB_PORT"],
    user=config["DB_USER"],
    password=config["DB_PASSWORD"],
    database=config["DB_NAME"],
) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute(
            "SELECT first_name, last_name, email_address FROM customer LIMIT 5;"
        )
        for row in cursor:
            print(row)
