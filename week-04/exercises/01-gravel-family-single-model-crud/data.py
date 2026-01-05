from models import Employee


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


class EmployeeRepository:
    def __init__(self, connection):
        self._context = DatabaseContext(connection)

    def find_all(self, limit=25):
        query = """
            SELECT
                employee_id,
                first_name,
                last_name,
                start_date,
                end_date
            FROM employee
            LIMIT %s;
        """
        records = self._context.find(query, (limit,))
        return [Employee(*record) for record in records]

    def find_by_id(self, employee_id):
        query = """
            SELECT
                employee_id,
                first_name,
                last_name,
                start_date,
                end_date
            FROM employee
            WHERE employee_id = %s;
        """
        record = self._context.find_one(query, (employee_id,))
        return Employee(*record) if record else None

    def update(self, employee):
        query = """
            UPDATE employee SET
                first_name = %s,
                last_name = %s,
                start_date = %s,
                end_date = %s
            WHERE employee_id = %s;
        """
        return self._context.update(
            query,
            (
                employee.first_name,
                employee.last_name,
                employee.start_date,
                employee.end_date,
                employee.employee_id,
            ),
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._context.close()
