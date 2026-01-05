import os

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)

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
    dcc.Graph(figure=fig_weight_avg_price),
]

if __name__ == "__main__":
    app.run(debug=True)
