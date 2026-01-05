import os

import pandas as pd
import plotly.express as px
from car_columns import category_columns, quantitative_columns
from dash import Dash, Input, Output, callback, dcc, html
from dash.exceptions import PreventUpdate

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)


app.layout = [
    html.H1("Car 93"),
    html.Div(
        [
            html.Div(
                [
                    html.Label("Categories"),
                    dcc.Dropdown(
                        category_columns,
                        category_columns[0],
                        id="ddl-categories",
                    ),
                    html.Label("Quantitative Values"),
                    dcc.Dropdown(
                        quantitative_columns,
                        quantitative_columns[0],
                        id="ddl-quantitative",
                    ),
                    html.Label("Histogram Function"),
                    dcc.Dropdown(
                        ["count", "sum", "avg", "min", "max"],
                        "count",
                        id="ddl-histfunc",
                    ),
                    dcc.Graph(id="histogram"),
                ],
                style={"width": "45%", "marginRight": "1rem"},
            ),
            dcc.Graph(id="histogram-details", style={"width": "45%"}),
        ],
        style={"display": "flex"},
    ),
]


@callback(
    Output(component_id="histogram", component_property="figure"),
    Input(component_id="ddl-categories", component_property="value"),
    Input(component_id="ddl-quantitative", component_property="value"),
    Input(component_id="ddl-histfunc", component_property="value"),
)
def update_bar_chart(category, quantitative, histfunc):
    fig = px.histogram(
        df,
        x=category,
        y=quantitative,
        title=f"{quantitative} vs {category}",
        barmode="group",
        histfunc=histfunc,
    )
    fig.update_layout(yaxis_title=f"{histfunc} ({quantitative})")
    fig.update_traces(customdata=df[category])
    return fig


@callback(
    Output(component_id="histogram-details", component_property="figure"),
    Input(component_id="histogram", component_property="clickData"),
    Input(component_id="ddl-categories", component_property="value"),
    Input(component_id="ddl-quantitative", component_property="value"),
)
def update_histogram_details(click_data, category, quantitative):
    if not click_data:
        raise PreventUpdate

    category_value = click_data["points"][0]["customdata"][0]
    df_filtered = df[df[category] == category_value]
    fig = px.histogram(
        df_filtered,
        x=quantitative,
        title=f"{category} ({category_value}) {quantitative} Distribution",
    )
    fig.update_layout(bargap=0.05)
    return fig


if __name__ == "__main__":
    app.run(debug=True)
