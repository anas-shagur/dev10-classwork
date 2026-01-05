import os

from dynaconf import Dynaconf
from etl import ETLProcessor, Transformer
from sqlalchemy import create_engine, text

os.chdir(os.path.dirname(__file__))


def run():
    third_party_path = "third_party_data.csv"
    load_path = "load.csv"

    def build_engine():
        settings = Dynaconf(envvar_prefix="DB", load_dotenv=True)
        return create_engine(settings.ENGINE_URL, echo=False)

    engine = build_engine()

    transformer = Transformer()

    with engine.connect() as cnx, cnx.begin():
        cursor = cnx.execute(text("SELECT * FROM employee;"))
        print(cursor.fetchone())
        # processor = ETLProcessor(
        #     cnx,
        #     third_party_path,
        #     load_path,
        #     transformer,
        # )
        # processor.process()

    engine.dispose()


if __name__ == "__main__":
    run()
