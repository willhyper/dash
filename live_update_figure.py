import dash
import plotly.graph_objs as go
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from collections import deque
import requests


n = 20
tick = 0
t , t0, t1 = deque([], n), deque([], n), deque([], n)

app = dash.Dash()
app.layout = html.Div([
                    html.H1("Plotly Live update"),
                    dcc.Graph(id='plot', figure=None),
                    dcc.Interval(id='live-update', interval=1000),
                ])

@app.callback(Output('plot','figure'), events=[Event('live-update', 'interval')])
def gen_plot():
    global tick, t, t0, t1
    tick += 1
    t.append(tick)
    t0.append(np.random.randint(10))
    t1.append(np.random.randint(10))

    trace = [go.Scatter(x=list(t), y=list(t0), name='trace0', fill='tozeroy'),
             go.Scatter(x=list(t), y=list(t1), name='trace1', fill='tozeroy'),
             ]

    return dict(data=trace, layout={'title' : 'title',
                                    'xaxis' : {'title':'tick'},
                                    'yaxis' : {'title':'magnitude'}})


if __name__ == '__main__':
    app.run_server(debug=True)
