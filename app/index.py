import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# from app.pages import sales

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
            dbc.Col(
                html.Div([
                    dbc.Nav("LOGO"),
                    html.Br(),
                    html.Div('Dashboard'),
                    html.Div(
                        [
                            dbc.Row(
                                [dbc.NavLink(page["name"], href=page['path'], className="nav-subtext")],)
                            for page in dash.page_registry.values()
                            if page["path"].startswith("/dashboard")
                        ]
                    ),
                    html.Div('Analysis'),
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.NavLink(
                                        page["name"], href=page['path'], className="nav-subtext"),
                                ],
                            )
                            for page in dash.page_registry.values()
                            if page["path"].startswith("/analysis")
                        ]
                    ),
                    html.Hr(),

                ], className='nav-card '), style={"height": "100%"},
                width=2
            ),
            dbc.Col(dash.page_container)
            ])
]
)


if __name__ == '__main__':
    app.run_server(debug=True)
