import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



# from app.pages import sales

app = Dash(__name__, use_pages = True)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Col( 
            html.Div([
            dbc.Nav("LOGO"),
            html.Br(),
            html.Div(
                     [
                         "ANALYTICS",
                     dbc.Row([
                         dbc.NavLink(page["name"],href= page["path" ]) 
                              for page in dash.page_registry.values()
                        if page["path"].startswith("app\pages\dashboard")
                              ], align = 'left'),
                     
                     ], className =' nav-subtext'),  
            html.Hr(),
            html.Div(
                      [
                          "MENU",
                     dbc.Row([dbc.NavLink("Plan Campaign",href=[])]),
                     dbc.Row([dbc.NavLink("Projections",href="http://")]),
                     dbc.Row([dbc.NavLink("Customer",href="http://")]),
                     ], className =' nav-subtext'), 
            html.Hr(),
            dbc.Nav(["UTILITIES"], className ='nav-subtext')
            ], className = 'nav-card '),style={"height":"100%"}, 
            width = 2
         ),
        
        dash.page_container
    ])
])
]
)








if __name__ == '__main__':
    app.run_server(debug=True)