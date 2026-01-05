import csv

from alchemy_models import Review
from sqlalchemy import select
from sqlalchemy.orm import Session


class ReviewRepository:
    def __init__(self, session: Session):
        self._session = session

    def find_all(self):
        stmt = select(Review)
        return list(self._session.scalars(stmt))

    def is_connected(self):
        return self._session.bind is not None

    def close(self):
        if self.is_connected():
            self._session.close()


class DictReviewRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def find_all(self):
        records = []

        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            for record in reader:
                records.append(record)

        return records


class MovieReviewCsvWriter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def add_all(self, movie_reviews):
        with open(self.file_path, "w") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["anonymous_id", "movie_id", "movie_name", "rating", "review_date"]
            )
            writer.writerows(mr.to_tuple() for mr in movie_reviews)
