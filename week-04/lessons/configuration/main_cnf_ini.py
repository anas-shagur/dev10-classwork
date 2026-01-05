import os

import mysql.connector

db_cnf_path = os.path.join(os.path.dirname(__file__), "db.cnf")
db_ini_path = os.path.join(os.path.dirname(__file__), "db.ini")


print("with db.cnf")
with mysql.connector.connect(option_files=db_cnf_path) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("""SELECT first_name, last_name, street_address, city 
                       FROM customer LIMIT 5;""")
        for row in cursor:
            print(row)

print("with db.ini")
with mysql.connector.connect(option_files=db_ini_path) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("""SELECT first_name, last_name, street_address, city 
                       FROM customer LIMIT 5;""")
        for row in cursor:
            print(row)
