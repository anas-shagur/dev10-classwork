import uuid

from models import Customer


class DatabaseContext:
    def __init__(self, connection):
        self._connection = connection

    def find(self, query, params=None) -> list[tuple]:
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def find_one(self, query, params=None) -> tuple:
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

    def insert(self, query, params=None):
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
            self._connection.commit()
            return cursor.lastrowid

    def update(self, query, params=None) -> int:
        with self._connection.cursor() as cursor:
            cursor.execute(query, params)
            self._connection.commit()
            return cursor.rowcount

    def close(self):
        if self._connection.is_connected():
            self._connection.close()


class CustomerRepository:
    SELECT = """
        SELECT
            customer_id,
            first_name,
            last_name,
            street_address,
            city,
            state,
            zip_code,
            email_address,
            phone,
            date_added,
            reward_points
        FROM customer
    """

    def __init__(self, connection):
        self.context = DatabaseContext(connection)

    def find_all(self, limit=25):
        query = f"{self.SELECT} LIMIT %s;"
        return [Customer(*record) for record in self.context.find(query, (limit,))]

    def find_by_last_name_begins_with(self, last_name_prefix):
        query = f"{self.SELECT} WHERE last_name LIKE %s;"
        return [
            Customer(*record)
            for record in self.context.find(query, (f"{last_name_prefix}%",))
        ]

    def find_by_id(self, customer_id):
        query = f"{self.SELECT} WHERE customer_id = %s;"
        record = self.context.find_one(query, (customer_id,))
        if record:
            return Customer(*record)
        return None

    def find_by_email(self, email):
        query = f"{self.SELECT} WHERE email_address = %s;"
        record = self.context.find_one(query, (email,))
        if record:
            return Customer(*record)
        return None

    def insert(self, customer):
        query = """
            INSERT INTO customer (
                customer_id,
                first_name,
                last_name,
                street_address,
                city,
                state,
                zip_code,
                email_address,
                phone,
                date_added,
                reward_points
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );"""

        customer.customer_id = str(uuid.uuid4())
        params = customer.to_tuple()
        return self.context.insert(query, params)

    def update(self, customer):
        query = """
            UPDATE customer SET
                first_name = %s,
                last_name = %s,
                street_address = %s,
                city = %s,
                state = %s,
                zip_code = %s,
                email_address = %s,
                phone = %s,
                date_added = %s,
                reward_points = %s
            WHERE customer_id = %s;"""
        params = customer.to_tuple()
        return self.context.update(query, params[1:] + params[0:1])

    def delete_by_email(self, email):
        query = "DELETE FROM customer WHERE email_address = %s;"
        return self.context.update(query, (email,))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.context.close()
