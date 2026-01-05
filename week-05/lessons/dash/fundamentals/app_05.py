import os

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)

# transform to a new DataFrame
df_weight_mpg = df.melt(
    id_vars=["Weight"],
    value_vars=["MPG.city", "MPG.highway"],
    var_name="MPG_Type",
    value_name="MPG",
)

app.layout = [
    html.H1("Car93 Data"),
    dcc.Graph(
        figure=px.scatter(
            df_weight_mpg,
            x="Weight",
            y="MPG",
            title="Weight vs MPG",
            color="MPG_Type",
            labels={"MPG_Type": "MPG"},
            trendline="ols",
        )
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
