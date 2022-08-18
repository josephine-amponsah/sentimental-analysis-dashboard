
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

adsData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\marketingData.csv',  index_col= 0)
revData = pd.read_csv(r'C:\\Users\\HP\\Downloads\\mybooks\\project\\ads-proj\\ad-sales-ml-proj\\data\\revenueData.csv',  index_col= 0)

app.layout = html.Div([
    dbc.Row([
        dbc.Col( 
            html.Div([
            dbc.Nav("LOGO"),
            html.Br(),
            html.Div(
                     [
                         "ANALYTICS",
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")], align = 'left'),
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     ], className =' nav-subtext'),  
            html.Hr(),
            html.Div(
                      [
                          "MENU",
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     dbc.Row([dbc.NavLink("Plan Campaign",href="http://")]),
                     ], className =' nav-subtext'), 
            html.Hr(),
            dbc.Nav(["UTILITIES"], className ='nav-subtext')
            ], className = 'nav-card '),style={"height":"100%"}, 
            width = 2
            ),
        dbc.Col(
                dbc.Row([
        dbc.Row([
            dbc.Col(html.Div("MSG"), width = 3),
            dbc.Col(html.Div("SEARCH"), width = 3),
            dbc.Col(html.Div("NOTIFS & PROFILE"), width = 4),
            ]),
        dbc.Row([]),
                ]),
                className = 'dashboard'
                , width=10)
    ]),
    

])
app.callback()

if __name__ == '__main__':
    app.run_server(debug=True)