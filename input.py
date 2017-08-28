import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div([
        dcc.Input(id='my-id', value= 'hi', type='text'),
        html.H1(id = 'my-header', children='header')
        ])

@app.callback(
    Output('my-header', 'children'),
    [Input('my-id', 'value')]
    )
def update(input_value):
    return f'{input_value}'*2

if __name__ == '__main__':
    app.run_server()
