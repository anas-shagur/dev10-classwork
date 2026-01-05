import logging
import os

from dynaconf import Dynaconf
from etl import ETLProcessor, Transformer
from sqlalchemy import create_engine


def run():
    logging.basicConfig(level=logging.NOTSET)

    movie_review_path = os.path.join(os.path.dirname(__file__), "movie_reviews.csv")
    load_path = os.path.join(os.path.dirname(__file__), "load.csv")

    def build_engine():
        settings = Dynaconf(envvar_prefix="DB", load_dotenv=True)
        return create_engine(settings.ENGINE_URL, echo=False)

    engine = build_engine()

    transformer = Transformer()

    with engine.connect() as cnx, cnx.begin():
        processor = ETLProcessor(
            cnx,
            movie_review_path,
            load_path,
            transformer,
        )
        processor.process()

    engine.dispose()


if __name__ == "__main__":
    run()
