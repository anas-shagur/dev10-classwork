import os

import pandas as pd
import plotly.express as px
from dash import Dash, dash_table, dcc, Input, Output, callback, html
from dash.exceptions import PreventUpdate

app = Dash()

parent_dir = os.path.dirname(__file__)

sp500_companies_file = os.path.join(parent_dir, "./sp500_companies.csv")
sp500_stocks_file = os.path.join(parent_dir, "./sp500_stocks.csv")

df_companies = pd.read_csv(sp500_companies_file)

df_stocks = pd.read_csv(sp500_stocks_file)
df_stocks = df_stocks.dropna()

fig_sector_distribution = px.histogram(
    df_companies,
    x="Sector",
    title="Sector Distribution",
)

fig_avg_employees_sector = px.histogram(
    df_companies,
    x="Sector",
    y="Fulltimeemployees",
    histfunc="avg",
    title="Average employees per Company Sector"
)

fig_marketcap_to_employeecount = px.scatter(
    df_companies,
    x="Marketcap",
    y="Fulltimeemployees",
    color="Sector",
    size="Marketcap",
    title="Market cap to Employee count"
)

fig_stocks_over_time = px.line(
    df_stocks,
    x="Date",
    y="Close",
    color="Symbol",
    title="Stock Prices over time"
)


app.layout = [
    html.H1("Companies Data"),
    dash_table.DataTable(
        data=df_companies.to_dict("records"), page_size=25, sort_action="native"
    ),
    dcc.Graph(figure=fig_sector_distribution),
    html.Div(
        [
            html.Label("Histogram function"),
            dcc.Dropdown(
                ["count", "sum", "avg", "min", "max"],
                "avg",
                id="ddl-histfunc",
            ),
        ],
        style={"width": "45%", "display": "inline-block", "marginRight": "1rem"},
    ),
    dcc.Graph(figure=fig_avg_employees_sector, id="histogram"),
    dcc.Graph(figure=fig_marketcap_to_employeecount),
    html.Div(
        [
            html.Label("Stocks over time"),
            dcc.Dropdown(
                sorted(df_stocks["Symbol"].unique()),
                value=["AOS", "MMM"],
                multi=True,
                id="ddl-symbols"
            )
        ]
    ),
    dcc.Graph(figure=fig_stocks_over_time, id="line-chart"),
]


@callback(
    Output(component_id="histogram", component_property="figure"),
    Input(component_id="ddl-histfunc", component_property="value")
)
def update_histogram(value):
    fig = px.histogram(
        df_companies,
        x="Sector",
        y="Fulltimeemployees",
        histfunc=value,
        title=f"{value.title()} Employees per Company Sector"
    )
    return fig

@callback(
    Output(component_id="line-chart", component_property="figure"),
    Input(component_id="ddl-symbols", component_property="value")
)
def update_line_graph(selected_symbols):
    if not selected_symbols:
        raise PreventUpdate

    df_filtered_stocks = df_stocks[df_stocks["Symbol"].isin(selected_symbols)]

    fig = px.line(
        df_filtered_stocks,
        x="Date",
        y="Close",
        color="Symbol",
        title="Stock Prices over time"
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
