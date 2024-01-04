#import os
#os.getcwd()

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from app_instance import app
from components import update_output
from vizualization import summary_graph


sidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(
                    page["name"], className="ms-2"
                )
            ],
            href=page["path"],
            active="exact",
        ) for page in dash.page_registry.values()
    ],
    vertical=True,
    pills=True,
    className="bg-light",
)

app.layout = dbc.Container(
    [
        dcc.Store(id='stored-data'), # invisible component, stores data into users browser, max 2-3MB (can't use for very large files)
        dbc.Row(
            [
                dbc.Col(
                    [
                      html.Div(
                          "Domino eNPS Sentiment Analysis with Dash",
                            style={
                                'fontsize':50,
                                'textAlign':'center'
                        }
                      )  
                    ]
                    
                )
            ]
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [sidebar],
                    xs=4, sm=4, md=2, lg=2, xl=2, xxl=2
                ),
                dbc.Col(
                    [dash.page_container],
                    xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                )
            ]
        )
    ],
    fluid=True
)
   
"""

app.layout = html.Div(
    [
        # framework of the main app
        html.Div(
            "Domino eNPS Sentiment Analysis with Dash",
            style={
                'fontsize':50,
                'textAlign':'center'
            }
            ),
        html.Div(
            [
                dcc.Link(
                    children=page['name']+"  |  ",
                    href=page['path']
                ) for page in dash.page_registry.values()
            ]
        ),
        html.Hr(),
        dash.page_container # content for each page
    ]
)

"""

if __name__ == '__main__':
    app.run_server(debug=True)
    