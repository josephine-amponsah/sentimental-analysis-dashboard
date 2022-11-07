
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

cardNames = ["Titles", "Titles", "Titles", "Titles"]

layout = html.Div([
    dbc.Row([
        dbc.Row([
            dbc.Col(html.Div(
                children=[html.Div("Hi Marketing Manager", style={'fontWeight': 'bold'}), html.Div("Welcome back!")]), width=3),
            dbc.Col(
                html.Div([
                    html.I(className="bi bi-search"),
                    html.I(className="bi bi-bell-fill"),
                    html.I(className="bi bi-person-circle"),
                ], className='icon-bar'), width=3),
        ], justify='between'),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        dbc.Row([
            dbc.Col(html.Div([
                dcc.DatePickerRange(id="dash-date-filter",
                                    month_format='MMM Do, YY',
                                    end_date_placeholder_text='MMM Do, YY',
                                    start_date="03 01 19",
                                    calendar_orientation='horizontal',
                                    day_size=25,
                                    style={'fontSize': '10px', }
                                    ),
                html.Div(id="dash-date-filter-range")],
                className='dashboard-date-filter'
            ), width=4),
            dbc.Col([
                dbc.Button(
                    "DOWNLOAD",
                    className='download-button'
                )], width=2
            )
        ], justify='between', className='filter-bar'),
        html.Br(),
        dbc.Row(style={'height': '20px'}),
        html.Div([
            html.Div([
                html.Div("Analysis Overview"),
                html.Br(),
                dbc.Row([
                    dbc.Col(dbc.Card(
                        children=[html.Div(title), html.Div("value", className='value'), html.Div("description")], className='summary-cards',),
                        width=3,)
                    for title in cardNames
                ], justify="evenly")
            ], className='summary-section'),
            dbc.Row(style={'height': '20px'}),
            html.Div([
                html.Div("graph title"),
                html.Br(),
                dcc.Graph("graph")
            ], className='summary-section')
        ]),
    ],),



])


# @app.callback(Output('page-content', 'children'),
#               [Input('summary-link', 'pathname')])
# def display_page(pathname):
#     return sales.layout if pathname == '/pages/sales' else app.layout
