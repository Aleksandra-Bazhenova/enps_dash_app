import dash
from dash import dcc, html

from utils import openai_sentiment

dash.register_page(__name__, name='Sentiment Analysis')

layout = html.Div(
    [
        dcc.Markdown('# This will be the content of Page 2')
    ]
)