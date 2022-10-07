import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


dash.register_page(__name__, path = "/analysis/planning")
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

layout = html.Div([
     html.Div(" Optimzation"),
])

