import os

import pandas as pd
from dash import Dash, dash_table, html

app = Dash()

# data
os.chdir(os.path.dirname(__file__))

df = pd.read_csv("penguins.csv")


app.layout = [
    html.H1("Palmer Penguins"),
    dash_table.DataTable(
        data=df.to_dict("records"), page_size=10, sort_action="native"
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
