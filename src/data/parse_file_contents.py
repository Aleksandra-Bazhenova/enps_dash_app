import base64
import datetime
import io

import pandas as pd

from dash import dcc, html
from dash import dash_table

from data import reshape_data, column_manager

def parse_contents(contents, filename, date):
    
    content_type, content_string = contents.split(',')
    
    decoded = base64.b64decode(content_string)
    
    try:
        if '.csv' in filename:
            # assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))

        elif '.xls' in filename:
            # assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        
        # call on the reshape_data.py file which manipulates the data into a wider format
        wide_df = reshape_data.make_wide_df(df)
        wide_df = column_manager.nps_label_based_on_score(wide_df)
        
    except Exception as e:
        print(e)
        return html.Div([
            "There was an error processing this file. Please see the 'Help' page to learn more about expected file and data format."
        ])

    # return CSS-styled html.Div components with the file contents
    
        """ This output will be returned inside update_output(),
            which in turn will provide children for the html.Div with the id='output-datatable'
        """    
    return html.Div([
        html.H6([html.B("File Name: "), filename.split('.')[0]],
        style={
            'font-size':'0.75em',
            'color':'#003B5C'
            }),
        html.H6([html.B("File Type: "), filename.split('.')[1].upper()],
        style={
            'font-size':'0.75em',
            'color':'#003B5C'
            }),
        html.H6([html.B("File Last Modified On: "), str(datetime.datetime.fromtimestamp(date))],
                style={
                    'font-size':'0.75em',
                    'color':'#003B5C'
                    }),
        html.Br(),
        html.P("Select Horizonal Axis Data"),
        dcc.Dropdown(id='xaxis-data',
                     options=[{'label':x, 'value':x} for x in wide_df.columns]),
        html.Br(),
        html.P("Select Vertical Axis Data"),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label':x, 'value':x} for x in wide_df.columns]),
        html.Br(),
        html.Button(id="graph_explorer_submit_button", children="Create Graph"),
        html.Hr(), # horizontal line

        dash_table.DataTable(
            data=wide_df.to_dict('records'),
            columns=[{'name':i, 'id':i} for i in wide_df.columns],
            page_size=15,
            style_table={'overflowX': 'scroll'}
        ),
        dcc.Store(id='stored-data', data=wide_df.to_dict('records')), # store data into users browser, max 2-3MB (can't use for very large files)
    ])
