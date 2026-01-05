# Pokemon Database and API

We have two services.

## Pokemon DB

```
./db
├── Dockerfile
└── schema-and-data.sql
```

**schema-and-data.sql**

1. Create a `pokedex` database.
2. Use DDL to create tables: `poke_type` and `pokemon`. `pokemon` has a foreign key between primary type and secondary type.
3. Insert 18 `poke_type`s.
4. Insert 267 `pokemon`s.

**Dockerfile**

1. Use `mariadb:latest`.
2. The `/docker-entrypoint-initdb.d/` directory copies all of our SQL files and at our very first `docker run`, executes those files in order. `docker stop` and `docker start` will never execute those files.

## Pokemon API

```
./api
├── Dockerfile
├── main.py
├── models.py
├── requests.http
└── requirements.txt
```

**models.py**

1. Use `@dataclass`es: `PokeType` and `Pokemon`.
2. `find_all` has a connection to our MariaDB.
3. `find_all` supports paging.
3. We don't want to _first_ find `find_poke_type` and then the `Pokemon`, because if the `Pokemon` have a length of zero, the `find_poke_type` is a waste.

**main.py**

1. Only support `GET` requests.
2. `page` is a query string variable. It can either exist or not. If `page` isn't an integer, we reject it.

    ```
    http://127.0.0.1:5000/pokemon               # defaults to 1
    http://127.0.0.1:5000/pokemon?page=2        # works!
    http://127.0.0.1:5000/pokemon?page=meatloaf # bad integer
    ```

**requirements.txt**

1. Our requirements are `Flask` and `mariadb` that don't require version numbers.

**Dockerfile**

1. Use `python:alpine`.
2. Create a working directory.
3. Copy all of the files, minus `.dockerignore`.
4. `apk` is the Alpine package manager. Update it and use compilers that build out the MariaDB C Connector.
5. We need to build the MariaDB Connector first, then install our `mariadb` Python package.
6. Expose port 5000
7. Run flask.

## docker-compose.yml

```yaml
services:
  # the database
  db:
    build: ./db
    hostname: db
    environment:
      - MARIADB_ROOT_PASSWORD=${DB_PASSWORD}
  # the api
  api:
    build: ./api
    hostname: api
    environment:
      - MARIADB_ROOT_PASSWORD=${DB_PASSWORD}
    ports:
      - 5000:5000
    depends_on:
      - db
```

Our `.env` file embeds our `${DB_PASSWORD}` into our `docker-compose.yml`.

```.env
DB_PASSWORD=top-secret-password
```