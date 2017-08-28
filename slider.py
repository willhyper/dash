import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

choices = {str(x): str(x) for x in range(7)}

app = dash.Dash()

app.layout = html.Div([
    dcc.Slider(
        id='year-slider',
        min=min(choices),
        max=max(choices),
        value=min(choices),
        step=2,
        marks=choices
    ),

    html.Div(id='output'),

    dcc.Slider(id='slider2',)
])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='slider2', component_property='value')]
)
def update_output_div(input_value):
    return f'{input_value}'

if __name__ == '__main__':
    app.run_server()
