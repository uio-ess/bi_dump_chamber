#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq


external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Beam Dump Imaging Chamber Tesing Dashboard'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div([
        html.Div([
            daq.Indicator(
                id="demoBooleanIndicator",
                label=" BooleanSwitch Indicator",
                labelPosition="right",
                value=True
            ),
        ], style={ 'height': '40px' }),
        html.Div([
            daq.Indicator(
                id='demoToggleIndicator',
                label=' ToggleSwitch Indicator',
                labelPosition="right",
                value=False
            )
        ], style={ 'height': '40px' }),
        html.Div([
            daq.Indicator(
                id="demoIndicator",
                label="Stop Button Indicator",
                labelPosition="right",
                value=True
            )
        ], style={ 'height': '40px' }),
        html.Div([
            daq.Indicator(
                id='demoPowerIndicator',
                label=' Power Indicator',
                labelPosition="right",
                value=False
            )
        ], style={ 'height' : '40px' }),
        html.Div([
            daq.NumericInput(
                id='goto',
                value=0,
                min=-300.0,
                max=300.0
            )
        ]),
    ], style = {
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'space-between'
    }),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)