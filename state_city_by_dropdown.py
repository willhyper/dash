import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from collections import defaultdict

app = dash.Dash()

d = defaultdict(list)
d['CA'].append('San Jose')
d['CA'].append('San Francisco')
d['CA'].append('Santa Rosa')
d['CA'].append('Oakland')
d['CA'].append('San Mateo')

d['MD'].append('Columbia')
d['MD'].append('Greenbelt')
d['MD'].append('College Park')
d['MD'].append('Laural')

states = d.keys()
app.layout = html.Div([
    dcc.Dropdown(id='state',options=[{'label': s, 'value': s} for s in states]),
    dcc.Dropdown(id='city', options=None),
    html.H1(id='header')
                    ])

@app.callback(Output('city','options'),
            [Input('state','value')]
            )
def update_city_list(state):
    return [{'label': c, 'value': c} for c in d[state]]

@app.callback(Output('city','value'),
            [Input('city','options')]
            )
def update_city_default(city_options): # this is the trivial part
    return city_options[0]['value']

@app.callback(Output('header','children'),
            [   Input('state','value'),
                Input('city','value')   ]
            )
def update_header(state, city):
    return f'{state}: {city}'

if __name__ == '__main__':
    app.run_server()
