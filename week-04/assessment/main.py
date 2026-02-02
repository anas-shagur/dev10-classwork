import os

from dynaconf import Dynaconf
from sqlalchemy import create_engine

from etl import ETLProcessor

os.chdir(os.path.dirname(__file__))


def build_engine():
    settings = Dynaconf(envvar_prefix="DB", load_dotenv=True)
    return create_engine(settings.ENGINE_URL, echo=False)


def run():
    engine = build_engine()

    processor = ETLProcessor(
        engine,
        movies_path="ml-latest-small/movies.csv",
        ratings_path="ml-latest-small/ratings.csv",
    )

    processor.process()

    engine.dispose()


if __name__ == "__main__":
    run()
