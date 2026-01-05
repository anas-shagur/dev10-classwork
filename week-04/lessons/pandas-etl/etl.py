import logging
import re

import pandas as pd

logger = logging.getLogger(__name__)


def convert_percent_to_number(value):
    if isinstance(value, float):
        return value
    elif "%" in value:
        return float(value.replace("%", "")) / 10
    elif re.match(r"\d+.?\d*", value):
        return float(value)
    return 0.0


class Transformer:
    def transform(self, df):
        logger.info(f"original: {len(df)}")

        df = self.drop_na_customer_id_movie_name_rating(df)
        logger.info(f"drop na: {len(df)}")

        df = self.convert_data_types(df)
        logger.info(f"convert: {len(df)}")

        df = self.drop_duplicates(df)
        logger.info(f"drop dupes: {len(df)}")

        df = self.remove_unmatched_ratings(df)
        logger.info(f"remove non-matched ratings: {len(df)}")

        df = self.filter_ratings(df)
        logger.info(f"filter 0 <= rating >= 10: {len(df)}")

        return df

    def drop_na_customer_id_movie_name_rating(self, df):
        return df.dropna(subset=["customer_id", "movie_name", "rating"])

    def convert_data_types(self, df):
        df = df.copy()
        df["customer_id"] = df["customer_id"].astype(int)
        df["rating"] = df["rating"].apply(convert_percent_to_number).astype(float)
        return df

    def drop_duplicates(self, df):
        return df.drop_duplicates(subset=["customer_id", "movie_name", "rating"])

    def remove_unmatched_ratings(self, df):
        return df[~df.duplicated(subset=["customer_id", "movie_name"], keep=False)]

    def filter_ratings(self, df):
        condition = (df["rating"] >= 0.0) & (df["rating"] <= 10.0)
        return df[condition]


class ETLProcessor:
    def __init__(
        self,
        cnx,
        csv_path,
        load_path,
        transformer: Transformer,
    ):
        self._cnx = cnx
        self._csv_path = csv_path
        self._load_path = load_path
        self._transformer = transformer

    def extract_sql(self):
        sql = """
            SELECT
                c.customer_id,
                m.`name` movie_name,
                g.`name` genre,
                r.rating,
                r.review_date
            FROM review r
            INNER JOIN customer c ON r.customer_id = c.customer_id
            INNER JOIN movie m ON r.movie_id = m.movie_id
            INNER JOIN genre g ON m.genre_id = g.genre_id;
            """

        return pd.read_sql(sql, self._cnx)

    def extract_csv(self):
        return pd.read_csv(self._csv_path)

    def extract(self):
        df = self.extract_sql()

        csv_df = self.extract_csv()
        csv_df.rename(columns={"anonymous_id": "customer_id"}, inplace=True)

        return pd.concat([df, csv_df])

    def load(self, df):
        df.to_csv(self._load_path, index=False)

    def process(self):
        df = self.extract()
        df = self._transformer.transform(df)
        self.load(df)
