import dash_bootstrap_components as dbc
from dash import html

world_logo = "assets/images/world.jpg"
second_logo = "assets/images/plotly_dash_logo.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=world_logo, height="90px")),
                    dbc.Col(dbc.NavbarBrand([
        "World data ",
        html.Span("Dash", style={"color": "#3f4f75"}), # Dash Color
        "board", html.Span(".", style={"color": "rgba(127,205,189,1)", "fontSize": "3.5rem"})  # Dash Color
    ], className="ms-3 nav-title")),
                ],
                align="center",
                className="g-0",
                # wyśrodkowanie w poziomie
                # justify="center", 
                # className="g-0 w-100",
            ),
            dbc.Row([dbc.Col(html.Img(src=second_logo, height="90px"), width=2)]),
        ]
    ),
    color="dark",
    dark=True,
)
