import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import numpy as np

app = dash.Dash()


x = np.linspace(0, 2, num=100)

app.layout = html.Div(
    [
        dcc.Graph(id='graph'),
        dcc.Slider(id='scale', value=x[0], min= min(x), max = max(x), step=x[1]-x[0])
    ]
)

@app.callback(Output('graph','figure'),[Input('scale','value')])
def update(until):
    y = - x * np.log(x)

    xx, yy = x[x<until], y[x<until]
    
    return {
        'data': [   go.Scatter(x=x,y=y),
                    go.Scatter(x=xx,y=yy, fill='tozeroy')
                ],
        'layout' : go.Layout(
            xaxis={'title': 't'},
            yaxis={'title': 'magnitude'}
        )
    }

if __name__ == '__main__':
    app.run_server()
