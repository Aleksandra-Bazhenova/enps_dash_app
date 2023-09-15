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