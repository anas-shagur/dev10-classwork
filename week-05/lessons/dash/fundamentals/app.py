import os

import pandas as pd
import plotly.express as px
from dash import Dash, dash_table, dcc, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)

df_weight_mpg = df.melt(
    id_vars=["Weight"],
    value_vars=["MPG.city", "MPG.highway"],
    var_name="MPG_Type",
    value_name="MPG",
)

# figures
fig_weight_avg_price = px.histogram(
    df,
    x="Weight",
    y="Price",
    histfunc="avg",
    title="Weight vs Avg Price",
    nbins=14,
)
fig_weight_avg_price.update_layout(yaxis_title="Avg Price", bargap=0.1)


app.layout = [
    html.H1("Car93 Data"),
    dash_table.DataTable(
        data=df.to_dict("records"), page_size=10, sort_action="native"
    ),
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
    dcc.Graph(
        figure=px.box(
            df,
            x="Cylinders",
            y="Price",
            title="Cylinders vs Price",
        )
    ),
    dcc.Graph(
        figure=px.bar(
            df["Cylinders"].value_counts().reset_index(),
            x="Cylinders",
            y="count",
            title="Cylinders vs Car Count",
            labels={"count": "Car Count"},
        )
    ),
    dcc.Graph(figure=fig_weight_avg_price),
    dcc.Graph(
        figure=px.histogram(
            df,
            x="Price",
            title="Price Frequency",
            nbins=7,
        )
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
