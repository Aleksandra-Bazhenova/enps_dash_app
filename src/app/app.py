import sys
sys.path.append('../../')

from data import reshape_data

import base64
import datetime
import io

import dash
from dash import dcc, html
from dash import no_update
from dash import dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px


pages_folder=os.path.join(os.path.dirname(__name__), "pages")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        # framework of the main app
        html.Div("Domino eNPS Sentiment Analysis with Dash", style={'fontsize':50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(children=page['name']+"  |  ", href=page['path']) for page in dash.page_registry.values()
        ]),
        html.Hr(),
        
        # content for each page
        dash.page_container
    ]
)

def parse_contents(contents, filename, date):
    
    content_type, content_string = contents.split(',')
    
    decoded = base64.b64decode(content_string)
    
    try:
        if '.csv' in filename:
            # assume that the user uploaded a CSV file
            data = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))

        elif '.xls' in filename:
            # assume that the user uploaded an excel file
            data = pd.read_excel(io.BytesIO(decoded))
        
        # call on the reshape_data.py file which manipulates the data into a wider format
        df = reshape_data.make_wide_df(data)
        
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
                     options=[{'label':x, 'value':x} for x in df.columns]),
        html.Br(),
        html.P("Select Vertical Axis Data"),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label':x, 'value':x} for x in df.columns]),
        html.Br(),
        html.Button(id="submit-button", children="Create Graph"),
        html.Hr(), # horizontal line

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name':i, 'id':i} for i in df.columns],
            page_size=15,
            style_table={'overflowX': 'scroll'}
        ),
        dcc.Store(id='stored-data', data=df.to_dict('records')), # store data into users browser, max 2-3MB (can't use for very large files)
    ])

# first callback with output feeding into the html.Div(id='output-datatable') in the app.layout

""" In this callback function, the Input and States (contents,  filename, last_modified) are taken from the dcc.Upload above.
    These 3 props are then used as inputs into def update_output() function.
    'Input' will trigger dash callback; 'State' will not. 'State allows to pass extra information along without triggering the callback.
    The update_output() function checks that the list of contents is not None.
    It then uses the previously defined parse_contents() function to parse these file attributes.
"""
    
@app.callback(Output('output-datatable', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)
            ]
        return children


# second callback with output feeding into the html.Div(id='output-div') in the app.layout
@app.callback(Output('output-div', 'children'),
              Input('submit-button','n_clicks'),
              State('stored-data','data'),
              State('xaxis-data','value'),
              State('yaxis-data', 'value'))
def make_graphs(n, data, x_data, y_data):
    if n is None:
        return dash.no_update
    else:
        fig = px.histogram(data, x=x_data, color_discrete_sequence=['#003B5C'])
        fig.update_layout(
            plot_bgcolor='white',
            title=f"Count of Responses by {x_data}",
            title_x=0.5,
            xaxis={'categoryorder':'total descending'},
            xaxis_title="",
            yaxis_title="Count"
            )
        
        
        # print(data)
        return dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)