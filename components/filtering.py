from typing import List

import dash_bootstrap_components as dbc
from dash import dcc, html
from data.external import data_gapminder_df
from matplotlib.pyplot import text
from pyparsing import White


# Funkcja, ktora tworzy slider
def data_year_slider() -> dcc.Slider:
    df = data_gapminder_df()
    min_ = df.year.min()
    max_ = df.year.max()
    # all_years_ = df.year.nunique()

    # Tworzenie range na lata
    data_year_steps = range(min_, max_ + 1, 5)

    # Tworzenie slownika
    marks = {steps: f"{steps}" for steps in data_year_steps}

    # Tworzenie slider
    slider = dcc.Slider(
        min=min_,
        max=max_,
        step=5,
        marks=marks,
        value=min_,
        included=False,
        id="data-year-slider",
    )
    return slider
