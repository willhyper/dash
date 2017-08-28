import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
            dcc.Dropdown(
                id='dropdown',
                options=[{'label': i, 'value': i} for i in range(10)],
                value='initial value'),
            html.H1(id='header')
                        ])

@app.callback(Output('header', 'children'),
[Input('dropdown', 'value')])
def update(input_value):
    return f'{input_value}'
if __name__ == '__main__':
    app.run_server()
