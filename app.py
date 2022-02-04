# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 07:33:49 2019

@author: yangky
"""

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

data = pd.read_csv("data/gis_data.csv", header=0)

dataFilter = data[["SALE_YEAR","SALESAMT"]]
dataFilter = data[data["SALESAMT"]>0]
dataFilter = dataFilter.groupby("SALE_YEAR").agg({"SALESAMT":np.mean}).reset_index()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            #Would like the data to come from Data Lake or Azure SQL
            'data': [
                {'x': dataFilter["SALE_YEAR"], 'y': dataFilter["SALESAMT"], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'AVG Home Prices in G-TOWN Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
