import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

external_stylesheets=[dbc.themes.SPACELAB]

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    # main app framework
                    html.Div(
                        "Python Multipage App with Dash",
                        style={'fontSize':50, 'textAlign':'center'}
                        )
                )
            ]
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [sidebar],
                    # number of columns depending on screensize:
                    xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
                ),
                dbc.Col(
                    #content for each page:
                    [dash.page_container],
                    # number of columns depending on screensize:
                    xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                )
            ]
        )
    ],
    fluid=True
)


if __name__ == "__main__":
    app.run(debug=True)