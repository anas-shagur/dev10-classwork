import pendulum
from airflow.sdk import dag, task
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from sqlalchemy import create_engine

from simple.players.etl import PlayersETL


@dag(
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["mysql", "players"],
)
def players_etl_dag():

    create_schema = SQLExecuteQueryOperator(
        task_id="create_players_schema",
        conn_id="mysql_players",  
        sql="/players/players_ddl.sql",
    )

    @task
    def run_etl():

        hook = MySqlHook(mysql_conn_id="mysql_players")
        connection = hook.get_conn()

        engine = create_engine(
            hook.get_uri(),
            creator=lambda: connection
        )

        processor = PlayersETL(
            "/opt/airflow/dags/simple/players/players.csv",
            engine
        )

        processor.process()

        engine.dispose()

    etl_task = run_etl()

    create_schema >> etl_task


players_etl_dag()