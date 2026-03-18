import pandas as pd


class PlayersETL:

    def __init__(self, csv_path: str, engine):
        self.csv_path = csv_path
        self.engine = engine

    def extract(self):
        df = pd.read_csv(self.csv_path)
        return df

    def transform(self, df):

        df.drop(columns=["id"], inplace=True)

        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        return df

    def load(self, df):

        df.to_sql(
            "player",
            con=self.engine,
            if_exists="append",
            index=False,
        )

    def process(self):
        df = self.extract()
        df = self.transform(df)
        self.load(df)