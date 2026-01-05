from dash import Dash, html, Input, Output, callback
from dash_daq import ColorPicker

app = Dash()

app.layout = [
    html.H1("Colors"),
    ColorPicker(id="ddl-color", value=dict(hex="#f5a3a3")),
    html.Div(id="color-div"),
]


# the decorator "listens".
# Output must proceed Input.
@callback(
    Output(component_id="color-div", component_property="style"),
    Input(component_id="ddl-color", component_property="value"),
)
def update_color_div(value):
    return {"backgroundColor": value.get("hex"), "height": "75vh"}


if __name__ == "__main__":
    app.run(debug=True)
