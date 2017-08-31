import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import numpy as np

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph(id='graph'),
        dcc.Slider(id='scale', value=1)
    ]
)

x = np.array(range(100))

@app.callback(Output('graph','figure'),[Input('scale','value')])
def update(freq):
    y = np.sin(freq * x)

    return {
        'data': [   go.Scatter(x=x,y=y),
                    go.Scatter(x=x,y=2*y)
                ],
        'layout' : go.Layout(
            xaxis={'title': 't'},
            yaxis={'title': 'magnitude'}
        )
    }

if __name__ == '__main__':
    app.run_server()
