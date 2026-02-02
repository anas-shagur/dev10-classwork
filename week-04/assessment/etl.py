import pandas as pd

#drops genre column and changes movieId to movie_id to match the schema
class TransformMovies:
    def transform(self, df):
        df = df.drop(columns=["genres"])

        df.rename(columns={"movieId": "movie_id"}, inplace=True)

        return df


#drops the timestamp column and changes userId to user_id and movieId to movie_id to match the schema
class TransformRatings:
    def transform(self, df):
        
        df = df.drop(columns=["timestamp"])

        df.rename(columns={"userId": "user_id", "movieId": "movie_id"},inplace=True)

        return df


class ETLProcessor:

    def __init__(self, engine, movies_path, ratings_path):
        self._engine = engine
        self._movies_path = movies_path
        self._ratings_path = ratings_path

    def _extract_movies(self):
        return pd.read_csv(self._movies_path)

    def _extract_ratings(self):
        return pd.read_csv(self._ratings_path)

    def _load_movies(self, df):
        df.to_sql("movie", con=self._engine, if_exists="append", index=False)

    def _load_ratings(self, df):
        df.to_sql("movie_rating", con=self._engine, if_exists="append", index=False)

    def process(self):
        movies_df = self._extract_movies()
        movies_df = TransformMovies().transform(movies_df)
        self._load_movies(movies_df)

        ratings_df = self._extract_ratings()
        ratings_df = TransformRatings().transform(ratings_df)
        self._load_ratings(ratings_df)
