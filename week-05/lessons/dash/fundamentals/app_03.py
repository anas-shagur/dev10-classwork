import os

import pandas as pd
from dash import Dash, dash_table, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)


app.layout = [
    html.H1("Car93 Data"),
    dash_table.DataTable(
        data=df.to_dict("records"), page_size=10, sort_action="native"
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
