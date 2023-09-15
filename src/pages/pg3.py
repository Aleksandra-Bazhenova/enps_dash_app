import sys
sys.path.append('../../')
from data import reshape_data

import base64
import datetime
import io

import pandas as pd
import numpy as np

import dash
from dash import dcc, html
from dash import no_update
from dash import dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px

dash.register_page(__name__)

layout = html.Div(
    [
        dcc.Markdown('# This will be the content of Page 3')
    ]
)
