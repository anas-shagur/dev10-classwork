import pandas as pd


class Transformer:
    def transform(self, df):
        return df


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
        pass
        # sql = ""
        # return pd.read_sql(sql, self._cnx)

    def extract_csv(self):
        pass
        # return pd.read_csv(self._csv_path)

    def extract(self):
        pass
        # df = self.extract_sql()
        # csv_df = self.extract_csv()

        # return pd.concat([df, csv_df])

    def load(self, df):
        # pass
        df.to_csv(self._load_path, index=False)

    def process(self):
        pass
        # df = self.extract()
        # df = self._transformer.transform(df)
        # self.load(df)
