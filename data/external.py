import pandas as pd
import plotly.express as px


# Import danych z biblioteki Plotly
def data_gapminder_df() -> pd.DataFrame:
    return px.data.gapminder().round(2)
