import logging
import re
from datetime import date

from models import MovieReview

logger = logging.getLogger(__name__)


class Transformer:
    def transform(self, db_reviews, csv_reviews):
        logger.info(f"DB review count: {len(db_reviews)}")
        movie_reviews = self.db_to_movie_reviews(db_reviews)
        logger.info(f"Movie review count: {len(movie_reviews)}")

        logger.info(f"CSV review count: {len(csv_reviews)}")
        csv_reviews = self.remove_na_anonymous_id(csv_reviews)
        logger.info(f"Remove anonymous_id CSV review count: {len(csv_reviews)}")
        csv_reviews = self.remove_na_movie_name(csv_reviews)
        logger.info(f"Remove movie name CSV review count: {len(csv_reviews)}")

        # we don't care about genre or review date

        csv_reviews = self.convert_percent_to_number(csv_reviews)
        logger.info(f"% to number CSV review count: {len(csv_reviews)}")
        movie_reviews = self.merge(movie_reviews, csv_reviews)
        logger.info(f"Merged movie review count: {len(movie_reviews)}")

        movie_reviews = self.remove_dupes(movie_reviews)
        logger.info(f"Remove duplicates review count: {len(movie_reviews)}")
        movie_reviews = self.remove_unmatched_ratings(movie_reviews)
        logger.info(f"Remove unmatched ratings review count: {len(movie_reviews)}")
        movie_reviews = self.filter_rating(movie_reviews)
        logger.info(f"Filtered ratings review count: {len(movie_reviews)}")

        return movie_reviews

    def db_to_movie_reviews(self, db_reviews):
        return [
            MovieReview(
                anonymous_id=review.customer_id,
                movie_id=review.movie_id,
                movie_name=review.movie.name,
                rating=review.rating,
                review_date=review.review_date,
            )
            for review in db_reviews
        ]

    def remove_na_anonymous_id(self, csv_reviews):
        return [review for review in csv_reviews if review["anonymous_id"].isnumeric()]

    def remove_na_movie_name(self, csv_reviews):
        return [
            review for review in csv_reviews if len(review["movie_name"].strip()) > 0
        ]

    def convert_percent_to_number(self, csv_reviews):
        results = []
        for review in csv_reviews:
            if isinstance(review["rating"], float):
                pass
            elif "%" in review["rating"]:
                review["rating"] = float(review["rating"].replace("%", "")) / 10
            elif re.match(r"\d+.?\d*", review["rating"]):
                review["rating"] = float(review["rating"])
            else:
                continue
            results.append(review)

        return results

    def merge(self, movie_reviews, csv_reviews):
        movie_set = set([(r.movie_id, r.movie_name) for r in movie_reviews])
        movie_dict = {movie_tuple[1]: movie_tuple[0] for movie_tuple in movie_set}

        for review in csv_reviews:
            movie_reviews.append(
                MovieReview(
                    anonymous_id=int(review["anonymous_id"]),
                    movie_id=movie_dict.get(review["movie_name"], 0),
                    movie_name=review["movie_name"],
                    rating=review["rating"],
                    review_date=date.fromisoformat(review["review_date"])
                    if len(review["review_date"].strip()) > 0
                    else None,
                )
            )

        return movie_reviews

    def remove_dupes(self, movie_reviews):
        results = []

        seen = set()
        for review in movie_reviews:
            key = (review.anonymous_id, review.movie_name, round(review.rating, 2))
            if key in seen:
                continue
            seen.add(key)
            results.append(review)

        return results

    def remove_unmatched_ratings(self, movie_reviews):
        rating_map = {}
        for review in movie_reviews:
            key = (review.anonymous_id, review.movie_name)
            if key in rating_map:
                rating_map[key].append(review)
            else:
                rating_map[key] = [review]

        results = [value[0] for value in rating_map.values() if len(value) == 1]

        return results

    def filter_rating(self, movie_reviews):
        return [
            review
            for review in movie_reviews
            if review.rating >= 0.0 and review.rating <= 10.0
        ]


class ETLProcessor:
    def __init__(
        self,
        dbRepository,
        csvRepository,
        movieReviewWriter,
        transformer: Transformer,
    ):
        self._dbRepository = dbRepository
        self._csvRepository = csvRepository
        self._movieReviewWriter = movieReviewWriter
        self._transformer = transformer

    def extract(self):
        db_reviews = self._dbRepository.find_all()
        csv_reviews = self._csvRepository.find_all()
        return db_reviews, csv_reviews

    def load(self, data):
        self._movieReviewWriter.add_all(data)

    def process(self):
        db_reviews, csv_reviews = self.extract()
        transformed_data = self._transformer.transform(db_reviews, csv_reviews)
        self.load(transformed_data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._dbRepository.close()
