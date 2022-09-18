import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output


# Connect to main app.py file
import home
from home import app
from home import server


# Connect to your app pages
from pages import sales, optimize, customerrev, campaign


# Navbar
navbar = dbc.Col( 
            html.Div([
            dbc.Nav("LOGO"),
            html.Br(),
            html.Div(
                     [
                         "ANALYTICS",
                     dbc.Row([dbc.NavLink("Customer Review Analysis",href="")], align = 'left'),
                     dbc.Row([dbc.NavLink("Customer Review Analysis",href="/pages/sales")]),
                     ], className =' nav-subtext'),  
            html.Hr(),
            html.Div(
                      [
                          "MENU",
                     dbc.Row([dbc.NavLink("Plan Campaign",href="")]),
                     dbc.Row([dbc.NavLink("Projections",href=" ")]),
                     dbc.Row([dbc.NavLink("Customer",href="")]),
                     ], className =' nav-subtext'), 
            html.Hr(),
            dbc.Nav(["UTILITIES"], className ='nav-subtext')
            ], className = 'nav-card '),style={"height":"100%"}, 
            width = 2
            ),


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', children=[])
])


# Not making a 404 page, routing it directly to home
default_template = app.layout


@home.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/sales':
        return sales.layout
    elif pathname == '/apps/campaign':
        return campaign.layout
    elif pathname == '/apps/optimize':
        return optimize.layout
    elif pathname == '/apps/customerrev':
        return customerrev.layout
    else:
        return default_template


if __name__ == '__main__':
    home.run_server(debug=True)