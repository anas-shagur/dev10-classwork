import mysql.connector

db_username = "username"
db_password = "password"

cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=db_username,
    password=db_password,
    database="bowls",
)

print(cnx.connection_id)
print(cnx.is_connected())
cnx.close()

cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=db_username,
    password=db_password,
    database="bowls",
)

cursor = cnx.cursor()
cursor.execute("SELECT * FROM customer LIMIT 15;")

record = cursor.fetchone()
print("First record:")
print(record)

print("2-4 records:")
for record in cursor.fetchmany(size=3):
    print(record)

print("All but 4 records:")
records = cursor.fetchall()
for record in records:
    print(record)

cursor.close()
cnx.close()
