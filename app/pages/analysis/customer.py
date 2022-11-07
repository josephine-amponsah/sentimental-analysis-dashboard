import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


dash.register_page(__name__, path="/analysis/customer")
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

layout = html.Div([
    html.H1(" Sentimental Analysis", style={"color": "black"}),
])
