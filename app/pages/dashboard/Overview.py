
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# from app.pages import sales

dash.register_page(__name__, path="/dashboard/")
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# server = app.server

# adsData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\marketingData.csv',  index_col= 0)
# revData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\revenueData.csv',  index_col= 0)
# salesData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\WebTransactionsCSV.csv',  sep=';', header= 0 )

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


# @app.callback(Output('page-content', 'children'),
#               [Input('summary-link', 'pathname')])
# def display_page(pathname):
#     return sales.layout if pathname == '/pages/sales' else app.layout
