import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

x = np.array(range(100))
y = np.sin(x/100)

fig = {
        'data': [   go.Scatter(x=x,y=y,name='line'),
                    go.Scatter(x=x,y=2*y, mode='markers',name='dot'),

                ],
        'layout' : go.Layout(
            xaxis={'title': 't'},
            yaxis={'title': 'magnitude'}
        )
}

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph(id='graph', figure=fig)
    ]
)

if __name__ == '__main__':
    app.run_server()
