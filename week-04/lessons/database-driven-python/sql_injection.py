import mysql.connector

# sql injection

cnx = mysql.connector.connect(host="localhost")
cursor = cnx.cursor()

first_name = input("Enter a name: ")

sql = "SELECT * FROM customer WHERE first_name = '" + first_name + "';"

for record in cursor.execute(sql):
    print(record)

# no injection

cnx = mysql.connector.connect(host="localhost")
cursor = cnx.cursor()

first_name = input("Enter a name: ")

sql = "SELECT * FROM customer WHERE first_name = %s;"

cursor.execute(sql, (first_name,))

for record in cursor:
    print(record)
