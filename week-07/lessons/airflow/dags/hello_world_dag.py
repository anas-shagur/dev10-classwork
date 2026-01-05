import pendulum
from airflow.sdk import dag, task


# 1. dag decorator
@dag(
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def hello_world_dag():  # 2. dag function
    @task()  # 3. task decorator
    def print_hello():  # 4. task function
        print("Hello World!")

    print_hello()  # 5. Execute our task `print_hello()`


hello_world_dag()  # 6. Execute our dag `hello_world_dag()`
