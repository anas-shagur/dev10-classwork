import logging
import os

from data import (
    DictReviewRepository,
    MovieReviewCsvWriter,
    ReviewRepository,
)
from dynaconf import Dynaconf
from etl import ETLProcessor, Transformer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def run():
    logging.basicConfig(filename="etl.log", level=logging.INFO)
    movie_review_path = os.path.join(os.path.dirname(__file__), "movie_reviews.csv")
    load_path = os.path.join(os.path.dirname(__file__), "load.csv")

    def build_engine():
        settings = Dynaconf(envvar_prefix="DB", load_dotenv=True)
        return create_engine(settings.ENGINE_URL, echo=False)

    engine = build_engine()

    dbRepository = ReviewRepository(Session(engine))
    csvRepository = DictReviewRepository(movie_review_path)
    movieReviewWriter = MovieReviewCsvWriter(load_path)
    transformer = Transformer()

    with ETLProcessor(
        dbRepository,
        csvRepository,
        movieReviewWriter,
        transformer,
    ) as etl:
        etl.process()

    engine.dispose()


if __name__ == "__main__":
    run()
