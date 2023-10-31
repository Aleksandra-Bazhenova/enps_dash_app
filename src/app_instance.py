import dash
import dash_bootstrap_components as dbc

# external_stylesheets = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
external_stylesheets = dbc.themes.SPACELAB

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[external_stylesheets],
    suppress_callback_exceptions=True
)