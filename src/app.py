import os
os.getcwd()

import dash
from dash import dcc, html

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ],
    suppress_callback_exceptions=True
)
    
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

if __name__ == '__main__':
    app.run_server(debug=True)