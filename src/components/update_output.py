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