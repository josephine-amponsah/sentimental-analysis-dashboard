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
            dbc.Col( 
            html.Div([
            dbc.Nav("LOGO"),
            html.Br(),
            # html.Div(
            #          [
            #              "ANALYTICS",
            #          dbc.Row([dbc.NavLink("Overview",href=dash.page_registry['pages.dashboard.overview']['path'])]),
            #          dbc.Row([dbc.NavLink("Ads Stats",href=dash.page_registry['pages.dashboard.ads-stats']['path'])]),
            #          dbc.Row([dbc.NavLink("Sales Stats",href=dash.page_registry['pages.dashboard.sales-stats']['path'])])
            #          ], className =' nav-subtext'), 
              html.Div ('Dashboard'),
            html.Div (
                [
                
                    dbc.Row([dbc.NavLink(page["name"], href = page['path'], className="nav-subtext")],)
                for page in dash.page_registry.values()
                if page["path"].startswith("/dashboard")
                ]
                ),
            html.Div ('Analysis'),
            html.Div (
                [
                    dbc.Row(
                    [
                        dbc.NavLink(page["name"], href = page['path'], className="nav-subtext"),
                    ],
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/analysis")
                ]
                ),
            html.Hr(),
            dbc.Nav(["UTILITIES"], className ='nav-subtext')
            ], className = 'nav-card '),style={"height":"100%"}, 
            width = 2
         )
    , dash.page_container
]),
    # dash.page_container
]
)








if __name__ == '__main__':
    app.run_server(debug=True)