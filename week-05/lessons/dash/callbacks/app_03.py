import os

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)


app.layout = [
    html.H1("Car93"),
    dcc.RadioItems(
        ["Price", "Max.Price", "MPG.city", "Horsepower", "RPM", "Length", "Width"],
        "Price",
        inline=True,
        id="rdi-input",
    ),
    dcc.Graph(id="scatter-plot"),
]


@callback(
    Output(component_id="scatter-plot", component_property="figure"),
    Input(component_id="rdi-input", component_property="value"),
)
def update_scatter_plot(value):
    fig = px.scatter(
        df, x="Weight", y=value, trendline="ols", title=f"{value} vs Weight"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
