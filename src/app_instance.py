import dash

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ],
    suppress_callback_exceptions=True
)