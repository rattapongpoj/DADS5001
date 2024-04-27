import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import base64
import io

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-data-upload')
])

# Define callback to process the uploaded file
@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              prevent_initial_call=True)
def update_output(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        
        # Assume uploaded file is a CSV and parse it into DataFrame
        try:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            # Process the DataFrame as needed
            return html.Div([
                html.H5('Uploaded CSV file contents:'),
                dcc.Textarea(value=df.to_string(), style={'width': '100%', 'height': 300})
            ])
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)