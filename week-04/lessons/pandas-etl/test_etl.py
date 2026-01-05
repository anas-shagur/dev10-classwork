from datetime import date
from unittest.mock import MagicMock

from etl import ETLProcessor, Transformer

import pandas as pd


def generate_db_reviews():
    return pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 1, 2, 3, 1, 2, 3],
            "movie_name": [
                "Movie 1",
                "Movie 1",
                "Movie 1",
                "Movie 2",
                "Movie 2",
                "Movie 2",
                "Movie 3",
                "Movie 3",
                "Movie 3",
            ],
            "genre": ["Genre"] * 9,
            "rating": [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5],
            "review_date": [date.today()] * 9,
        }
    )


def generate_csv_reviews():
    return pd.DataFrame(
        {
            "anonymous_id": ["1", "2", "3", "3", None, "5", "5"],
            "movie_name": [
                "Movie 1",
                "Movie 2",
                "Movie 3",
                "Movie 4",
                "Movie 4",
                None,
                "Movie 5",
            ],
            "genre": ["Genre"] * 7,
            "rating": ["2.5", "3.0", "3.5", "35%", "3.5", "3.5", "13.5"],
            "review_date": [date.today().isoformat()] * 7,
        }
    )


def generate_etl_processor():
    processor = ETLProcessor(
        None,
        "",
        "",
        Transformer(),
    )

    processor.extract_sql = MagicMock(return_value=generate_db_reviews())
    processor.extract_csv = MagicMock(return_value=generate_csv_reviews())

    return processor


class TestTransformer:
    processor = generate_etl_processor()
    transformer = Transformer()

    def test_drop_na_customer_id_movie_name_rating(self):
        df = self.processor.extract()
        length = len(df)
        df = self.transformer.drop_na_customer_id_movie_name_rating(df)
        assert len(df) == length - 2

    def test_convert_data_types(self):
        df = self.processor.extract()
        df = self.transformer.drop_na_customer_id_movie_name_rating(df)
        length = len(df)
        df = self.transformer.convert_data_types(df)
        assert len(df) == length
        assert df["customer_id"].dtype == "int64"
        assert df["rating"].dtype == "float64"

    def test_drop_duplicates(self):
        df = self.processor.extract()
        df = self.transformer.drop_na_customer_id_movie_name_rating(df)
        df = self.transformer.convert_data_types(df)
        length = len(df)
        df = self.transformer.drop_duplicates(df)
        assert len(df) == length - 1

    def test_remove_unmatched_ratings(self):
        df = self.processor.extract()
        df = self.transformer.drop_na_customer_id_movie_name_rating(df)
        df = self.transformer.convert_data_types(df)
        df = self.transformer.drop_duplicates(df)
        length = len(df)
        df = self.transformer.remove_unmatched_ratings(df)
        assert len(df) == length - 4

    def test_filter_ratings(self):
        df = self.processor.extract()
        df = self.transformer.drop_na_customer_id_movie_name_rating(df)
        df = self.transformer.convert_data_types(df)
        df = self.transformer.drop_duplicates(df)
        df = self.transformer.remove_unmatched_ratings(df)
        length = len(df)
        df = self.transformer.filter_ratings(df)
        assert len(df) == length - 1


class TestETLProcessor:
    processor = generate_etl_processor()

    def test_extract(self):
        df = self.processor.extract()
        assert len(df) == 16

    def test_transform(self):
        df = self.processor.extract()
        df = self.processor._transformer.transform(df)
        assert len(df) == 8
