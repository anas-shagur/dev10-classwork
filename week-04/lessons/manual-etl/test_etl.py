from datetime import date
from unittest.mock import MagicMock

from alchemy_models import Customer, Genre, Movie, Review
from etl import ETLProcessor, Transformer


def generate_db_reviews():
    g = Genre(name="Genre")
    movies = [
        Movie(movie_id=1, name="Movie 1", genre=g),
        Movie(movie_id=2, name="Movie 2", genre=g),
        Movie(movie_id=3, name="Movie 3", genre=g),
    ]
    customers = [
        Customer(customer_id=1, name="Customer 1", email="one@example.com"),
        Customer(customer_id=2, name="Customer 2", email="two@example.com"),
        Customer(customer_id=3, name="Customer 3", email="three@example.com"),
    ]
    reviews = []
    rating = 2.5
    for movie in movies:
        for customer in customers:
            reviews.append(
                Review(
                    movie_id=movie.movie_id,
                    movie=movie,
                    customer_id=customer.customer_id,
                    customer=customer,
                    rating=rating,
                    review_date=date.today(),
                )
            )
            rating += 0.5
            if rating > 10.0:
                rating = 2.5

    return reviews


def generate_csv_reviews():
    return [
        {
            "anonymous_id": "1",
            "movie_name": "Movie 1",
            "rating": "2.5",
            "review_date": date.today().isoformat(),
        },
        {
            "anonymous_id": "2",
            "movie_name": "Movie 2",
            "rating": "3.0",
            "review_date": date.today().isoformat(),
        },
        {
            "anonymous_id": "3",
            "movie_name": "Movie 3",
            "rating": "3.5",
            "review_date": date.today().isoformat(),
        },
        {
            "anonymous_id": "3",
            "movie_name": "Movie 4",
            "rating": "35%",
            "review_date": date.today().isoformat(),
        },
        {
            "anonymous_id": "",
            "movie_name": "Movie 4",
            "rating": "3.5",
            "review_date": date.today().isoformat(),
        },
        {
            "anonymous_id": "5",
            "movie_name": "",
            "rating": "3.5",
            "review_date": date.today().isoformat(),
        },
        {
            "anonymous_id": "5",
            "movie_name": "Movie 5",
            "rating": "13.5",
            "review_date": date.today().isoformat(),
        },
    ]


def generate_etl_processor():
    dbRepository = MagicMock()
    dbRepository.find_all.return_value = generate_db_reviews()

    csvRepository = MagicMock()
    csvRepository.find_all.return_value = generate_csv_reviews()
    movieReviewWriter = MagicMock()

    transformer = Transformer()

    return ETLProcessor(
        dbRepository,
        csvRepository,
        movieReviewWriter,
        transformer,
    )


class TestETLProcessor:
    processor = generate_etl_processor()

    def test_extract(self):
        db_reviews, csv_reviews = self.processor.extract()
        assert len(db_reviews) == 9
        assert len(csv_reviews) == 7

    def test_transform(self):
        db_reviews, csv_reviews = self.processor.extract()
        transformed_data = self.processor._transformer.transform(
            db_reviews, csv_reviews
        )
        assert len(transformed_data) == 8


class TestTransformer:
    transformer = Transformer()

    def clean_db(self):
        db_reviews = generate_db_reviews()
        return self.transformer.db_to_movie_reviews(db_reviews)

    def clean_csv(self):
        csv_reviews = generate_csv_reviews()
        csv_reviews = self.transformer.remove_na_anonymous_id(csv_reviews)
        csv_reviews = self.transformer.remove_na_movie_name(csv_reviews)
        return self.transformer.convert_percent_to_number(csv_reviews)

    def merge(self):
        return self.transformer.merge(self.clean_db(), self.clean_csv())

    def test_db_to_movie_reviews(self):
        db_reviews = generate_db_reviews()
        len_reviews = len(db_reviews)
        movie_reviews = self.transformer.db_to_movie_reviews(db_reviews)
        assert len(movie_reviews) == len_reviews

    def test_remove_na_anonymous_id(self):
        csv_reviews = generate_csv_reviews()
        len_reviews = len(csv_reviews)
        csv_reviews = self.transformer.remove_na_anonymous_id(csv_reviews)
        assert len(csv_reviews) == len_reviews - 1

    def test_remove_na_movie_name(self):
        csv_reviews = generate_csv_reviews()
        len_reviews = len(csv_reviews)
        csv_reviews = self.transformer.remove_na_movie_name(csv_reviews)
        assert len(csv_reviews) == len_reviews - 1

    def test_convert_percent_to_number(self):
        csv_reviews = generate_csv_reviews()
        len_reviews = len(csv_reviews)
        csv_reviews = self.transformer.convert_percent_to_number(csv_reviews)
        assert len(csv_reviews) == len_reviews

    def test_merge(self):
        movie_reviews = self.clean_db()
        csv_reviews = self.clean_csv()

        len_csv_reviews = len(csv_reviews)
        len_movie_reviews = len(movie_reviews)

        movie_reviews = self.transformer.merge(movie_reviews, csv_reviews)

        assert len(movie_reviews) == len_csv_reviews + len_movie_reviews

    def test_remove_dupes(self):
        results = self.merge()
        length = len(results)
        result = self.transformer.remove_dupes(results)
        assert len(result) == length - 1

    def test_remove_unmatched_ratings(self):
        results = self.merge()
        results = self.transformer.remove_dupes(results)
        length = len(results)
        results = self.transformer.remove_unmatched_ratings(results)
        assert len(results) == length - 4

    def test_filter_ratings(self):
        results = self.merge()
        results = self.transformer.remove_dupes(results)
        results = self.transformer.remove_unmatched_ratings(results)
        length = len(results)
        results = self.transformer.filter_rating(results)
        assert len(results) == length - 1
