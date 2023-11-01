import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Home', path='/') # home page

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Upload(
                            id='upload-data',
                            children=html.Div(
                                [
                                    'Drag and Drop or ',
                                    html.A('Select Files', style={'color':'#003B5C'})
                                ],
                                style={'color':'#FFFFFF'}
                            ),
                            style={
                                'width':'100%',
                                'height':'60px',
                                'lineHeight':'60px',
                                'borderWidth':'1px',
                                'borderStyle':'dashed',
                                'borderRadius':'5px',
                                'borderColor':'#009639',
                                'backgroundColor':'#80CB9C',
                                'textAlign':'center'
                            },
                            multiple=True # allow multiple files selection
                        )
                    ],
                    width=12
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # this empty div is tied to the second callback function, which contains the graph. It's physicall positioned between the data table and the upload component
                        html.Div(id='output-div')
                    ],
                    width=12
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        # this empty div will contain the output children from the first callback function
                        html.Div(id='output-datatable')
                    ],
                    width=12
                )
            ]
        )
    ]
)

"""

layout = html.Div([ # this code section taken from Dash docs https://dash.plotly.com/dash-core-components/upload
    # CSS style the upload component
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files',
                   style={'color':'#003B5C'})
        ],
                          style={'color':'#FFFFFF'}),
        style={
            'width':'100%',
            'height':'60px',
            'lineHeight':'60px',
            'borderWidth':'1px',
            'borderStyle':'dashed',
            'borderRadius':'5px',
            'borderColor':'#009639',
            'backgroundColor':'#80CB9C',
            'textAlign':'center'
        },
        # allow multiple files to be uploaded
        multiple=True
    ),
    
    # this empty div is tied to the second callback function, which contains the graph. It's physicall positioned between the data table and the upload component
    html.Div(id='output-div'),
    # this empty div will contain the output children from the first callback function
    html.Div(id='output-datatable'),
])

"""