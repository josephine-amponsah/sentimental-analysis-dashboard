import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# app = Dash(__name__)
dash.register_page(__name__, path="/dashboard/ad-stats")
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

summaryCard = ["Impressions", "Clicks", "Visits", "Conversions"]
secondSum = ["CTR", "CR", "ROI"]


layout = html.Div([
    dbc.Row([
        dbc.Row([
            dbc.Col([
                  html.Div([
                      html.I(className="bi bi-search"),
                      html.I(className="bi bi-bell-fill"),
                      html.I(className="bi bi-person-circle"),
                  ], className='icon-bar'),
                  ],  width=3)
        ], justify="end"),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row([
            dbc.Col(dbc.Card(
                children=[html.Div(title), html.Div("value", className='value'), html.Div("description")], className='summary-cards',),
                width=3,)
            for title in summaryCard
        ]),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col(dbc.Card(
                        children=[html.Div(title), html.Div("value", className='value'), html.Div("description")], className='summary-cards',),
                    )
                    for title in secondSum
                ]),
                dbc.Row([
                    dcc.Graph(id="bar-ads-chart")
                ])
            ], width=9),
            dbc.Col([
                dbc.Card(children=[html.Div("Charts")])
            ], width=3)
        ], style={"height": "100vh"})
    ], className="dashboard")


])
