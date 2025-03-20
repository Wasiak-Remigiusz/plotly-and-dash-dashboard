import dash_bootstrap_components as dbc
from dash import html

world_logo = "https://t3.ftcdn.net/jpg/02/38/16/94/240_F_238169477_Daonex5XsbOWLdcL0x8IcQ91RCJGubDy.jpg"
# second_logo = "https://www.webelfujisoftvara.com/CMSImages/TL_637323403091545348.png"
second_logo = "https://saturn-public-assets.s3.us-east-2.amazonaws.com/example-resources/plotly_dash_logo.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=world_logo, height="90px")),
                    dbc.Col(dbc.NavbarBrand("World data Dashboard", className="ms-2")),
                    # dbc.Col(html.H5("World data Dashboard", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
            dbc.Row([dbc.Col(html.Img(src=second_logo, height="90px"), width=2)]),
        ]
    ),
    color="dark",
    dark=True,
)
