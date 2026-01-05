from dash import Dash, html, dcc, Input, Output, callback

app = Dash()

app.layout = [
    html.H1("Simple Callbacks"),
    # dcc.Input
    html.Div(
        [
            dcc.Input(id="txt-input", type="text", value="Apples"),
            html.Div(id="txt-output-div"),
        ],
        style={"marginBottom": "1rem"},
    ),
    # dcc.Dropdown
    html.Div(
        [
            dcc.Dropdown(["Hydrogen", "Helium", "Lithium"], "Helium", id="ddl-input"),
            html.Div(id="ddl-output-div"),
        ],
        style={"marginBottom": "1rem"},
    ),
    # dcc.Slider
    html.Div(
        [
            dcc.Slider(min=0, max=10, step=1, value=5, id="sld-input"),
            html.Div(id="sld-output-div"),
        ],
        style={"marginBottom": "1rem"},
    ),
    # dcc.RadioItems
    html.Div(
        [
            dcc.RadioItems(
                ["Berlin", "Beijing", "Banjul"], "Banjul", id="rdi-input", inline=True
            ),
            html.Div(id="rdi-output-div"),
        ],
        style={"marginBottom": "1rem"},
    ),
]


@callback(
    Output(component_id="txt-output-div", component_property="children"),
    Input(component_id="txt-input", component_property="value"),
)
def update_txt_output_div(value):
    return value


@callback(
    Output(component_id="ddl-output-div", component_property="children"),
    Input(component_id="ddl-input", component_property="value"),
)
def update_ddl_output_div(value):
    return value


@callback(
    Output(component_id="sld-output-div", component_property="children"),
    Input(component_id="sld-input", component_property="value"),
)
def update_sld_output_div(value):
    return value


@callback(
    Output(component_id="rdi-output-div", component_property="children"),
    Input(component_id="rdi-input", component_property="value"),
)
def update_rdi_output_div(value):
    return value


if __name__ == "__main__":
    app.run(debug=True)
