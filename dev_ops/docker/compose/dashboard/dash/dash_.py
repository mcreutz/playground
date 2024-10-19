import random
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq


app = dash.Dash(__name__)

data = []

app.layout = html.Div([
        html.Div(id='Axis', children=[
                daq.Gauge(
                id='my-daq-gauge',
                showCurrentValue=True,
                units="NM",
                label='Axis 01 Torque',
                min=0,
                max=10,
                value=0
                ),
                dcc.Graph(id='example-graph',)
        ]),
        dcc.Interval(
                id='interval-component',
                interval=300, # in milliseconds
                n_intervals=0
        )
])


@app.callback(Output('my-daq-gauge', 'value'),
              Input('interval-component', 'n_intervals'))
def update_gauge(n):
    secs = datetime.datetime.now().second % 10
    val = secs + random.random()
    return val


@app.callback(Output('example-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):
    secs = datetime.datetime.now().second % 10
    val = secs + random.random()
    global data
    data.append(val)

    if len(data) > 300:
        data = data[1:]

    figure={
            'data': [
                {'x': list(range(len(data))), 'y': data, 'type': 'line', 'name': 'values'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'uirevision': 'fix', # any non-changing value
            }
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
