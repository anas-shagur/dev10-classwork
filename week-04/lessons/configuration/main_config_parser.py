import configparser
import os

import mysql.connector

config_path = os.path.join(os.path.dirname(__file__), "db.ini")

config = configparser.ConfigParser(interpolation=None)
config.read(config_path)

print(config.sections())

# database stuff
print(config["client"]["host"])
print(config["client"]["port"])
print(config["client"]["user"])
print(config["client"]["password"])
print(config["client"]["database"])

# API stuff
print(config["api"]["api_key"])

with mysql.connector.connect(**config["client"]) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("""SELECT first_name, last_name, street_address, city 
                       FROM customer LIMIT 5;""")
        for row in cursor:
            print(row)