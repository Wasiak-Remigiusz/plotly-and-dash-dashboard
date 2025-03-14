import imp
from gc import callbacks
from ntpath import join
from subprocess import call
from typing import List

import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

from components.filtering import data_year_slider

# Import z paczek z aplikacji
from components.static import navbar
from data.external import data_gapminder_df
from graphs.templates import (
    bar_country,
    choropleth_world,
    line_country,
    scatter_gdpPercap,
)

# Tworzenie aplikacji Dash-owej
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


# Wyglad aplikacji (layout)
app.layout = html.Div(
    [
        navbar,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.H5("Display year: "), width=2),
                # dbc.Col(html.B("Display Year: "), width=2),
                dbc.Col(data_year_slider(), width=10),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    id="choropleth-world-col", children=choropleth_world(), width=6
                ),
                dbc.Col(
                    id="scatter-gdpPercap-col",
                    children=scatter_gdpPercap(),
                    width=6,
                    align="center",
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.H5(id="outpout_cointener", children=[]), width=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(id="line-country-col", children=line_country(), width=6),
                dbc.Col(id="bar-country-col", children=bar_country(), width=6),
            ]
        ),
    ],
)

# Callback dal wykresow z gory (1, 2)
@app.callback(
    Output("choropleth-world-col", "children"),
    Output("scatter-gdpPercap-col", "children"),
    Input("data-year-slider", "value"),
)
def update_graphs(selected_year: List[float]):

    return (choropleth_world(selected_year), scatter_gdpPercap(selected_year))


# Callback dla wykresow z dolu (3, 4)
@app.callback(
    Output("line-country-col", component_property="children"),
    Output("bar-country-col", component_property="children"),
    Output("outpout_cointener", component_property="children"),
    Input("choropleth-world", component_property="clickData"),
    prevent_initial_call=True,
)
def update_graphs_3_and_4(clickData: dict):
    if clickData is not None:
        country_selected = clickData["points"][0]["hovertext"]
    else:
        country_selected = "click on the map above"
    container = "Displayed country: {}".format(country_selected)

    return (line_country(clickData), bar_country(clickData), container)


# Zabezpieczenie -> uruchominie wylacznie gdy python-to-this-file.py
server = app.server  # <- Dodanie dla Render.com - Gunicorn
if __name__ == "__main__":
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
