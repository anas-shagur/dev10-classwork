from datetime import date

from dash import Dash, dcc, html

app = Dash()


app.layout = [
    html.H1("Cars93 Data"),
    html.Div(children=[dcc.DatePickerSingle(date=date.today())]),
]

if __name__ == "__main__":
    app.run(debug=True)
