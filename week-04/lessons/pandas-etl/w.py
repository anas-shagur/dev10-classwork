import pandas as pd
import mysql.connector


cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="bug4pig",
    database="bowls",
)

sql = "SELECT * FROM customer LIMIT 15;"
df = pd.read_sql(sql, cnx)
print(df.head())

cnx.close()
