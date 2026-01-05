import os

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash()

# data
parent_dir = os.path.dirname(__file__)
cars93_file = os.path.join(parent_dir, "../../matplotlib/cars93.csv")

df = pd.read_csv(cars93_file)


app.layout = [
    html.H1("Car93 Data"),
    # connect a Graph component to bar chart
    dcc.Graph(
        figure=px.bar(
            df["Cylinders"].value_counts().reset_index(),
            x="Cylinders",
            y="count",
            title="Cylinders vs Car Count",
            labels={"count": "Car Count"},
        )
    ),
]

if __name__ == "__main__":
    app.run(debug=True)
