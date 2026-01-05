import mysql.connector
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix=False,
    settings_files=["db.toml"],
)

print(f"{type(settings.db.host)}: {settings.db.host}")
print(f"{type(settings.db.port)}: {settings.db.port}")
print(f"{type(settings.db.user)}: {settings.db.user}")
print(f"{type(settings.db.password)}: {settings.db.password}")
print(f"{type(settings.db.database)}: {settings.db.database}")
print(f"{type(settings.api.api_key)}: {settings.api.api_key}")
print(settings.db)

with mysql.connector.connect(**settings.db) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("""SELECT first_name, last_name, street_address, city 
                       FROM customer LIMIT 5;""")
        for row in cursor:
            print(row)
