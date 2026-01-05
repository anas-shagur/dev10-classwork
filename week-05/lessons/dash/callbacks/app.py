import os

import pandas as pd
import plotly.express as px
from car_columns import quantitative_columns
from dash import Dash, Input, Output, callback, dcc, html
from dash.exceptions import PreventUpdate

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)


def render_tab1():
    return [
        html.Div(
            [
                html.Div(
                    [
                        html.Label("X-Axis"),
                        dcc.Dropdown(
                            quantitative_columns,
                            quantitative_columns[0],
                            id="ddl-x",
                            style={"marginBottom": "1rem"},
                        ),
                        dcc.Graph(id="scatter"),
                    ],
                    style={"width": "48%", "marginRight": "1rem"},
                ),
                html.Div(
                    [
                        html.Label("Y-Axis"),
                        dcc.Dropdown(
                            quantitative_columns,
                            quantitative_columns[2],
                            id="ddl-y",
                            multi=True,
                        ),
                        dcc.Graph(id="histogram"),
                    ],
                    style={"width": "48%"},
                ),
            ],
            style={"display": "flex", "marginTop": "2rem"},
        ),
        html.Img(
            src="/assets/1993-lincoln-town-car.jpeg",
            style={
                "width": "85%",
                "height": "auto",
                "margin": "auto",
                "display": "block",
            },
        ),
    ]


def render_tab2():
    return [
        dcc.Graph(
            figure=px.treemap(
                df,
                path=["Manufacturer", "Make", "Model"],
                height=800,
            ),
        ),
        dcc.Graph(
            figure=px.sunburst(
                df,
                path=["Type", "Manufacturer"],
                height=800,
            ),
        ),
    ]


app.layout = [
    html.H1("Cars 93"),
    dcc.Tabs(
        [
            dcc.Tab(render_tab1(), label="Quantitative"),
            dcc.Tab(render_tab2(), label="Categories"),
        ],
    ),
]


@callback(
    Output(component_id="scatter", component_property="figure"),
    Input(component_id="ddl-x", component_property="value"),
    Input(component_id="ddl-y", component_property="value"),
)
def update_scatter_chart(x_axis, y_axis):
    if x_axis is None or y_axis is None or x_axis == y_axis or x_axis in y_axis:
        raise PreventUpdate

    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        trendline="ols",
        labels={"variable": "Y-Values"},
        title=f"{y_axis} vs {x_axis}",
    )
    fig.update_layout(yaxis_title="Y-Values")
    return fig


@callback(
    Output(component_id="histogram", component_property="figure"),
    Input(component_id="ddl-x", component_property="value"),
)
def update_histogram(x_axis):
    fig = px.histogram(
        df,
        x=x_axis,
        title=f"{x_axis} Distribution",
        barmode="group",
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
