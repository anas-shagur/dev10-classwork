import os

import pandas as pd
import plotly.express as px
from car_columns import category_columns, quantitative_columns
from dash import Dash, Input, Output, callback, dcc, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)


app.layout = [
    html.H1("Car93"),
    html.Div(
        [
            html.Label("Categories"),
            dcc.Dropdown(
                category_columns,
                category_columns[0],
                id="ddl-categories",
            ),
        ],
        style={"width": "45%", "display": "inline-block", "marginRight": "1rem"},
    ),
    html.Div(
        [
            html.Label("Quantitative Values"),
            dcc.Dropdown(
                quantitative_columns,
                quantitative_columns[0],
                id="ddl-quantitative",
            ),
        ],
        style={"width": "45%", "display": "inline-block"},
    ),
    dcc.Graph(id="box-plot"),
]


@callback(
    Output(component_id="box-plot", component_property="figure"),
    Input(component_id="ddl-categories", component_property="value"),
    Input(component_id="ddl-quantitative", component_property="value"),
)
def update_box_plot(category, quantitative):
    fig = px.box(df, x=category, y=quantitative, title=f"{quantitative} vs {category}")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
