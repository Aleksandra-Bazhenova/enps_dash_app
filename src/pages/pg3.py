import dash
from dash import dcc, html

dash.register_page(__name__, name='Theme Detection')

layout = html.Div(
    [
        dcc.Markdown('# This will be the content of Page 3')
    ]
)
