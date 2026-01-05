# Single Input

1. Use a `Dropdown` to target qualitative columns: species, island, sex.

2. Use the `@callback` decorator. `Output` should be a `Graph` targeting our `figure`. `Input` should trigger an event, the value, and route it to our function.

    ```py
    @callback(
        Output(component_id="some_id", component_property="figure"),
        Input(component_id="other_id", component_property="value"),
    )
    def route_value_to_figure(value):
        return ...
    ```

    The figure should be a histogram using our X-axis `value`.

3. Use `RadioItems` to target quantitative columns: bill length, bill depth, flipper length.

4. Use the `@callback` decorator. `Output` should be a `Graph` targeting our `figure`. `Input` should trigger an event, the value, and route it to our function.

    The figure should be a scatter plot. Our X-axis is always body mass. Our Y-axis is bill length, bill depth, or flipper length.

5. Create another scatter plot that includes X-axis: body mass and multiple Y-axis: bill length, bill depth, and flipper length. No input required.